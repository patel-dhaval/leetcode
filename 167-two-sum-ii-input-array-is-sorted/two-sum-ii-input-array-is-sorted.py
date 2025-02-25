class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers)-1

        while L < R:
            curr_sum = numbers[L] + numbers[R]
            if curr_sum > target:
                R -= 1
            elif curr_sum < target:
                L +=1
            else:
                return [L+1, R+1]
        