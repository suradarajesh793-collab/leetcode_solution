class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        r=1
        s=set(nums)
        h=len(s)
        for i in range(h+1):
            if r in s:
                r=r+1
            else:
                return r
        