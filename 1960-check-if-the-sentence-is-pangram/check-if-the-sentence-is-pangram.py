class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        freq_arr = [0] * 26

        for i in sentence:
            freq_arr[ord(i) - ord("a")] += 1
        
        for c in freq_arr:
            if c == 0:
                return False
        return True