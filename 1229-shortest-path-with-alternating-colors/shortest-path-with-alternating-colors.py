class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # Helper function to build adjacency list
        def adjList(edges, n):
            graph = [[] for _ in range(n)]
            for u, v in edges:
                graph[u].append(v)
            return graph
        
        # Build adjacency lists for red and blue edges
        redList = adjList(redEdges, n)
        blueList = adjList(blueEdges, n)
        
        # Result array to store the shortest path to each node
        result = [-1] * n
        
        # BFS Queue - stores (node, color) where color is 0 for blue and 1 for red
        q = deque()
        q.append((0, -1))  # Start from node 0 with no color
        
        # Visited sets for red and blue edges
        visited = [[False, False] for _ in range(n)]  # [visited_with_red, visited_with_blue]
        visited[0] = [True, True]  # Node 0 is visited with both colors at start
        
        # Distance counter
        pathLength = 0
        
        # BFS traversal
        while q:
            for _ in range(len(q)):
                node, color = q.popleft()
                
                # Set result for this node if it hasn't been visited yet
                if result[node] == -1:
                    result[node] = pathLength
                
                # If the previous edge was red (-1 or 1), we can go to blue edges
                if color != 0:
                    for neighbor in blueList[node]:
                        if not visited[neighbor][0]:  # Not visited via blue edge
                            q.append((neighbor, 0))
                            visited[neighbor][0] = True  # Mark visited via blue edge
                
                # If the previous edge was blue (-1 or 0), we can go to red edges
                if color != 1:
                    for neighbor in redList[node]:
                        if not visited[neighbor][1]:  # Not visited via red edge
                            q.append((neighbor, 1))
                            visited[neighbor][1] = True  # Mark visited via red edge
            
            # Increment path length after each level of BFS
            pathLength += 1
        
        return result
