class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        word = []
        for char in s:
            if char == ' ':
                if word:
                    stack.append("".join(word))
                    word = []
            else:
                word.append(char)
        if word:
            stack.append(''.join(word))

        return " ".join(stack[::-1])

