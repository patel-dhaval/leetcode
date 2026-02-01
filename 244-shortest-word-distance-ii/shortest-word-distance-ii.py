class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsDict = wordsDict
        
    def shortest(self, word1: str, word2: str) -> int:
        self.location_array_1 = []
        self.location_array_2 = []
        self.min_len = float("inf")
        for i, word in enumerate(self.wordsDict):
            if word == word1:
                self.location_array_1.append(i)
            if word == word2:
                self.location_array_2.append(i)
        
        i = 0
        j = 0

        while i < len(self.location_array_1) and j < len(self.location_array_2):
            self.min_len = min(self.min_len, abs(self.location_array_1[i] - self.location_array_2[j]))
            if self.location_array_1[i] < self.location_array_2[j]:
                i+=1
            else:
                j+=1
        
        return self.min_len

# from collections import defaultdict

# class WordDistance:

#     def __init__(self, wordsDict: List[str]):
#         # OPTIMIZATION: Build the map ONCE here.
#         self.locations = defaultdict(list)
#         for i, word in enumerate(wordsDict):
#             self.locations[word].append(i)

#     def shortest(self, word1: str, word2: str) -> int:
#         # Retrieve pre-calculated lists
#         loc1 = self.locations[word1]
#         loc2 = self.locations[word2]
        
#         i, j = 0, 0
#         min_dist = float("inf")

#         # Two Pointer Logic
#         while i < len(loc1) and j < len(loc2):
#             val1, val2 = loc1[i], loc2[j]
            
#             min_dist = min(min_dist, abs(val1 - val2))
            
#             # LOGIC FIX: Compare the values, not the lists
#             if val1 < val2:
#                 i += 1
#             else:
#                 j += 1
        
#         return min_dist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)