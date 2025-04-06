class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        m = max(people)
        counts = [0] * (m+1)

        # Count the quantity of each val in arr
        for p in people:
            counts[p] += 1
        
        #print(counts)
        # Fill each bucket in the original array
        idx, i = 0, 1
        while idx < len(people):
            while counts[i] == 0:
                i += 1
            people[idx] = i
            counts[i] -= 1
            idx += 1

        # i = 0
        # for idx in range(len(people)):
        #     for _ in range(counts[idx]):
        #         people[i] = idx
        #         i+=1

        l, r = 0, len(people)-1

        res, l, r = 0, 0, len(people) - 1
        while l <= r:
            remain = limit - people[r]
            r -= 1
            res += 1
            if l <= r and remain >= people[l]:
                l += 1
        return res
                