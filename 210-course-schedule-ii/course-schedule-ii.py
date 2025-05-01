class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i: [] for i in range(numCourses)}
        for src, dst in prerequisites:
            adjList[src].append(dst)

        visit = set()
        path_visit = set()
        toposort = []

        def dfs(node):
            if node in path_visit:
                return False

            if node in visit:
                return True

            path_visit.add(node)

            for neighbor in adjList[node]:
                if not dfs(neighbor):
                    return False

            path_visit.remove(node)
            visit.add(node)
            toposort.append(node)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return toposort
