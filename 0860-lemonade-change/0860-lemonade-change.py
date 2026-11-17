class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five=0
        ten=0
        twenty=0
        n=len(bills)
        if bills[0]==10 or bills[0]==20:
            return False
        for i in range(n):
            if bills[i]==5:
                five+=1
            elif bills[i]==10:
                ten+=1
                if five>0:
                    five-=1
                else:
                    return False
            elif bills[i]==20:
                twenty+=1
                if five>0 and ten>0:
                    five-=1
                    ten-=1
                elif ten==0 and five>2:
                    five-=3
                else:
                    return False
            
        return True

        