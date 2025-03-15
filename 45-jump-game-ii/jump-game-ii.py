"""
Idea is to look at the number of jumps it takes from 0, the window for every jump would be between the lowest and the largest value of the distance that jump can take. If in that, if we track the largest jump, then that jump count is the res.

ip: 2,3,1,1,4

ip: 2, 3
l: 0, 1, 3
r: 0, 2, 4
farthest: 2, 4
count: 1, 2

ip: 1,2,1,1,1

ip: 1, 2, 1, 1
l: 0, 1, 2, 3, 4
r: 0, 1, 3, 3, 4
farthest: 1, 3, 3, 4
count: 1, 2, 3, 4


"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        farthest = 0
        count = 0

        while r < len(nums)-1:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            count +=1
        
        return count
