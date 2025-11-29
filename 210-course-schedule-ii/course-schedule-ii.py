class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj_lst = {i: [] for i in range(numCourses) }
        queue = collections.deque()
        toposort = []
        visited = set()
        for src, dst in prerequisites:
            adj_lst[src].append(dst)
            indegree[dst] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            visited.add(node)
            for nei in adj_lst[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
            toposort.append(node)
        
        if len(toposort) != numCourses:
            return []
        
        return toposort[::-1]
