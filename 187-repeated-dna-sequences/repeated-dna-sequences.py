"""
AAAAACCCCC
"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        repeated = set()

        for idx in range(0, len(s) - 9):
            word = s[idx: idx+10]

            if word in seen:
                repeated.add(word)
            else:
                seen.add(word)
        
        return list(repeated)