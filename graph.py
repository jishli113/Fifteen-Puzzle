# author: Joshua Li
# date: Dec 4, 2022
# file: graph.py a Python program that implements a Vertex as well as a Graph ADT
# input: none
# output: none
class Vertex:

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.getId() for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def replaceConnections(self, connections):
        self.connectedTo = connections

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.dfsret = []
        self.bfsret = []

    def addVertex(self, key):
        self.vertList[key] = Vertex(key)

    def getVertex(self, n):
        for i in self.vertList.keys():
            if self.vertList[i].getId() == n:
                return self.vertList[i]
        return None

    def __contains__(self, n):
        for i in self.vertList.keys():
            if self.vertList[i] == n:
                return True
        return False

    def addEdge(self, f, t, weight=0):
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def replaceVertices(self, newVert):
        self.vertList = newVert

    def getDict(self):
        return self.vertList

    def swapVertices(self, i, j):
        self.vertList[i], self.vertList[j] = self.vertList[j], self.vertList[i]
        c = self.vertList[j].getConnections()
        self.vertList[j].replaceConnections(self.vertList[i])
        self.vertList[i].replaceConnections(c)

    def __iter__(self):
        return iter(self.vertList.values())

    def breadth_first_search(self, root):
        q = []
        for i in self.vertList.keys():
            if self.vertList[i].getId() == root:
                q.append(self.vertList[i])
                while len(q) > 0:
                    store = q.pop(0)
                    if store.getId() not in self.bfsret:
                        self.bfsret.append(store.getId())
                    for j in store.getConnections():
                        if j.getId() not in self.bfsret:
                            q.append(j)
                break
        return self.bfsret

    def evaluateboard(self, board):
        count = 0
        for i in range(1, 17):
            if board[i - 1] == 0 or board[i - 1] == i:
                count = count + 1
        return count

    def depth_first_search(self, root):
        self.dfsret.append(root)
        for i in self.vertList.keys():
            if self.vertList[i].getId() == root:
                for j in self.vertList[i].getConnections():
                    if j.getId() not in self.dfsret:
                        self.depth_first_search(j.getId())
                break
        return self.dfsret


if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.addVertex(i)

    g.addEdge(0, 1)
    g.addEdge(0, 5)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 0)
    g.addEdge(5, 4)
    g.addEdge(5, 2)
    for v in g.getDict():
        print(v)
    assert (g.getVertex(0) in g) == True
    assert (g.getVertex(6) in g) == False

    print(g.getVertex(0))
    assert str(g.getVertex(0)) == '0 connectedTo: [1, 5]'
    print(g.getVertex(5))
    assert str(g.getVertex(5)) == '5 connectedTo: [4, 2]'
    path = g.breadth_first_search(0)
    print('BFS traversal by discovery time (preordering): ', path)
    assert path == [0, 1, 5, 2, 4, 3]

    path = g.depth_first_search(0)
    print('DFS traversal by discovery time (preordering): ', path)
    assert path == [0, 1, 2, 3, 4, 5]
