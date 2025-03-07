from typing import List
from collections import Counter
from math import inf

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        # Calculate the sum of all numbers in the list
        s = sum(nums)
      
        # Create a frequency counter for the numbers in the list
        count = Counter(nums)
      
        # Initialize the answer to negative infinity
        largest_outlier = -inf
      
        # Iterate over each unique number and its count in the list
        for num, freq in count.items():
            # Calculate the tentative sum removing the current number
            tentative_sum = s - num
          
            # Check if tentative_sum is odd or there is no pair that sums up to half of tentative_sum
            if tentative_sum % 2 or count[tentative_sum // 2] == 0:
                continue
          
            # Check for the condition of a valid outlier
            if num != tentative_sum // 2 or freq > 1:
                # Update the largest outlier if the current number is greater
                largest_outlier = max(largest_outlier, num)
      
        # Return the largest outlier found, default is -inf if none found
        return largest_outlier