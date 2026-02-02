class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(numCourses)}
        visited = set()
        for src, dst in prerequisites:
            adj_list[src].append(dst)

        path = set()

        def dfs(node):
            if node in path:
                return True
            
            if node in visited:
                return False

            path.add(node)
        
            for neighbour in adj_list[node]:
                if dfs(neighbour):
                    return True
                
            path.remove(node)
            
            visited.add(node)

            return False

        for i in range(numCourses):
            if dfs(i):
                return False

        return True


