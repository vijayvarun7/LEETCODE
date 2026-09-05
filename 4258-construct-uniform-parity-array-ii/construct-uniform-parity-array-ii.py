class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n,m=0,0
        for i in nums1:
            if i%2==0:
                n+=1
            else:
                m+=1
        if n==len(nums1) or m==len(nums1):
            return True
        if m>=1 and min(nums1)%2==1:
            return True
        return False
