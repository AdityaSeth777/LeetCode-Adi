class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        stack,ans=[],[]
        
        for i in obstacles:
            br=bisect_right(stack,i)
            if br==len(stack):
                stack.append(i)
            else:
                stack[br]=i
            ans.append(br+1)
            
        return ans