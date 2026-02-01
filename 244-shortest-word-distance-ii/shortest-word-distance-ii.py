from collections import defaultdict

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.locations = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.locations[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        loc1 = self.locations[word1]
        loc2 = self.locations[word2]
        
        i, j = 0, 0
        min_dist = float("inf")

        while i < len(loc1) and j < len(loc2):
            val1, val2 = loc1[i], loc2[j]
            
            min_dist = min(min_dist, abs(val1 - val2))
            
            if val1 < val2:
                i += 1
            else:
                j += 1
        
        return min_dist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)