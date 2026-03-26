class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.locations = collections.defaultdict(list)
        
        for idx, word in enumerate(wordsDict):
            self.locations[word].append(idx)


    def shortest(self, word1: str, word2: str) -> int:
        min_dist = float('inf')
        loc1 = self.locations[word1]
        loc2 = self.locations[word2]

        i, j = 0, 0 

        while i < len(loc1) and j < len(loc2):
            l1 = loc1[i]
            l2 = loc2[j]

            min_dist = min(min_dist, abs(l1-l2))

            if l1 > l2:
                j += 1
            else:
                i += 1
        
        return min_dist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)