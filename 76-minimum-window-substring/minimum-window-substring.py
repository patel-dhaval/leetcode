class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        countT = {}
        window = {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have = 0
        need = len(countT)
        res = [-1, -1]
        resLen = float('inf')
        l = 0
        for r in range(len(s)):
            curr_char = s[r]
            window[curr_char] = 1 + window.get(curr_char, 0)

            if curr_char in countT and window[curr_char] == countT[curr_char]:
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

        return s[l:r+1] if resLen != float('inf') else ""
