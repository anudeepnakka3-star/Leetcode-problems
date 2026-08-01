class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        s1=s+s
        if s1.find(goal)!=-1:
            return True
        else:
            return False


        
        