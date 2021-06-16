from class_construction import Graph

def topo_sort_bfs(graph):
    #Initialization
    queue = []
    indegree = {}
    topo_sort = []

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
        for j in graph.adjList[node]:
            indegree[j]-=1
            if indegree[j]==0:
                queue.append(j)

        topo_sort.append(node)

    return topo_sort

if __name__ == "__main__":

    graph = Graph(bidir = False)

    graph.addEdge(4, 0)
    graph.addEdge(5, 0)
    graph.addEdge(4, 1)
    graph.addEdge(3, 1)
    graph.addEdge(5, 2)
    graph.addEdge(2, 3)

    print(topo_sort_bfs(graph))
