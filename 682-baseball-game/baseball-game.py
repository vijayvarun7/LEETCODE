class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s=[]
        sum=0
        for i in operations:
            if i.lstrip("-").isnumeric():
                s.append(int(i))
                sum+=int(i)
            elif i=="C":
                sum-=s[-1]
                s.pop()
            elif i=="D":  
                s.append(s[-1]*2)
                sum+=s[-1]
            elif i=="+":  
                s.append(s[-1]+s[-2])
                sum+=s[-1]
        return sum