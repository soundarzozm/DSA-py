from class_construction import WeightedGraph

def topo_sort_dfs_weighted(graph):
    stack = []
    dfs_arr = []
    visited = {}

    for i in graph.nodes:
        visited[i] = False

    def search(node):
        #Base case
        if visited[node]!=False:
            return None

        #Induction
        visited[node] = True
        dfs_arr.append(node)
        for i in graph.adjList[node]:
            search(i[0])
        stack.append(node)
        return None

    for i in graph.nodes:
        if visited[i]==False:
            search(i)

    return stack[::-1]

if __name__ == "__main__":

    graph = WeightedGraph(bidir = False)

    graph.addEdge(0, 1, 2)
    graph.addEdge(1, 2, 3)
    graph.addEdge(2, 3, 6)
    graph.addEdge(0, 4, 1)
    graph.addEdge(4, 2, 2)
    graph.addEdge(4, 5, 4)
    graph.addEdge(5, 3, 1)

    print(graph.adjList)
    print(topo_sort_dfs_weighted(graph))
