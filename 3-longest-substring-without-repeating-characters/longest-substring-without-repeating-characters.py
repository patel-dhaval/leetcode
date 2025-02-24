'''
Approach
maintain a set for the unique characters
2 pointers, left and right, increase the size of the window if the new char is not part of the set
if the new char is part of the set, reduce the len of the window till the set no longer contain the char
add the new char and maintain the len of the subarry
return the max len of the subarray without duplicate characters

Edge Case:

if len(s) == 0:
    return 0

if len(s) == 1:
    return 1 


L, R = 0,1
maxLen = 1
charSet = set()
while R < len(s):
    if s[R] not in charSet:
        charSet.add(S[R])
        currLen = R - L + 1
        if currLen > maxLen:
            maxLen = currLen
    else:
        while s[R] not in charSet:
            charSet.remove(s[L])
            L += 1
        
    R +=1

return maxLen

Algo:


'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1 

        L, R = 0, 0
        max_len = 0
        char_set = set()

        while R < len(s):
            if s[R] not in char_set:
                char_set.add(s[R])
                max_len = max(max_len, R - L + 1)
                R += 1
            else:
                char_set.remove(s[L])
                L += 1

        return max_len