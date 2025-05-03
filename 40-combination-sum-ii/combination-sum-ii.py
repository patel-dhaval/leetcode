class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combs = []
        def helper(index, currComb, curr_sum):
            if curr_sum > target:
                return
            
            if curr_sum == target:
                combs.append(currComb.copy())
                return

            prev = -1
            for i in range(index, len(candidates)):
                if candidates[i] != prev: 
                    currComb.append(candidates[i])
                    helper(i+1, currComb, curr_sum + candidates[i])
                    currComb.pop()
                    prev = candidates[i]
            return
        
        helper(0, [], 0)

        return combs