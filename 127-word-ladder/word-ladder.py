"""
Begin word -> possible combination -> check dict, if present move and increase counter else backtrack

"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList = set(wordList)
        queue = collections.deque()
        visited = set([beginWord])
        possible_chars = "abcdefghijklmnopqrstuvwxyz"
        queue.append([beginWord,1])
        while queue:
            curr, steps = queue.popleft()
            if curr == endWord:
                return steps

            for idx in range(len(curr)):
                original_char = curr[idx]
                
                for c in possible_chars:
                    if c == original_char: continue
                    
                    combination = curr[:idx] + c + curr[idx+1:]
                    
                    if combination == endWord:
                        return steps + 1

                    if combination in wordList and combination not in visited:
                        visited.add(combination)
                        queue.append((combination, steps+1))
                
        return 0