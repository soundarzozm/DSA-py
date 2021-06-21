from topo_sort_dfs import topo_sort_dfs
from class_construction import Graph

def dfs_single_directed(graph, node):
    dfs_arr = []

    def search(node):
        global visited

        #Base
        if visited[node]==True:
            return None

        #Induction
        dfs_arr.append(node)
        visited[node] = True
        for i in graph.adjList[node]:
            search(i)
        return None
    search(node)
    return dfs_arr

def kosaraju(graph):
    scc = []
    topo_stack = topo_sort_dfs(graph)
    transposed_graph = transpose(graph)
    for i in topo_stack:
        bruh = dfs_single_directed(transposed_graph, i)
        if bruh:
            scc.append(bruh)
    return scc

def transpose(graph):
    transpose = Graph(bidir = False)
    for i in graph.adjList:
        for j in graph.adjList[i]:
            transpose.addEdge(j, i)
    return transpose

if __name__ == "__main__":

    visited = {}

    graph = Graph(bidir = False)

    graph.addEdge(1, 2)
    graph.addEdge(2, 3)
    graph.addEdge(3, 1)
    graph.addEdge(2, 4)
    graph.addEdge(4, 5)

    for i in graph.nodes:
        visited[i]=False

    print(kosaraju(graph))
