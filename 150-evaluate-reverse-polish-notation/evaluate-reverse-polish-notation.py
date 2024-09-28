class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        if len(tokens) < 2:
            return int(tokens[0])

        stack = []
        operationArr = ['+', '-', '*', '/']

        stack.append(tokens[0])
        stack.append(tokens[1])

        for i in range(2, len(tokens)):
            if tokens[i] in operationArr:
                temp1 = stack.pop()
                temp2 = stack.pop()
                val = int(self.operation(temp2, temp1, tokens[i]))
                print(val)
                stack.append(val)
            else:
                stack.append(tokens[i])
        
        return stack[-1]

    def operation(self, val1, val2, opn):
        if opn == '+':
            return int(val1) + int(val2)
        elif opn == '-':
            return int(val1) - int(val2)
        elif opn == '*':
            return int(val1) * int(val2)
        elif opn == '/':
            return int(val1)/int(val2)
        