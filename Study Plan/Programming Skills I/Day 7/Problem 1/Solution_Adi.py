class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        primary_sum = 0
        secondary_sum = 0

        for i in range(n):
            primary_sum += mat[i][i]
            secondary_sum += mat[i][n-i-1]

        if n % 2 == 1:
            secondary_sum -= mat[n//2][n//2]

        return primary_sum + secondary_sum
