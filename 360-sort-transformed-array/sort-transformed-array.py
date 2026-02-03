class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        n = len(nums)
        result = [0] * n
        i, j = 0, n - 1
        
        # Consistent logic: if a >= 0, we fill from the end.
        if a >= 0:
            index_ptr = n - 1
        else:
            index_ptr = 0

        while i <= j:
            # Calculate the transformed values
            # (In Python, this variable definition inside the loop is perfectly fine)
            val_i = a * (nums[i] * nums[i]) + b * nums[i] + c
            val_j = a * (nums[j] * nums[j]) + b * nums[j] + c

            if a >= 0:
                # Case 1: 'a' is positive (or 0). The largest values are at the ends.
                # We want the MAX to go at the end of our result array.
                if val_i >= val_j:
                    result[index_ptr] = val_i
                    i += 1
                else:
                    result[index_ptr] = val_j
                    j -= 1
                index_ptr -= 1
                
            else:
                # Case 2: 'a' is negative. The smallest values are at the ends.
                # We want the MIN to go at the start of our result array.
                if val_i < val_j:
                    result[index_ptr] = val_i
                    i += 1
                else:
                    result[index_ptr] = val_j
                    j -= 1
                index_ptr += 1

        return result