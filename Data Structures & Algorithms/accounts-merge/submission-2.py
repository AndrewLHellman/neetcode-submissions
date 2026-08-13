class UnionFind:
    def __init__(self, n: int):
        self.pars = list(range(n))
        self.rank = [1] * n
    
    def find(self, x: int) -> int:
        p = self.pars[x]
        while p != self.pars[p]:
            self.pars[p] = self.pars[self.pars[p]]
            p = self.pars[p]
        return p
    
    def union(self, x1: int, x2: int) -> bool:
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        
        if self.rank[p1] >= self.rank[p2]:
            self.pars[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.pars[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAccount = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAccount:
                    uf.union(emailToAccount[email], i)
                else:
                    emailToAccount[email] = i

        print(emailToAccount)
        print(uf.pars) 
        emailGroup = defaultdict(list)
        for email, i in emailToAccount.items():
            emailGroup[uf.find(i)].append(email)
        print(dict(emailGroup))
    
        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + emails)

        return res