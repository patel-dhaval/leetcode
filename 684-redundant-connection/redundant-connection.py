class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj_lst = [[] for _ in range(n + 1)]
            
        
        def dfs(node, parent):
            if node in visited:
                return True
            visited.add(node)
            for neighbour in adj_lst[node]:
                if parent == neighbour:
                    continue
                if dfs(neighbour, node):
                    return True
            return False
        
        for src, dst in edges:
            adj_lst[src].append(dst)
            adj_lst[dst].append(src)
            visited = set()
            if dfs(src, -1):
                return [src, dst]

        return []