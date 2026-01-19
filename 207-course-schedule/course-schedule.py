class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {}

        for src, dst in prerequisites:
            if src in adj_list:
                adj_list[src].append(dst)
            else:
                adj_list[src] = [dst]
            if dst not in adj_list:
                adj_list[dst] = []
        
        path = set()
        visited = set()

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

            return True

        for i in adj_list.keys():
            if not dfs(i):
                return False

        return True
