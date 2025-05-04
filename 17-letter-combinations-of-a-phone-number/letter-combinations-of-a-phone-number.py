class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:  # Handle empty input early
            return []
        
        num_letter_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w','x', 'y', 'z'],
        }
        res = []
        def helper(index, currComb):
            
            if index > len(digits):
                return

            if index == len(digits):
                res.append(''.join(currComb.copy()))
                return
        
            for v in num_letter_map[digits[index]]:
                currComb.append(v)
                helper(index+1, currComb)
                currComb.pop()
        
        
        helper(0, [])
        
        return res

            
