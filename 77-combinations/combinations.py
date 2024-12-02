class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        subset = []

        def combinationGenerator(curr_number, subset):
            if len(subset) == k:
                res.append(subset.copy())

            if curr_number <= n:
                for i in range(curr_number, n+1):
                    subset.append(i)
                    combinationGenerator(i+1, subset)
                    subset.pop()
                
        combinationGenerator(1, [])

        return res