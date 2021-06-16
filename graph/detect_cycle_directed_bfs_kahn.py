from class_construction import Graph

def cycle_bfs(graph):
    #Initialization
    queue = []
    indegree = {}
    topo_sort = []
    counter = 0

    #Create InDegree
    for i in graph.nodes:
        indegree[i] = 0

    for i in graph.nodes:
        for j in graph.adjList[i]:
            indegree[j]+=1

    #Initialize Queue
    for i in indegree.keys():
        if indegree[i] == 0:
            queue.append(i)

    #Loop
    while queue:
        node = queue.pop(0)
        counter+=1
        for j in graph.adjList[node]:
            indegree[j]-=1
            if indegree[j]==0:
                queue.append(j)

        topo_sort.append(node)

    return counter!=len(graph.nodes)

if __name__ == "__main__":

    graph = Graph(bidir = False)

    graph.addEdge(1, 2)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)
    graph.addEdge(4, 5)
    graph.addEdge(3, 6)
    graph.addEdge(6, 5)
    graph.addEdge(7, 2)
    graph.addEdge(7, 8)
    graph.addEdge(8, 9)
    graph.addEdge(9, 7)

    print(cycle_bfs(graph))
