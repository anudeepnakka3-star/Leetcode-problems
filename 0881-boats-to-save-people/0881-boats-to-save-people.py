class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        n=len(people)
        ans=0
        l=0
        r=n-1
        while l<=r:
            if people[l]+people[r]<=limit:
                ans+=1
                l+=1
                r-=1
            elif people[l]+people[r]>limit:
                ans+=1
                r-=1
        return ans
        