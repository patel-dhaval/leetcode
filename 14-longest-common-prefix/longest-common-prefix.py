"""
Approach
Split the input strings into individual strings
Use a single pointer, keep processing that till the end of the shortest str
For each common char across strings, keep tracking and add to the prefix
if mismatch found, start the tracking again and store the longest one as answer
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = []
        prefix = []
        inputs = len(strs)
        smallest_len = float(inf)
        for s in strs:
            smallest_len = min(len(s), smallest_len)
        
        for i in range(smallest_len):
            current_char = strs[0][i]
            for s in strs[1:]:
                if current_char != s[i]:
                    current_char = ""
                    prefix = []    
                                
            if current_char != "":
                prefix.append(current_char)
                if len(prefix) > len(longest_prefix):
                    longest_prefix = prefix
            else:
                break
        
        return ''.join(longest_prefix)