from random import randint


def peso_total(G):
    peso_total = 0
    for i in G:
        peso_total += i[1]
    return peso_total


def prim(V, adjMatrix):
    vertex_inic = vertex = randint(0, V-1)
    MST = []
    edges = []
    visited = set()
    minEdge = [set(), float('inf')]

    while(len(MST) < V-1):
        visited.add(vertex)

        for r in range(V):
            if adjMatrix[vertex][r] != 0:
                edges.append([{vertex, r}, adjMatrix[vertex][r]])

        for e in range(len(edges)):
            if edges[e][1] < minEdge[1] and not edges[e][0].issubset(visited):
                minEdge = edges[e]

        edges.pop(edges.index(minEdge))
        MST.append(minEdge)
        aux_set = minEdge[0].copy()
        aux_set.remove(aux_set.intersection(visited).pop())

        #vertex from minEdge that is not in visited
        vertex = aux_set.pop()
        minEdge = [set(), float('inf')]

    return MST, vertex_inic