class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n+1)]

        for src, dst in dislikes:
            graph[src].append(dst)
            graph[dst].append(src)

        colors = [-1] * (n + 1)
        queue = collections.deque()

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

        