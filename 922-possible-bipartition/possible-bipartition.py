class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(n+1)]
        queue = collections.deque()

        for src, dst in dislikes:
            adj_list[src].append(dst)
            adj_list[dst].append(src)

        colors = [-1] * (n+1)

        for idx in range(1, n+1):
            if colors[idx] == -1:
                queue.append(idx)
                colors[idx] = 0
            while queue:
                curr = queue.popleft()
                for neighbour in adj_list[curr]:
                    if colors[neighbour] == colors[curr]:
                        return False
                    if colors[neighbour] == -1:
                        colors[neighbour] = 1 - colors[curr]
                        queue.append(neighbour)
        
        
        return True