from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # 1. Map row -> set of reserved columns
        # We only store rows that have reservations.
        reserved = defaultdict(set)
        for r, c in reservedSeats:
            if c in {2,3,4,5,6,7,8,9}: # Optimization: Ignore 1 and 10 (irrelevant)
                reserved[r].add(c)
        
        # 2. Count perfectly empty rows
        # These rows can hold 2 families each.
        count = (n - len(reserved)) * 2
        
        # 3. Process each dirty row
        for r in reserved:
            seats = reserved[r]
            
            # Check the 3 slots
            left_open = not (seats & {2,3,4,5})
            right_open = not (seats & {6,7,8,9})
            mid_open = not (seats & {4,5,6,7})
            
            if left_open and right_open:
                count += 2
            elif left_open or right_open or mid_open:
                count += 1
            # else: count += 0 (can't fit anyone)
            
        return count