# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         mapping = {2: 'abc',3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
#         res = []
#         letter_combinations = []

#         def combinationGenerator(index, letter_combinations):
#             if len(letter_combinations) == len(digits):
#                 temp_copy = letter_combinations.copy()
#                 local_res = ''.join(temp_copy)
#                 res.append(local_res)
#                 return
            
#             for i in range(index, len(digits)):
#                 char = mapping[int(digits[index])]
#                 for c in char: 
#                     letter_combinations.append(c)
#                     combinationGenerator(i+1, letter_combinations)
#                     letter_combinations.pop()
            
#         if len(digits) < 1:
#             return []

#         combinationGenerator(0, [])

#         return res


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:  # Handle empty input early
            return []

        # Store mapping with string keys
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        res = []

        def combinationGenerator(index, letter_combinations):
            if index == len(digits):  # Base case: fully processed digits
                res.append(''.join(letter_combinations))
                return

            for c in mapping[digits[index]]:
                letter_combinations.append(c)
                combinationGenerator(index + 1, letter_combinations)  # Move to the next digit
                letter_combinations.pop()  # Backtrack

        combinationGenerator(0, [])
        return res