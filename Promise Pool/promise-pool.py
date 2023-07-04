class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)-2):
            if arr[i+2]-arr[i+1] == arr[i+1]-arr[i]:
                continue
            else:
                return False
        return True