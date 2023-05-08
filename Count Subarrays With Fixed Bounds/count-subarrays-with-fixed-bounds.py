class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # find the subarray with min value is minK and max value is maxK
        # find the index of the min value and max value.
        # first, find the longest subarrays with minK and maxK
        # then, find each number of subarrays for each array
        def findArrays(nums, minK, maxK):
            nums.append(0)
            res = []
            arr = []
            for i in range(len(nums)):
                if nums[i] >= minK and nums[i] <= maxK:
                    arr.append(nums[i])
                else:
                    if arr and min(arr)==minK and max(arr)==maxK:
                        res.append(arr)
                    arr = []
            return res
        
        def calculateSubarrays(arr, minK, maxK):
            res = 0
            # use queue tostore the index of the minK and max K
            queue = []
            prev = 0
            n = len(arr)
            if minK==maxK:
                return n//2*(n+1) if n%2==0 else (n+1)//2*n
            for i in range(len(arr)):
                if i>=prev and (arr[i] == minK or arr[i] == maxK):
                    # print(queue)
                    while len(queue)>0 and arr[queue[len(queue)-1]] !=arr[i]:
                        index = queue.pop(0)
                        beforeCount = index -prev+1
                        afterCount = n - i
                        res += beforeCount*afterCount
                        # print(prev,index,i,beforeCount,afterCount)
                        prev = index+1
                    queue.append(i)
            return res

        # main body
        arrs = findArrays(nums, minK, maxK)
        ans = 0
        for arr in arrs:
            ans+=calculateSubarrays(arr, minK, maxK)
        return ans