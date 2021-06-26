class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = dict(
            name=kingName,
            children=[],
            alive=True
        )
        self.d = {kingName: self.king}


    def birth(self, parentName: str, childName: str) -> None:
        p = self.d[parentName]
        x = dict(
            name=childName,
            children=[],
            alive=True
        )
        p['children'].append(x)
        self.d[childName] = x
        
    def death(self, name: str) -> None:
        self.d[name]['alive'] = False

    def getInheritanceOrder(self) -> List[str]:
        def dfs(node):
            if node['alive']:
                yield node['name']
            for c in node['children']:
                yield from dfs(c)
        return list(dfs(self.king))



# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
