class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mp = dict()
        ls = []
        p = []
        names = []
        n = 0

        def find(x):
            if p[x] == -1:
                return x
            p[x] = find(p[x])
            return p[x]

        for acc in accounts:
            name = acc[0]
            root = -1
            for mail in acc[1:]:
                k = mp.get(mail, -1)
                if k == -1:
                    mp[mail] = n
                    ls.append(mail)
                    p.append(-1)
                    names.append(name)
                    k = n
                    n += 1
                if root > -1:
                    a = find(root)
                    b = find(k)
                    if a != b:
                        p[a] = b
                root = find(k)
        
        ans = dict()

        for i in range(n):
            k = find(i)
            if k not in ans:
                ans[k] = []
            ans[k].append(ls[i])

        # print(mp)
        # print(ls)
        # print(p)
        # print(names)

        return [[names[k]] + sorted(mails) for k, mails in ans.items()]
