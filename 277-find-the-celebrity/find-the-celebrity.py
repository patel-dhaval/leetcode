# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for idx in range(1, n):
            if knows(candidate, idx):
                candidate = idx

        for idx in range(n):
            if idx == candidate:
                continue
            if knows(candidate, idx) or not knows(idx, candidate):
                return -1
        
        return candidate