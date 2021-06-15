from class_construction import Graph

def cycle_dfs(graph):
    flag = False
    ans = False
    visited = {}
    dfs_visited = {}
    dfs_arr = []

    for i in graph.nodes:
        visited[i] = False
        dfs_visited[i] = False

    def search(node):
        ans = False
        flag = False

        #Base case
        if dfs_visited[node]!=False:
            ans = True
            return ans

        #Induction
        visited[node] = True
        dfs_visited[node] = True
        dfs_arr.append(node)
        for i in graph.adjList[node]:
            flag = search(i)
            ans = max(ans, flag)
        dfs_visited[node] = False
        return ans

    for i in graph.nodes:
        if visited[i]==False:
            flag = search(i)
            ans = max(ans, flag)

    return ans

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

    #print(graph.adjList)

    #print(cycle_bfs(graph))
    print(cycle_dfs(graph))
