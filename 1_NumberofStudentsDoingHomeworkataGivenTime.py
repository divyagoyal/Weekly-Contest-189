class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count=0
        for i,st in enumerate(startTime):
            if queryTime>=st and queryTime<=endTime[i]:
                count+=1
        return count
        
