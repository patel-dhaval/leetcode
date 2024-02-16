class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) == len(t)):
            hmap_s = {}
            for i in range(0, len(s)):
                if s[i] in hmap_s:
                    hmap_s[s[i]] = (hmap_s[s[i]] + 1)
                else:
                    hmap_s[s[i]] = 1
            hmap_t = {}
            for i in range(0, len(t)):
                if t[i] in hmap_t:
                    hmap_t[t[i]] = (hmap_t[t[i]] + 1)
                else:
                    hmap_t[t[i]] = 1
                
            if hmap_s == hmap_t:
                return True
        return False