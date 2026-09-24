class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            sumi=0
            digitals=0
            t=nums[i]
            while t > 0:
                digitals=t%10
                sumi=sumi+digitals
                t =t//10
            if sumi == i:
                return i
        
        return -1


        