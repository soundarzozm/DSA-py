class Graph:

    def __init__(self, bidir=True):
        self.nodes = []
        self.adjList = {}
        self.bidir = bidir

    def createNode(self, node):
        if node not in self.adjList.keys():
            self.nodes.append(node)
            self.adjList[node] = []

    def printAdjList(self):
        for node in self.nodes:
            print(node, "->", self.adjList[node])

    def addEdge(self, u, v):
        self.createNode(u)
        self.createNode(v)

        self.adjList[u].append(v)

        if self.bidir == True:
            self.adjList[v].append(u)

    def degree(self, node):
        return len(self.adjList[node])

if __name__=="__main__":

    graph = Graph()

    graph.addEdge("Chennai", "Bangalore")
    graph.printAdjList()

