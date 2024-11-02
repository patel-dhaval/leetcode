class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        queue = collections.deque()
        
        adj = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)
        
        for node in range(numCourses):
            if indegree[node] == 0:
                queue.append(node)

        print(adj)

        finish, output = 0, []
        while queue:
            curr = queue.popleft()
            output.append(curr)
            finish += 1

            for nei in adj[curr]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)

        if finish != numCourses:
            return []
        else:
            return output[:: -1]