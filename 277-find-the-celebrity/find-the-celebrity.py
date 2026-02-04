# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for idx in range(1, n):
            if knows(candidate, idx):
                candidate = idx

        potential_celebrity = candidate
        for idx in range(n):
            if idx == potential_celebrity:
                continue
            if knows(potential_celebrity, idx) or not knows(idx, potential_celebrity):
                return -1
        
        return potential_celebrity