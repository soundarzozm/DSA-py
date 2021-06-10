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

    def bfs(self, node):
        bfs_arr = []
        visited = {}

        for i in self.nodes:
            visited[i]=False

        queue = []

        queue.append(node)
        visited[node] = True

        while queue:

            node = queue.pop(0)
            bfs_arr.append(node)

            for i in self.adjList[node]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return bfs_arr

if __name__=="__main__":

    graph = Graph()

    graph.addEdge(1, 2)
    graph.addEdge(7, 5)
    graph.addEdge(2, 7)
    graph.addEdge(2, 3)
    graph.addEdge(3, 5)
    graph.addEdge(4, 6)

    print(graph.bfs(1))
