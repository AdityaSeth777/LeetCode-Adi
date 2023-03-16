class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []

        def helper(curr=root):
            nonlocal ans
            if curr:
                ans.append(curr.val)
                for i in curr.children:
                    helper(i)
        helper()
        return ans
