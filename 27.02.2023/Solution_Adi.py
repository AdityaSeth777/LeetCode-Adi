class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # Define a recursive helper function to build the quad tree
        def build_quad_tree(grid, top, left, bottom, right):
            # Check if the sub-matrix is homogeneous (i.e., all values are the same)
            is_homogeneous = True
            val = grid[top][left]
            for i in range(top, bottom):
                for j in range(left, right):
                    if grid[i][j] != val:
                        is_homogeneous = False
                        break
                if not is_homogeneous:
                    break

            # If the sub-matrix is homogeneous, create a leaf node
            if is_homogeneous:
                return Node(val, True, None, None, None, None)

            # Otherwise, recursively build the quad tree
            mid_row = (top + bottom) // 2
            mid_col = (left + right) // 2
            topLeft = build_quad_tree(grid, top, left, mid_row, mid_col)
            topRight = build_quad_tree(grid, top, mid_col, mid_row, right)
            bottomLeft = build_quad_tree(grid, mid_row, left, bottom, mid_col)
            bottomRight = build_quad_tree(grid, mid_row, mid_col, bottom, right)

            return Node(None, False, topLeft, topRight, bottomLeft, bottomRight)

        # Call the recursive helper function to build the quad tree
        n = len(grid)
        return build_quad_tree(grid, 0, 0, n, n)
