class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        r=[]
        l=[]
        s=[]
        for i in  range(n):
            r.append(nums[i])
        for j in range(n,len(nums)):
            l.append(nums[j]) 
        for k in range(n):
            s.append(r[k])
            s.append(l[k]) 
        return s       

        