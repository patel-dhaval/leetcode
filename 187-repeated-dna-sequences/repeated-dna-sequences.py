class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        repeated = set()

        for idx in range(len(s) - 9):
            curr = s[idx: idx + 10]

            if curr in seen:
                repeated.add(curr)
            else:
                seen.add(curr)

        
        return list(repeated)