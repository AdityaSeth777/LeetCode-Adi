class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        if m * n != r * c:
            return mat
        
        flat_mat = [elem for row in mat for elem in row]
        
        reshaped_mat = []
        for i in range(r):
            row = flat_mat[i*c : (i+1)*c]
            reshaped_mat.append(row)
        
        return reshaped_mat
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        if m * n != r * c:
            return mat
        
        flat_mat = [elem for row in mat for elem in row]
        
        reshaped_mat = []
        for i in range(r):
            row = flat_mat[i*c : (i+1)*c]
            reshaped_mat.append(row)
        
        return reshaped_mat