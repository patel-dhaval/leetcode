from collections import defaultdict, deque
from typing import List

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # 1. Build the adjacency list (undirected graph)
        adj = defaultdict(list)
        for u, v in dislikes:
            adj[u].append(v)
            adj[v].append(u)
            
        # Array to store colors: -1 means uncolored, 0 is Red, 1 is Blue
        colors = [-1] * (n + 1)
        
        # 2. Check every person (in case of disconnected graph)
        for i in range(1, n + 1):
            if colors[i] == -1:
                # Start a BFS from this uncolored person
                queue = deque([i])
                colors[i] = 0 # Paint them Red
                
                while queue:
                    current = queue.popleft()
                    
                    for neighbor in adj[current]:
                        # If the neighbor has the SAME color, it's impossible!
                        if colors[neighbor] == colors[current]:
                            return False
                        
                        # If the neighbor is uncolored, paint them the OPPOSITE color
                        if colors[neighbor] == -1:
                            colors[neighbor] = 1 - colors[current]
                            queue.append(neighbor)
                            
        return True