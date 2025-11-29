class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_lst = [[] for _ in range(numCourses)]
        
        for src, dst in prerequisites:
            adj_lst[src].append(dst)
            
        print(adj_lst)
        toposort = []
        visited = set()
        path = set()
        def dfs(node):
            if node in path:
                return False

            if node in visited:
                return True
            visited.add(node)
            path.add(node)
            for neighbour in adj_lst[node]:
                if not dfs(neighbour):
                    return False

            path.remove(node)
            toposort.append(node)
            return True
        
        for n in range(0, numCourses):
            if not dfs(n):
                return False
        
        return True