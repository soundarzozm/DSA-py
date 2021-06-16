from class_construction import Graph
import sys

def shortestPath(graph, x):

    #Initialization
    distance = {}
    queue = []
    for i in graph.nodes:
        distance[i] = sys.maxsize

    distance[x] = 0
    queue.append(x)

    while queue:
        node = queue.pop(0)
        for i in graph.adjList[node]:
            if distance[i] > distance[node]+1:
                distance[i] = distance[node]+1
                queue.append(i)

    return distance

if __name__ == "__main__":

    graph = Graph()

    graph.addEdge(0, 1)
    graph.addEdge(1, 3)
    graph.addEdge(0, 3)
    graph.addEdge(1, 2)
    graph.addEdge(2, 6)
    graph.addEdge(3, 4)
    graph.addEdge(4, 5)
    graph.addEdge(5, 6)
    graph.addEdge(6, 7)
    graph.addEdge(7, 8)
    graph.addEdge(6, 8)

    print(shortestPath(graph, 0))
