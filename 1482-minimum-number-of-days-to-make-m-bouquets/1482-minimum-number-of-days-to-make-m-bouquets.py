class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def possible(bloomDay,day,m,k):
            c=0
            bouq=0
            for i in range(n):
                if bloomDay[i]<=day:
                    c+=1
                elif bloomDay[i]>day:
                    bouq+=c//k
                    c=0
            bouq+=c/k
            if bouq>=m:
                return True
            else:
                return False

        n=len(bloomDay)
        if m*k>n:
            return -1
        l=min(bloomDay)
        r=max(bloomDay)
        ans=r
        while l<=r:
            mid=(l+r)//2
            if possible(bloomDay,mid,m,k)==True:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
                
        return -1
                
                
            
        