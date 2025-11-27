class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def generateCombinations(idx, combination):
            if idx >= len(candidates) or sum(combination) > target:
                return

            if sum(combination) == target:
                res.append(combination.copy())
                return
            
            for i in range(idx, len(candidates)):
                combination.append(candidates[i])
                generateCombinations(i, combination)
                combination.pop()

        generateCombinations(0, [])
        return res