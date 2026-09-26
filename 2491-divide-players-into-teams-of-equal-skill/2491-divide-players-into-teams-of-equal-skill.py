class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        n=len(skill)
        l=0
        r=n-1
        temp=skill[0]+skill[n-1]
        res=0
        teams=n//2
        team=0
        while l<r:
            if skill[l]+skill[r]==temp:
                res+=(skill[l]*skill[r])
                team+=1
                l+=1
                r-=1
            else:
                return -1
        return res

