class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        rst = []
        a = nums[:n]
        b = nums[n:]
        for i in range(n):
            rst.append(a[i])
            rst.append(b[i])
        return rst
