class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        good = 0
        for i in hours:
            if  i >= target:
                good += 1
        return good
                
