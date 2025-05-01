from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}
        for src, dst in prerequisites:
            adjList[src].append(dst)

        visit = set()
        path_visit = set()

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
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
