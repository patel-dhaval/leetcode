class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_letter_map = {
            '1': None,
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w','x', 'y', 'z'],
            '0': None
        }
        res = []
        def helper(index, currComb):
            print(currComb, res)
            
            if index > len(digits):
                return

            if index == len(digits) and len(currComb) == len(digits):
                res.append(''.join(currComb.copy()))
                return
            
            for i in range(index, len(digits)):
                vals = num_letter_map.get(digits[i])
                for v in vals:
                    currComb.append(v)
                    helper(i+1, currComb)
                    currComb.pop()
            
        
        helper(0, [])
        
        return res if res != [""] else []

            
