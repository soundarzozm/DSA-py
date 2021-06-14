from class_construction import Graph

def cycle_bfs(graph):
    bfs_arr = []
    visited = {}
    ans = False

    for i in graph.nodes:
        visited[i]=False

    def search_component(node, prev):
        flag = False
        queue = []
        queue.append((node, prev))
        visited[node] = True

        while queue:
            node, prev = queue.pop(0)
            bfs_arr.append(node)

            for i in graph.adjList[node]:
                if visited[i] == False:
                    queue.append((i, node))
                    visited[i] = True
                else:
                    if i!=prev:
                        flag = True
        return flag

    for i in graph.nodes:
        if visited[i]==False:
            flag = search_component(i, -1)
            ans = max(ans, flag)

    return ans

def cycle_dfs(graph):
    flag = False
    ans = False
    visited = {}
    dfs_arr = []

    for i in graph.nodes:
        visited[i]=False

    def search(node, prev):
        ans = False
        flag = False

        #Base case
        if visited[node]!=False:
            ans = True
            return ans

        #Induction
        visited[node] = True
        dfs_arr.append(node)
        for i in graph.adjList[node]:
            if i!=prev:
                flag = search(i, node)
                ans = max(ans, flag)
        return ans

    for i in graph.nodes:
        if visited[i]==False:
            flag = search(i, -1)
            ans = max(ans, flag)

    return ans

if __name__ == "__main__":

    graph = Graph()

    graph.addEdge(1, 2)
    graph.addEdge(2, 4)
    graph.addEdge(3, 5)
    graph.addEdge(5, 6)
    graph.addEdge(6, 7)
    graph.addEdge(7, 8)
    graph.addEdge(8, 9)
    graph.addEdge(9, 10)
    graph.addEdge(10, 5)
    graph.addEdge(8, 11)

    print(cycle_bfs(graph))
    print(cycle_dfs(graph))
