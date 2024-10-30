class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visit = [0] * (len(isConnected[0]))
        count = 0

        def dfs(node):
            visit[node] = 1
            for i in range(len(isConnected)):
                if isConnected[i][node] == 1 and isConnected[node][i] == 1:
                    if visit[i] == 0:
                        dfs(i)
            

        for node in range(len(isConnected[0])):
            if visit[node] == 0:
                count +=1
                dfs(node)
        
        return count
