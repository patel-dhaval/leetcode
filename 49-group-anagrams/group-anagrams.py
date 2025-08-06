class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}

        for s in strs:
            freq_arr = [0] * 26
            for i in s:
                freq_arr[ord(i) - ord('a')] += 1
            if tuple(freq_arr) in result_dict.keys():
                result_dict[tuple(freq_arr)].append(s)
            else:
                result_dict[tuple(freq_arr)] = [s]

        return list(result_dict.values())
