class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combinations = []
        candidates.sort()
        def combinationGenerator(index, current_sum):
            if current_sum == target:
                res.append(combinations.copy())
                return
            
            if current_sum > target:
                return
            processed_ip = set()
            for i in range(index, len(candidates)):
                if candidates[i] not in processed_ip:
                    processed_ip.add(candidates[i])
                    combinations.append(candidates[i])
                    combinationGenerator(i+1, current_sum + candidates[i])
                    combinations.pop()
        
        combinationGenerator(0, 0)
        return res
