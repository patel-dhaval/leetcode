class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # One array to track "Net Trust Score"
        # indegree - outdegree
        scores = [0] * (n + 1)

        for a, b in trust:
            scores[a] -= 1  # Person A trusts someone (penalty)
            scores[b] += 1  # Person B is trusted (gain)

        for i in range(1, n + 1):
            # If net score is N-1, they are trusted by everyone 
            # AND they trust no one (otherwise score would be lower)
            if scores[i] == n - 1:
                return i
        
        return -1