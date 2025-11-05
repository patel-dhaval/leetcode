class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) < 2:
            return int(tokens[0])

        val_stack = []
        operators = ["+", "-", "/", "*"]
        for c in tokens:
            if c not in operators:
                val_stack.append(c)
            else:
                val1 = val_stack.pop()
                val2 = val_stack.pop()
                if c == "+":
                    temp_val = int(val2) + int(val1)
                elif c == "-":
                    temp_val = int(val2) - int(val1)
                elif c == '*':
                    temp_val = int(val2) * int(val1)
                elif c == '/':
                    temp_val = (int(val2)/int(val1))
                val_stack.append(int(temp_val))
        soln = 0

        for val in val_stack:
            soln += val
        return soln