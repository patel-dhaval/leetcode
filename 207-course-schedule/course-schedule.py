class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()

        adj_map = {i: [] for i in range(numCourses)}

        for course in prerequisites:
            if course[1] in adj_map:
                adj_map[course[1]].append(course[0])
            else:
                adj_map[course[1]] = [course[0]]

        def dfs(node):

            if node in visited:
                return False
            if adj_map[node] == []:
                return True

            visited.add(node)

            for neighbor in adj_map[node]:
                if not dfs(neighbor): return False
            visited.remove(node)
            adj_map[node] = []
            return True

        
        for node in adj_map.keys():
            if not dfs(node):
                return False
        
        return True
