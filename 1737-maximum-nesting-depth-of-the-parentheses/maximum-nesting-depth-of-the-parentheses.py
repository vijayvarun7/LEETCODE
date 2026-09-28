class Solution:
    def maxDepth(self, s: str) -> int:
        a,b=0,0
        k=0
        ans=0
        for i in s:
            if i=="(":
                a+=1
            elif i==")":
                b+=1            
            elif i.isnumeric() or ((i=="*") or (i=="-") or (i=="/") or (i=="+")):
                k+=1
            ans=max(a-b,ans)
        return ans
