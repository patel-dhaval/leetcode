class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        toposort = []
        visited = set()
        path = set()


        adj_list = [[] for _ in range(numCourses)]

        for src, dst in prerequisites:
            adj_list[src].append(dst)

        
        def dfs(node):
            if node in path:
                return False
            
            if node in visited:
                return True
            
            path.add(node)

            for neighbour in adj_list[node]:
                if not dfs(neighbour):
                    return False
            
            path.remove(node)
            visited.add(node)
            toposort.append(node)
        
            return True
        
        for course in range(numCourses):
            if course not in visited:
                if not dfs(course):
                    return []
        
        return toposort