"""
max_group = 0
reserved= {1: {2,3,8}, 2: {6}, 3: {1,10}}

"""
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        reserved = collections.defaultdict(set)

        for seat in reservedSeats:
            reserved[seat[0]].add(seat[1])
        
        max_groups = (n - len(reserved)) * 2

        for seats in reserved.values():
            left = not({2,3,4,5} & seats)
            mid = not({4,5,6,7} & seats)
            right = not({6,7,8,9} & seats)

            if left and right:
                max_groups += 2
            elif left or right or mid:
                max_groups += 1
        
        return max_groups