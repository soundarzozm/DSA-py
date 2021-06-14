from class_construction import Graph

def bfs(graph, node):
    bfs_arr = []
    visited = {}

    for i in graph.nodes:
        visited[i]=False

    def search(node):
        queue = []
        queue.append(node)
        visited[node] = True

        while queue:
            node = queue.pop(0)
            bfs_arr.append(node)

            for i in graph.adjList[node]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    search(node)

    for i in graph.nodes:
        if visited[i]==False:
            search(i)

    return bfs_arr

if __name__=="__main__":

    graph = Graph()

    graph.addEdge(1, 2)
    graph.addEdge(7, 5)
    graph.addEdge(2, 7)
    graph.addEdge(2, 3)
    graph.addEdge(3, 5)
    graph.addEdge(4, 6)

    print(bfs(graph, 5))
