class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        queue = collections.deque()        
        colors = [-1] * (n)

        for idx in range(0, n):
            if colors[idx] != -1:
                continue
            if colors[idx] == -1:
                queue.append(idx)
                colors[idx] = 0
            while queue:
                curr = queue.popleft()
                for neighbour in graph[curr]:
                    if colors[neighbour] == colors[curr]:
                        return False
                    if colors[neighbour] == -1:
                        colors[neighbour] = 1 - colors[curr]
                        queue.append(neighbour)
        return True


# class Solution:
#     def isBipartite(self, graph: List[List[int]]) -> bool:
#         n = len(graph)
#         colors = [-1] * n  # -1: uncolored, 0: color A, 1: color B
        
#         for i in range(n):
#             # If already colored, skip to handle disconnected components
#             if colors[i] != -1:
#                 continue
                
#             # Start BFS
#             queue = collections.deque([i])
#             colors[i] = 0
            
#             while queue:
#                 curr = queue.popleft()
#                 for neighbor in graph[curr]: # Use input graph directly
#                     if colors[neighbor] == -1:
#                         colors[neighbor] = 1 - colors[curr]
#                         queue.append(neighbor)
#                     elif colors[neighbor] == colors[curr]:
#                         return False # Found an odd cycle!
#         return True