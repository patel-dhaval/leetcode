class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        
        adj_list = [set() for _ in range(n)]
        queue = collections.deque()
        for idx, nodes in enumerate(graph):
            for node in nodes:
                adj_list[idx].add(node)


        colors = [-1] * (n)

        for idx in range(0, n):
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
