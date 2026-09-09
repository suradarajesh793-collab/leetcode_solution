class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count={0:1}
        prefix=0
        ans=0
        for x in nums:
            prefix +=x
            rem=prefix%k
            if rem in count:
                ans+=count[rem]
            count[rem]=count.get(rem,0) + 1
        return ans 

        