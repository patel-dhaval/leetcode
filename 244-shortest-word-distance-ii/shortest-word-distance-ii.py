"""
DRY RUN:
["WordDistance", "shortest", "shortest"]
[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]

self.locations {practice: [0], makes: [1,4], coding: [3]}

loc1 = [1,4]
loc2 = [3]

i = 1
j = 1

dist1 = 4
 
dist2 = 3

ans = 1

"""
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.locations = collections.defaultdict(list)

        for idx, word in enumerate(wordsDict):
            self.locations[word].append(idx)
        

    def shortest(self, word1: str, word2: str) -> int:
        loc1 = self.locations[word1]
        loc2 = self.locations[word2]

        i, j = 0, 0
        ans = float('inf')

        while i < len(loc1) and j < len(loc2):
            dist1 = loc1[i]
            dist2 = loc2[j]

            ans = min(ans, abs(dist1 - dist2))

            if dist1 > dist2:
                j += 1
            else:
                i += 1

        return ans


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)