class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n=len(digits)
        vis=[False]*1000
        ans=[]
        for i in range(n):
            if digits[i]==0:
                continue
            for j in range(n):
                if j==i:
                    continue
                for k in range(n):
                    if k==i or k==j or digits[k]%2!=0:
                        continue
                    else:
                        x=digits[i]*100+digits[j]*10+digits[k]
                        if not vis[x]:
                            vis[x]=True
                            ans.append(x)
        ans.sort()
        return ans

        