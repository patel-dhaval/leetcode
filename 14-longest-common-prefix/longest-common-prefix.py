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
        
        for i in range(len(strs[0])):
            current_char = strs[0][i]
            for s in strs[1:]:
                if i == len(s) or current_char != s[i]:
                    return ''.join(longest_prefix)    

            prefix.append(current_char)
            if len(prefix) > len(longest_prefix):
                longest_prefix = prefix
        
        return ''.join(longest_prefix)