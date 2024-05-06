class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict()
        freq_arr = [0] * 26
        soln = []

        for s in strs:
            temp_arr = [0] * 26
            for i in range(0, len(s)):
                temp_arr[ord(s[i]) - ord('a')] += 1
            if tuple(temp_arr) in hmap.keys():
                temp_val = hmap[tuple(temp_arr)]
                temp_val.append(s)
                hmap[tuple(temp_arr)] = temp_val
            else:
                hmap[tuple(temp_arr)] = [s]
        
        for v in hmap.values():
            soln.append(v)
        
        return soln        

            
