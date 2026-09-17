class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n=len(blocks)
        l=0
        ans=float("inf")
        w_count=0
        b_count=0
        for r in range(n):
            if blocks[r]=="W":
                w_count+=1
            else:
                b_count+=1
            if r-l==k:
                if blocks[l]=="W":
                    w_count-=1
                else:
                    b_count-=1
                l+=1
            if r-l+1==k:
                ans=min(ans,w_count)
        return ans
        