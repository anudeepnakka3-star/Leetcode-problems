class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        prefmax=[0]*n
        suffmax=[0]*n
        prefmax[0]=height[0]
        suffmax[n-1]=height[n-1]
        for i in range(1,n):
            prefmax[i]=max(prefmax[i-1],height[i])
        for i in range(n-2,-1,-1):
            suffmax[i]=max(suffmax[i+1],height[i])
        total=0
        for i in range(n):
            leftmax,rightmax=prefmax[i],suffmax[i]
            if height[i]<leftmax and height[i]<rightmax:
                total+=min(leftmax,rightmax)-height[i]
        return total
        