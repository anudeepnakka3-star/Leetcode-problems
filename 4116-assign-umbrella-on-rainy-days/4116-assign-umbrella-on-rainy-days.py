class Solution:
    def assignUmbrella(self, rain: list[int]) -> list[str]:
        
        n=len(rain)
        result=[""]*n
        alice=0
        bob=0
        for i in range(n-1):
            if rain[i]==rain[i+1]==1:
                if bob<alice:
                    result[i]="Bob"
                    bob+=1
                else:
                    result[i]="Alice"
                    alice+=1
            elif rain[i]==1 and rain[i]!=rain[i+1]:
                result[i]="Bob"
                bob+=1
            elif rain[i]==0:
                result[i]="None"
        if rain[-1]==1:
            result[-1]="Bob"
        else:
            result[-1]="None"

        return result
                
        