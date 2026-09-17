class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        def nse(arr):
            n=len(arr)
            nse=[0]*n
            stack=[]
            for i in range(n-1,-1,-1):
                while stack and arr[stack[-1]]>=arr[i]:
                    stack.pop()
                if len(stack)!=0:
                    nse[i]=stack[-1]
                else:
                    nse[i]=n
                stack.append(i)
            return nse
        def psee(arr):
            n=len(arr)
            psee=[0]*n
            stack=[]
            for i in range(n):
                while stack and arr[stack[-1]]>arr[i]:
                    stack.pop()
                if len(stack)!=0:
                    psee[i]=stack[-1]
                else:
                    psee[i]=-1
                stack.append(i)
            return psee
        n=len(arr)
        ans=0
        mod=10**9 +7
        nsee=nse(arr)
        pse=psee(arr)
        for i in range(n):
            left=i-pse[i]
            right=nsee[i]-i
            frq= left*right*1
            val=(frq*arr[i])%mod
            ans=(ans+val)%mod
        return ans