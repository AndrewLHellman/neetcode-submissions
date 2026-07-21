class Graph:
    
    def __init__(self):
        self.adj_list = {}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj_list:
            self.adj_list[src] = set()
        if dst not in self.adj_list:
            self.adj_list[dst] = set()
        self.adj_list[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list:
            return False
        if dst not in self.adj_list[src]:
            return False
        self.adj_list[src].remove(dst)
        return True
        

    def hasPath(self, src: int, dst: int, visit = None) -> bool:
        if visit == None:
            visit = set()

        if src == dst:
            return True
        if src in visit:
            return False
        
        visit.add(src)
        for node in self.adj_list[src]:
            if self.hasPath(node, dst, visit):
                return True
        return False
