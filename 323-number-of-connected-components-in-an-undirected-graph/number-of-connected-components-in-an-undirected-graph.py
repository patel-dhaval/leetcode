class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()

        adj_list = {i: [] for i in range(n)}

        for src, dst in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)


        def dfs(node):
            if node in visited:
                return 
            
            visited.add(node)

            for neighbour in adj_list[node]:
                if neighbour not in visited:
                    dfs(neighbour)
            
            return
        
        component_count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                component_count += 1
        
        return component_count
