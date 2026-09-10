class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        count={0:-1}
        prefix=0
        for i,x in enumerate(nums):
            prefix+=x
            rem=prefix%k
            if rem not in count:
                count[rem]=i
            elif i-count[rem] >=2:
                return True

        return False




        