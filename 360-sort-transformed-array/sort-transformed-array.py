class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        n = len(nums)
        result = [0] * n
        i, j = 0, n - 1
        
        if a >= 0:
            index_ptr = n-1
        else:
            index_ptr = 0

        while i <= j:
            temp_i = a *(nums[i] * nums[i]) + b * nums[i] + c
            temp_j = a * (nums[j] * nums[j]) + b * nums[j] + c

            if a >= 0:
                temp_v = max(temp_i, temp_j)
                result[index_ptr] = temp_v
                index_ptr -= 1
                if temp_i > temp_j:
                    i += 1
                else:
                    j -=1
                
            else:
                temp_v = min(temp_i, temp_j)
                result[index_ptr] = temp_v
                index_ptr += 1
                if temp_i < temp_j:
                    i += 1
                else:
                    j -=1

        return result
                