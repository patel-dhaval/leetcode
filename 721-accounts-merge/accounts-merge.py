import collections
from typing import List

class DSU:
    def __init__(self, n: int):
        # Using lists is faster than dictionaries for 0 to n-1 indices
        self.par = list(range(n)) 
        self.rank = [1] * n
    
    def find(self, node: int) -> int:
        # Standard iterative path compression
        root = node
        while root != self.par[root]:
            # Path halving: point to grandparent
            self.par[root] = self.par[self.par[root]] 
            root = self.par[root]
        return root

    def union(self, u: int, v: int):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return 

        if self.rank[pu] > self.rank[pv]:
            self.par[pv] = pu
        elif self.rank[pv] > self.rank[pu]:
            self.par[pu] = pv
        else:
            self.par[pu] = pv
            self.rank[pv] += 1
        

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU(len(accounts))
        email_to_account_idx = {} 

        # 1. Map emails to account indices and union overlapping ones
        for idx, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account_idx:
                    dsu.union(email_to_account_idx[email], idx)
                else:
                    email_to_account_idx[email] = idx
        
        # 2. Group emails by their root account index
        components = collections.defaultdict(list)
        for email, account_idx in email_to_account_idx.items():
            root_idx = dsu.find(account_idx)
            components[root_idx].append(email)

        # 3. Format the result
        return [
            [accounts[root_idx][0]] + sorted(emails) 
            for root_idx, emails in components.items()
        ]