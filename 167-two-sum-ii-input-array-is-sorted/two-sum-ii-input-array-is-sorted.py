class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0, len(numbers)-1

        op = []
        sum = 0
    
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum > target:
                j-=1
            elif sum < target:
                i+=1
            else:
                op.append(i+1)
                op.append(j+1)
                return op