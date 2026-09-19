
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
            n=len(nums)
            l=0
            r=0
            cnt=0
            ans=[]
            idx=0
            while r<n:
                if r>0 and nums[r]-nums[r-1]==1:
                    cnt+=1
                if r-l+1>=k:
                    ans.append(nums[r] if cnt == k - 1 else -1)
                    if l<n-1 and nums[l+1]-nums[l]==1:
                        cnt-=1
                    l+=1
                r+=1
            return ans


        