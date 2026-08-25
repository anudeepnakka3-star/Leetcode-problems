class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans=start^goal
        def convert_binary(num):
            result=""
            while num>0:
                if num%2==1:
                    result+="1"
                else:
                    result+"0"
                num=num//2
            return result[::-1]
        res=convert_binary(ans)
        c=0
        for i in res:
            if i=="1":
                c+=1
        return c
