class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = defaultdict(set)

        for r, c in reservedSeats:
            if int(c) in {2,3,4,5,6,7,8,9}:
                reserved[r].add(c)
            
        count = (n - len(reserved)) * 2

        for r in reserved:
            seats = reserved[r]

            left_open = not (seats & {2,3,4,5})
            mid_open = not (seats & {4,5,6,7})
            right_open = not (seats & {6,7,8,9})

            if left_open and right_open:
                count +=2
            elif left_open or right_open or mid_open:
                count += 1

        
        return count