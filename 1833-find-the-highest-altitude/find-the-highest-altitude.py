class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        count={0,1}
        prefix=0
        maxi=0
        for x in gain:
            prefix+=x
            maxi=max(maxi,prefix)
        return maxi

        