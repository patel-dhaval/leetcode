class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(index, currComb):
            if len(currComb) > k:
                return
            
            if len(currComb) == k:
                res.append(currComb.copy())
                
            for i in range(index, n+1):
                currComb.append(i)
                helper(i+1, currComb)
                currComb.pop()
        
        helper(1, [])
        return res
