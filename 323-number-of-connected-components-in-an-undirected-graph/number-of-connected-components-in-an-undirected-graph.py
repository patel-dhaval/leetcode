class DSU:
    def __init__(self, n):
        self.par = {}
        self.rank = {}
        self.components = n
        for idx in range(n):
            self.par[idx] = idx
            self.rank[idx] = 1

    def find(self, node):
        root = self.par[node]

        while root != self.par[root]:
            self.par[root] = self.par[self.par[root]]
            root = self.par[root]

        return root

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        
        if pu == pv:
            return False

        self.components -= 1

        if self.rank[pu] > self.rank[pv]:
            self.par[pv] = pu
        elif self.rank[pu] < self.rank[pv]:
            self.par[pu] = pv
        else:
            self.par[pu] = pv
            self.rank[pv] += 1
        
        return True

    def comps(self):
        return self.components

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        for u,v in edges:
            dsu.union(u,v)

        return dsu.comps()