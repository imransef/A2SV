class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = 0
        mp = {}
        for i in nums:
            if i in mp:
                mp[i] += 1
            else:
                mp[i] = 1
        for k in mp:
            counter +=  mp[k]*(mp[k]-1)//2
        return counter
