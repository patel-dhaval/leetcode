class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        
        digit_to_char = {1:"", 2: "abc", 3:"def", 4: "ghi", 5:"jkl", 6:"mno", 7: "pqrs", 8:"tuv", 9: "wxyz"}
        
        
        def backtrack(idx, combination):
            
            if len(combination) == len(digits):
                res.append("".join(combination.copy()))
                return
            
            for j in range(idx,len(digits)):
                digit = int(digits[j])
                
                chars = digit_to_char[digit]
                
                for c in chars:
                    combination.append(c)
                    backtrack(j+1, combination)
                    combination.pop()
        
        backtrack(0,[])
        
        return res