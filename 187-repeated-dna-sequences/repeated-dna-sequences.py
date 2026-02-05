class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        i = 0
        sequences = {}
        res = []
        if len(s) <= 10:
            return []

        for j in range(len(s)):
            if j - i + 1 == 10:
                seq = tuple(s[i:j+1])
                sequences[seq] = sequences.get(seq, 0) + 1
                i += 1
            
        for k, v in sequences.items():
            if v > 1:
                res.append(''.join(list(k)))
        
        return res