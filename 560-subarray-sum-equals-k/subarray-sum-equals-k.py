class Solution:
    def subarraySum(self, nums, k):
        count={0:1}
        prefix=0
        ans=0
        for x in nums:
            prefix+=x
            su=prefix-k
            if su in count:
                ans+=count[su]
            count[prefix]=count.get(prefix,0)+1
        return ans