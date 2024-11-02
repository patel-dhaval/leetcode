class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        queue = collections.deque()

        adj = [[] for i in range(numCourses)]
        for crs, pre in prerequisites:
            indegree[crs] += 1
            adj[pre].append(crs)

        
        for node in range(numCourses):
            if indegree[node] == 0:
                queue.append(node)

        output = []
        while queue:
            node = queue.popleft()
            output.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)
        if len(output) != numCourses:
            return []
        else:
            return output