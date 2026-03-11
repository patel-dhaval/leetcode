class DSU:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 1
    
    def find(self, node):
        p = self.par[node]

        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        
        return p

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if self.rank[pu] > self.rank[pv]:
            self.par[pv] = pu
        elif self.rank[pv] > self.rank[pu]:
            self.par[pu] = pv
        else:
            self.par[pu] = pv
            self.rank[pv] += 1
        

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails_to_account = collections.defaultdict(str)
        
        dsu = DSU(len(accounts))

        for idx, account in enumerate(accounts):
            for email in account[1:]:
                if email in emails_to_account:
                    dsu.union(emails_to_account[email], idx)
                else:
                    emails_to_account[email] = idx
        
        res = collections.defaultdict(list)

        for email, account in emails_to_account.items():
            res[dsu.find(account)].append(email)

        
        return [[accounts[i][0]] + sorted(emails) for i, emails in res.items()]

        
