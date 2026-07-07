class Solution:
    def sumAndMultiply(self, n: int) -> int:
        summ=0
        x=0
        for i in str(n):
            digit=int(i)
            if digit!=0:
                x=x*10+digit
                summ+=digit
        return summ*x