"""
sign = '*'
i = 0, 1, 2, 3, 4
char = 3, + , 1, *, 2
value = 0
stack = [3, 2]
sum(stack) = 5

ip: 3+1*2
op: 5

"""
class Solution:
    def calculate(self, s: str) -> int:
        len_input = len(s)
        stack = []
        sign = '+'
        value = 0

        for i, char in enumerate(s):

            if char.isdigit():
                value = value * 10 + int(char)
            
            if char in ('+-*/') or i == len_input - 1:
                if sign == '+':
                    stack.append(value)
                elif sign == '-':
                    stack.append(-value)
                elif sign == '*':
                    stack.append(stack.pop() * value)
                elif sign == '/':
                    stack.append(int(stack.pop() / value))
                sign = char
                value = 0
            
        return sum(stack)






            