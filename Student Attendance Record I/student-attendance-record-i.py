class Solution:
    def checkRecord(self, s: str) -> bool:
        absences = 0
        consecutive_lates = 0
        
        for day in s:
            if day == 'A':
                absences += 1
                consecutive_lates = 0
                if absences >= 2:
                    return False
            elif day == 'L':
                consecutive_lates += 1
                if consecutive_lates >= 3:
                    return False
            else:
                consecutive_lates = 0
        
        return True