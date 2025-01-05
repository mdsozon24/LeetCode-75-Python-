class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        s = list(senate)
        d,r=[],[]
        for i,c in  enumerate(s):
            if c == 'R':
                r.append(i)
            else:
                d.append(i)

        while d and r:
            x = d.pop(0)
            y = r.pop(0)
            if x<y:
                d.append(x+len(s))
            else:
                r.append(y+len(s))

        return 'Radiant' if r else 'Dire'