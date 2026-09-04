class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        n=len(nums2)
        ans=[-1]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while len(stack)!=0 and stack[-1]<=nums2[i]:
                stack.pop()
            if len(stack)!=0:
                ans[i]=stack[-1]
            stack.append(nums2[i])
        l=0
        r=0
        while l<len(nums1) :
            if nums1[l]==nums2[r]:
                nums1[l]=ans[r]
                l+=1
                r=0
            else:
                r+=1
        return nums1
    """
        n=len(nums2)
        stack=[]
        next_greater={}
        for i in range(n):
            while  len(stack)!=0 and stack[-1]<=nums2[i]:
                next_greater[stack.pop()]=nums2[i]
            stack.append(nums2[i])
        for num in stack:
            next_greater[num]=-1
        ans=[]
        for i in range(len(nums1)):
            ans.append(next_greater[nums1[i]])
        return ans                   
        