class DSU:
    def __init__(self, n):
        self.rank = [1] * n
        self.par = {}

        for i in range(n):
            self.par[i] = i

    def find(self, node):
        root = node

        while root != self.par[root]:
            self.par[root] = self.par[self.par[root]]
            root = self.par[root]

        return root

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if self.rank[pu] > self.rank[pv]:
            self.par[pv] = pu
        elif self.rank[pu] < self.rank[pv]:
            self.par[pu] = pv
        else:
            self.par[pu] = pv
            self.rank[pv] += 1
        

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_owner = {}
        dsu = DSU(len(accounts))
        for idx, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_owner:
                    dsu.union(idx, email_to_owner[email])
                else:
                    email_to_owner[email] = idx
        
        collection = collections.defaultdict(list)

        for email, idx in  email_to_owner.items():
            collection[dsu.find(idx)].append(email)
        res = []
        for idx, emails in collection.items():
            name = accounts[idx][0]
            entry = [name] + sorted(emails)
            res.append(entry)

        return res