#Shortest Distance UAG
import sys
sys.path.insert(1, "L:\Data Structures and Algos\love_babbar\heap")
from class_construction import WeightedGraph
from min_heap import MinHeap

def dijkstra(source, graph):
    cnt = 1
    distance = {}
    heap = MinHeap(len(graph.nodes))
    for i in graph.nodes:
        distance[i] = float('inf')
    distance[source] = 0

    heap.insert((0, source))

    while cnt!=0:
        dist, node = heap.removeMin()
        cnt -= 1
        for i in graph.adjList[node]:
            if distance[i[0]] > dist + i[1]:
                distance[i[0]] = dist + i[1]
                heap.insert((distance[i[0]], i[0]))
                cnt += 1
    return distance

if __name__ == "__main__":

    graph = WeightedGraph()

    graph.addEdge(1, 2, 2)
    graph.addEdge(2, 5, 5)
    graph.addEdge(2, 3, 4)
    graph.addEdge(1, 4, 1)
    graph.addEdge(4, 3, 3)
    graph.addEdge(3, 5, 1)

    print(dijkstra(2, graph))
