class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        target_vals = {}
        res = []
        for ip in strs:
            freq_arr = [0] * 26
            for c in ip:
                freq_arr[ord(c)-ord('a')] += 1
            
            if tuple(freq_arr) in target_vals.keys():
                target_vals[tuple(freq_arr)].append(ip)
            else:
                target_vals[tuple(freq_arr)] = [ip]
        
        # for v in target_vals.values():
        #     res.append(v)

        # return res
        return list(target_vals.values())