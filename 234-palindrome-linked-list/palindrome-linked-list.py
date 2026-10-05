# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        a=[]
        t=head
        while t!=None:
            a.append(t.val)
            t=t.next
        j=len(a)-1
        i=0
        while i<j:
            if a[i]!=a[j]:
                return False
            i+=1
            j-=1
        return True

        


        