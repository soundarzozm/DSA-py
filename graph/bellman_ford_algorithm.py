#Detect negative cycle
from class_construction import WeightedGraph

def edgesArray(graph):
    edges = []
    for i in graph.adjList:
        for j in graph.adjList[i]:
            edges.append((i, j[0], j[1]))
    return edges

def bellmanFord(graph, source):
    distance = {}
    for i in graph.nodes:
        distance[i] = float('inf')
    distance[source] = 0
    edges = edgesArray(graph)

    for _ in range(len(graph.nodes) - 1):
        for j in edges:
            if (distance[j[0]] + j[2]) < distance[j[1]]:
                distance[j[1]] = distance[j[0]] + j[2]

    for j in edges:
        if (distance[j[0]] + j[2]) < distance[j[1]]:
            return "negative cycle exists"
    return distance

if __name__ == "__main__":

    graph = WeightedGraph(bidir = False)

    graph.addEdge(3, 2, 6)
    graph.addEdge(5, 3, 1)
    graph.addEdge(0, 1, 5)
    graph.addEdge(1, 5, -3)
    graph.addEdge(1, 2, -2)
    graph.addEdge(3, 4, -2)
    graph.addEdge(2, 4, 3)

    print(bellmanFord(graph, 0))
