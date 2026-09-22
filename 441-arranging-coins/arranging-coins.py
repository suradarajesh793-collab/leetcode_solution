class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows=1
        while n>=rows:
            n=n-rows 
            rows=rows + 1
        return rows-1

        