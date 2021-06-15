from class_construction import Graph

def bipartite_bfs(graph):
    bfs_arr = []
    visited = {}
    ans = True

    for i in graph.nodes:
        visited[i]=-1

    def search_component(node):
        flag = True
        queue = []
        queue.append(node)
        visited[node] = 0

        while queue:
            node = queue.pop(0)
            bfs_arr.append(node)

            for i in graph.adjList[node]:
                if visited[i] == -1:
                    queue.append(i)
                    if visited[node]==0:
                        visited[i] =1
                    else:
                        visited[i]=0
                else:
                    if visited[node]==visited[i]:
                        flag = False
        return flag

    for i in graph.nodes:
        if visited[i]==-1:
            flag = search_component(i)
            ans = min(ans, flag)

    return ans

def bipartite_dfs(graph):
    flag = True
    ans = True
    visited = {}
    dfs_arr = []

    for i in graph.nodes:
        visited[i]=-1

    def search(node, color):
        ans = True
        flag = True

        #Induction
        visited[node] = color
        dfs_arr.append(node)
        for i in graph.adjList[node]:
            if visited[i]==-1:
                if color == 1:
                    flag = search(i, 0)
                else:
                    flag = search(i, 1)
                ans = min(ans, flag)
            else:
                if visited[i]==visited[node]:
                    flag = False
                    return flag
        return ans

    for i in graph.nodes:
        if visited[i]==-1:
            flag = search(i, 0)
            ans = min(ans, flag)

    return ans

if __name__ == "__main__":

    graph = Graph()

    graph.addEdge(1, 2)
    graph.addEdge(2, 3)
    #graph.addEdge(2, 4)
    graph.addEdge(3, 4)
    graph.addEdge(4, 5)
    graph.addEdge(5, 6)
    graph.addEdge(6, 7)
    graph.addEdge(7, 2)
    graph.addEdge(5, 8)

    print(bipartite_bfs(graph))
    print(bipartite_dfs(graph))
