class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i=0
        n=1
        while(k>0):
            if (i<len(arr) and n==arr[i]):
                i+=1
            else:
                k-=1
            n+=1
        return n-1



        