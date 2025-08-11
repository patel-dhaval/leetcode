"""
Approach:
Hashmap of open and close brackets, where closed are keys and open is value
Use a stack to track the brackets
When we encounter open bracket, we push it to the stack
When we encounter closed bracket, we check the top of the stack, if the top of the stack matches the dict value for it, then its a valid series, as it will suggest that an open bracket follows a closed bracket

"""
class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) < 2:
            return False
        
        val_stack = []
        bracket_dict = {")": "(", "}":"{", "]":"["}

        for i in range(len(s)):
            if s[i] not in bracket_dict.keys():
                val_stack.append(s[i])
            else:
                if val_stack and bracket_dict[s[i]] == val_stack[-1]:
                    val_stack.pop()
                else:
                    return False
        return True if not val_stack else False
        