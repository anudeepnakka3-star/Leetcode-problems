class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        for ch in s:
            if ch not in freq:
                freq[ch]=1
            else:
                freq[ch]+=1
        res=""
        sorted_freq=dict(sorted(freq.items(),key=lambda item:item[1],reverse=True))
        for i in sorted_freq:
            while sorted_freq[i]!=0:
                res+=i
                sorted_freq[i]-=1
        return res
        