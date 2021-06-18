from class_construction import WeightedGraph
import heapq

def prim(graph, node):
    key = {}
    mst = {}
    parent = {}
    for i in graph.nodes:
        key[i] = float('inf')
        mst[i] = False
        parent[i] = -1
    key[node] = 0

if __name__ == "__main__":

    graph = WeightedGraph()

    graph.addEdge(0, 1, 2)
    graph.addEdge(0, 3, 6)
    graph.addEdge(1, 3, 8)
    graph.addEdge(1, 4, 5)
    graph.addEdge(1, 2, 3)
    graph.addEdge(2, 4, 7)

    print(graph.adjList)
