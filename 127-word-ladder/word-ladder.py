class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # CRITICAL FIX 1: Convert to Set for O(1) lookups
        wordSet = set(wordList)
        
        if endWord not in wordSet:
            return 0
        
        queue = collections.deque([(beginWord, 1)])
        visited = set([beginWord])
        
        possible_chars = "abcdefghijklmnopqrstuvwxyz"
        
        while queue:
            curr, steps = queue.popleft()
            
            if curr == endWord:
                return steps
            
            for i in range(len(curr)):
                original_char = curr[i]
                
                for char in possible_chars:
                    if char == original_char: continue
                    
                    new_word = curr[:i] + char + curr[i+1:]

                    if new_word == endWord:
                        return steps + 1
                    
                    if new_word in wordSet and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, steps + 1))
                        
        return 0