class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_number_map = {2: "abc", 3:"def", 4: "ghi", 5: "jkl", 6: "mno", 7:"pqrs", 8: "tuv", 9: "wxyz"}

        res = []

        def backtrack(idx, char_arr):
            if idx > len(digits):
                return
            
            if len(char_arr) == len(digits):
                res.append("".join(char_arr))
                return

            for j in range(idx, len(digits)):
                char = digit_to_number_map[int(digits[j])]
                for c in char:
                    char_arr.append(c)
                    backtrack(j+1, char_arr)
                    char_arr.pop()
            
        backtrack(0, [])
        return res

            