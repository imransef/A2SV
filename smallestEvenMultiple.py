class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        rst = 0
        for i in range (2,99999999999999):
            
            if (i>=n):
                if i%n == 0 and i%2 == 0:
                    rst = i
                    break
        return rst
                
                
