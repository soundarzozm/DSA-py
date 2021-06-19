from class_construction import WeightedGraph
import heapq as hp

def prim(graph, node):
    key = {}
    mst = {}
    parent = {}
    for i in graph.nodes:
        key[i] = float('inf')
        mst[i] = False
        parent[i] = -1
    heap = []
    hp.heappush(heap, (0, node))

    while heap:
        dist, node = hp.heappop(heap)
        mst[node] = True
        for i in graph.adjList[node]:
            if mst[i[0]]==False:
                if key[i[0]] > i[1]:
                    key[i[0]] = i[1]
                    parent[i[0]] = node
                    hp.heappush(heap, (key[i[0]], i[0]))
    for i in parent.keys():
        parent[i] = (parent[i], key[i])

    return parent

if __name__ == "__main__":

    graph = WeightedGraph()

    graph.addEdge(0, 1, 2)
    graph.addEdge(0, 3, 6)
    graph.addEdge(1, 3, 8)
    graph.addEdge(1, 4, 5)
    graph.addEdge(1, 2, 3)
    graph.addEdge(2, 4, 7)

    print(prim(graph, 0))
