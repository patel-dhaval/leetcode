"""
Approach

Maintain count of the characters
Keep increasing the size of the window
Window - max_count <= k
If this fails, we know that we have to swap more than allowed (k), thus we slide the window and update the count of the element which was removed from the window
We track the max count and return once all inputs are processed

"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        if len(s) < 2:
            return len(s)
        
        l, r = 0, 0
        counts = defaultdict(int)
        maxLen = 0
        while r < len(s):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
            
            maxLen = max(maxLen, r - l + 1)
            r += 1
        return maxLen

                
