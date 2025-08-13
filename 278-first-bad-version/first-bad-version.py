# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:        
        """
        Uses binary search to find the first bad version.
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        left, right = 1, n

        while left < right:
            mid = left + (right - left) // 2  # Prevents overflow in some languages
            if isBadVersion(mid):
                right = mid  # First bad version is at or before mid
            else:
                left = mid + 1  # First bad version is after mid

        return left