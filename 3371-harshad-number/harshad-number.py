class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        n=x
        s=0
        while n>0:
            s=s+n%10
            n=n//10
        if x%s==0:
            return s
        else:
            return-1
    

        