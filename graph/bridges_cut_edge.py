from class_construction import Graph

def dfs(graph, source):
    time = {}
    low = {}
    bridges = []

    for i in graph.nodes:
        time[i] = False
        low[i] = False

    def search(node, prev):
        #Initialization
        global t

        #Base case
        if time[node]!=False:
            low[prev] = time[node]
            return None

        #Induction
        time[node] = t
        low[node] = t
        t += 1

        for i in graph.adjList[node]:
            if i!=prev:
                search(i, node)
                if low[i] != time[i]:
                    low[node] = low[i]
        if prev!=-1:
            if low[node] > low[prev]:
                bridges.append((prev, node))

        return None

    search(source, -1)

    return bridges

if __name__ == "__main__":
    t = 1
    graph = Graph()

    graph.addEdge(1, 2)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)
    graph.addEdge(4, 1)
    graph.addEdge(4, 5)
    graph.addEdge(5, 6)
    graph.addEdge(6, 7)
    graph.addEdge(6, 9)
    graph.addEdge(7, 8)
    graph.addEdge(9, 8)
    graph.addEdge(8, 10)
    graph.addEdge(10, 11)
    graph.addEdge(10, 12)
    graph.addEdge(11, 12)

    print(dfs(graph, 1))
