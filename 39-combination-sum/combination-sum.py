class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def generateCombinations(i, combination):
            if i >= len(candidates) or sum(combination) > target:
                return

            if sum(combination) == target:
                res.append(combination.copy())
                return
            
            combination.append(candidates[i])
            generateCombinations(i, combination)
            combination.pop()
            generateCombinations(i+1, combination)

        generateCombinations(0, [])

        return res