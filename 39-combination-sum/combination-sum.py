class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(index, currComb, combs):
            if sum(currComb) > target:
                return
            
            if sum(currComb) == target:
                combs.append(currComb.copy())
                return

            
            for i in range(index, len(candidates)):
                currComb.append(candidates[i])
                helper(i, currComb, combs)
                currComb.pop()
            
            return combs
        
        return helper(0, [], [])