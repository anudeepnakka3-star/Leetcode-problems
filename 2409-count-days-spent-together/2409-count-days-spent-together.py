class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def days(day,pref):
            month=int(day[:2])
            date=int(day[3:])
            return pref[month-1]+ date
        
        datesOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        pref=[0]
        for date in datesOfMonths:
            pref.append(pref[-1]+date)
        
        alday=days(arriveAlice,pref)
        laday=days(leaveAlice,pref)
        abday=days(arriveBob,pref)
        lbday=days(leaveBob,pref)

        return max(0,min(laday,lbday)-max(alday,abday)+1)
        

        