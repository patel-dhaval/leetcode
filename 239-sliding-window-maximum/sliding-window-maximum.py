"""
Approach

We are using a monotonically decreasing queue
Max Value in the queue would be at the left most position of the queue

Idea is that we insert values in the queue which are smaller than the values currently in the queue
If not, we pop all the smaller values and then only append

We remove the leftmost element from the queue once we slide the window

Once the window size is hit, append the op, slide the window.


"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # index
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output