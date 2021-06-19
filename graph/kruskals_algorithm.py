from disjoint_set import parent, rank, findParent, union

def makeSet(n):
    global parent
    global rank
    for i in range(n):
        parent.append(i)
        rank.append(0)
    return None

if __name__ == "__main__":
    edges = []
    cost = 0
    makeSet(7)
    mst = []

    edges.append((9, 5, 4))
    edges.append((4, 5, 1))
    edges.append((1, 1, 4))
    edges.append((5, 3, 4))
    edges.append((2, 1, 2))
    edges.append((3, 2, 4))
    edges.append((3, 2, 3))
    edges.append((8, 6, 3))
    edges.append((7, 6, 2))

    edges.sort()

    for i in edges:
        dist = i[0]
        node1 = i[1]
        node2 = i[2]

        if findParent(node1) != findParent(node2):
            cost += dist
            union(node1, node2)
            mst.append(i)

    print(mst)
    print(cost)
