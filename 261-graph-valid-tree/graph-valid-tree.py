class DSU:
    def __init__(self, n):
        self.par = [[] for _ in range(n)]
        self.rank = [[] for _ in range(n)]
        self.components = n
        for idx in range(n):
            self.par[idx] = idx
            self.rank[idx] = 1

    def find(self, node):
        p = self.par[node]

        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        
        return p

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False

        self.components -= 1
     
        if self.rank[pu] > self.rank[pv]:
            self.par[pv] = pu
        elif  self.rank[pu] < self.rank[pv]:
            self.par[pu] = pv
        else:
            self.par[pv] = pu
            self.rank[pu] += 1
        
        return True
    
    def comps(self):
        return self.components

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        dsu = DSU(n)

        for u, v in edges:
            if not dsu.union(u,v):
                return False
        
        return dsu.comps() == 1