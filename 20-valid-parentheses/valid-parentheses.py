class Solution:
    def isValid(self,s: str) -> bool:
        l=[]
        if len(s)%2==1:
            return False
        for i in range(len(s)):
            if s[i]=="{" or s[i]=="(" or s[i]=="[":
                l.append(s[i])
            elif l and ((l[-1]=="{" and s[i]=="}") or (l[-1]=="[" and s[i]=="]") or (l[-1]=="(" and s[i]==")")):
                l.pop()
            else:
                return False
        return len(l)==0