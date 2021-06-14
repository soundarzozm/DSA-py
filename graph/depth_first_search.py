from class_construction import Graph

def dfs(graph, node):

    visited = {}
    dfs_arr = []

    for i in graph.nodes:
        visited[i]=False

    def search(node):
        #Base case
        if visited[node]!=False:
            return None

        #Induction
        visited[node] = True
        dfs_arr.append(node)
        for i in graph.adjList[node]:
            search(i)
            
        return None

    search(node)

    return dfs_arr

if __name__=="__main__":

    graph = Graph()

    graph.addEdge(1, 2)
    graph.addEdge(2, 4)
    graph.addEdge(4, 6)
    graph.addEdge(6, 7)
    graph.addEdge(7, 2)
    graph.addEdge(3, 5)

    print(dfs(graph, 1))
