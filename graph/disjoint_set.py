parent = []
rank = []

def makeSet(n):
    global parent
    global rank
    for i in range(n):
        parent.append(i)
        rank.append(0)
    return None

def findParent(node):

    #Base case
    if parent[node] == node:
        return node

    #Induction
    return findParent(parent[node])

def union(node1, node2):

    node1 = findParent(node1)
    node2 = findParent(node2)

    if rank[node1] > rank[node2]:
        parent[node1] = node2
    elif rank[node1] <= rank[node2]:
        parent[node2] = node1

    return None

if __name__ == "__main__":
    makeSet(10)
    union(1, 2)
    union(2, 3)
    print(parent)
