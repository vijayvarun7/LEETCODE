class Solution:
    def reverseDegree(self, s: str) -> int:
        a=0
        for i in range(len(s)):
            a+=(i+1)*(97-ord(s[i])+26)
        return a