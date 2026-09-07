class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l=[]
        mx=max(candies)
        for i in candies:
            if i+extraCandies >= mx:
                l.append(True)
            else:
                l.append(False)
        return l            

        