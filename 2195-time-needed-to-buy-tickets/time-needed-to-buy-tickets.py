class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        q=deque()
        for i in range(len(tickets)):
            q.append(i)
        t=0
        while tickets[k]>0:
            f=q.popleft()
            tickets[f]-=1
            if tickets[f]>0:
                q.append(f)
            t+=1
        return t