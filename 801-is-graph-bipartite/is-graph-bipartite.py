class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        queue = collections.deque()        
        colors = [-1] * (n)

        for idx in range(0, n):
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
