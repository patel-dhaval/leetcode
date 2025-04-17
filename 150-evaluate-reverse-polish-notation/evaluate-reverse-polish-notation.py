class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        def addition(num1, num2) -> int:
            return int(num1) + int(num2)
        
        def subtraction(num1, num2) -> int:
            return int(num1) - int(num2)
        
        def multiply(num1, num2) -> int:
            return int(num1) * int(num2)
        
        def divide(num1, num2) -> int:
            if int(num2) == 0:
                raise ValueError
            return int(num1) / int(num2)
        
        val_stack = []
        symbols = ['+', '-', '*', '/']
        symbols = set(symbols)

        for v in tokens:
            if v not in symbols:
                val_stack.append(v)
            else:
                num2 = val_stack.pop()
                num1 = val_stack.pop()

                if v == '+':
                    res = addition(num1, num2)
                    val_stack.append(res)
                elif v == '-':
                    res = subtraction(num1, num2)
                    val_stack.append(res)
                elif v == '*':
                    res = multiply(num1, num2)
                    val_stack.append(res)
                elif v == '/':
                    res = divide(num1, num2)
                    val_stack.append(res)
        return int(val_stack[-1])

        
        