"""
DRY RUN:

IP: "ABAACDABC"

OP: "ABC"
countT: {A: 1, B: 1, C: 1}

have = 3
need = 3
window = {A: 1, B:1, C:1, D: 0}
l = 6
r = 8

curr = C

resLen = 3
res = [6, 8]
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        countT = collections.defaultdict(int)
        
        for c in t:
            countT[c] += 1
        
        have = 0
        need = len(countT)
        window = collections.defaultdict(int)
        l = 0
        res = [-1, -1]
        resLen = float("inf")
        for r in range(len(s)):
            curr = s[r]
            window[curr] += 1

            if curr in countT and window[curr] == countT[curr]:
                have += 1

            while have == need:    
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r]

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1
            
        l, r = res

        return s[l: r+1] if resLen != float("inf") else ""