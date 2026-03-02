class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_lst = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        queue = collections.deque()
        toposort = []
        visited = set()
        for src, dst in prerequisites:
            adj_lst[src].append(dst)
            indegree[dst] += 1
        

        for idx in range(numCourses):
            if indegree[idx] == 0:
                queue.append(idx)


        while queue:
            curr = queue.popleft()
            visited.add(curr)
            for neighbour in adj_lst[curr]:
                if neighbour not in visited:
                    indegree[neighbour] -= 1
                    if indegree[neighbour] == 0:
                        queue.append(neighbour)
            toposort.append(curr)
        
        if len(toposort) != numCourses:
            return False
        
        return True