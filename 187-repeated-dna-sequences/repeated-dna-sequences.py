class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        i = 0
        seen = set()
        res = set()
        if len(s) < 10:
            return []

        for j in range(len(s)):
            if j - i + 1 == 10:
                seq = s[i:j+1]
                if seq in seen:
                    res.add(seq)
                else:
                    seen.add(seq)
                i+=1
        
        return list(res)