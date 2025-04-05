class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) -1

        while i < j:
            sum_nos = numbers[i] + numbers[j]
            if target > sum_nos:
                i += 1
            elif target < sum_nos:
                j-=1
            else:
                return [i+1, j+1]