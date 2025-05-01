# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         toposort = []
#         adjList = {}
#         visit = set()
#         path_visit = set()

#         for src, dst in prerequisites:
#             if src not in adjList:
#                 adjList[src] = [dst]
#             else:
#                 adjList[src].append(dst)
#             if dst not in adjList:
#                 adjList[dst] = []
        

#         def dfs(node):
#             if node in visit:
#                 return True
            
#             if node in path_visit:
#                 return False
            
            
#             path_visit.add(node)

#             for nei in adjList[node]:
#                 if not dfs(nei):
#                     return False
            
#             toposort.append(node)
#             visit.add(node)
#             path_visit.remove(node)
            
#             return True
        
#         for node in adjList.keys():
#             if not dfs(node):
#                 return False
        
#         print(toposort)
        
#         if len(toposort) != numCourses:
#             return False
        
#         return True
            


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
