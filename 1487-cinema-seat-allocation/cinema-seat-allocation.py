class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seatmap = collections.defaultdict(set)
        for seats in reservedSeats:
            seatmap[seats[0]].add(seats[1])

        max_seating_possible = (n - len(seatmap)) * 2

        for seat in seatmap.values():
            left = not(seat & {2,3,4,5})
            mid = not(seat & {4,5,6,7})
            right = not(seat & {6,7,8,9})

            if left and right:
                max_seating_possible += 2
            elif left or right or mid:
                max_seating_possible += 1
        
        
        return max_seating_possible
