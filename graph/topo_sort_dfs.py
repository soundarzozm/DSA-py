from class_construction import Graph

def topo_sort_dfs(graph):
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
            search(i)
        stack.append(node)
        return None

    for i in graph.nodes:
        if visited[i]==False:
            search(i)

    return stack[::-1]

if __name__ == "__main__":

    graph = Graph(bidir = False)

    graph.addEdge(4, 0)
    graph.addEdge(5, 0)
    graph.addEdge(4, 1)
    graph.addEdge(3, 1)
    graph.addEdge(5, 2)
    graph.addEdge(2, 3)

    print(topo_sort_dfs(graph))
