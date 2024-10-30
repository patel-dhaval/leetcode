class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # visit = [0] * (len(isConnected[0]))
        # count = 0

        # def dfs(node):
        #     visit[node] = 1
        #     for i in range(len(isConnected)):
        #         if isConnected[i][node] == 1:
        #             if visit[i] == 0:
        #                 dfs(i)
            

        # for node in range(len(isConnected)):
        #     if visit[node] == 0:
        #         count +=1
        #         dfs(node)
        
        # return count

        def dfs(i):
            visited[i] = True
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and not visited[j]:
                    dfs(j)

        provinces = 0
        visited = [False] * len(isConnected)

        for i in range(len(isConnected)):
            if not visited[i]:
                provinces += 1
                dfs(i)

        return provinces
