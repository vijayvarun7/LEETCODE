class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        elif n>=1000 and n<=999999:
            return n-999
        elif n>=1000000 and n<=999999999:
            return 999000+(n-999999)*2
        elif n>=1000000000 and n<=999999999999:
            return 1998999000 +(n-999999999)*3
        elif n==1000000000000000:
            return 2998998999000+(n-999999999999)*4+1
        else:
            return 2998998999000+(n-999999999999)*4
