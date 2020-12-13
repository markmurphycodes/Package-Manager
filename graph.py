# Mark Murphy, 001223523


class Vertex:
    def __init__(self, label):
        self.label = label
        self.distance = float("inf")
        self.predVertex = Vertex


# The Graph class is the main data structure used in this program. The object tracks which nodes
# are adjacent to each other, their respective weights and indexes.
class Graph:
    def __init__(self):
        self.edgeWeights = {}
        self.adjacent = {}
        self.indexes = {}
        self.size = 0

    def addVertex(self, new):
        self.adjacent[new] = []
        self.indexes[self.size] = new
        self.size += 1

    def addEdge(self, v1, v2, weight=1.0):
        self.edgeWeights[(v1, v2)] = weight
        self.edgeWeights[(v2, v1)] = weight
        self.adjacent[v1].append(v2)
        self.adjacent[v2].append(v1)

    # Returns a distance matrix for the current nodes in the graph
    def getDistanceMatrix(self):
        distanceMatrix = [[] for n in range(0, self.size)]
        count = 0

        for i in self.adjacent:
            for j in self.adjacent:
                try:
                    distanceMatrix[count].append(self.edgeWeights[(i, j)])
                except KeyError:
                    distanceMatrix[count].append(0)
            count += 1

        return distanceMatrix

    # Returns a distance matrix only for the list of nodes provided as an arg
    def getModifiedDistanceMatrix(self, nodes):
        distanceMatrix = [[] for n in range(0, len(nodes))]
        count = 0

        for i in self.adjacent:
            if i in nodes:
                for j in self.adjacent:
                    try:
                        if j in nodes:
                            distanceMatrix[count].append(self.edgeWeights[(i, j)])
                    except KeyError:
                        distanceMatrix[count].append(0)
                count += 1

        return distanceMatrix


# This is the core algorithm which determines a eulerian circuit by which packages are delivered
# Portions of this code are adapted from Andrew Zhuravchak https://github.com/Retsediv/ChristofidesAlgorithm
# O(n^2 + log(n))
def tsp(fullGraph, subGraph):

    # build a graph
    if len(subGraph) < 2:
        return 0, subGraph
    elif len(subGraph) == 2:
        return fullGraph.edgeWeights[(fullGraph.indexes[subGraph[0]], fullGraph.indexes[subGraph[1]])], subGraph

    G = build_graph(fullGraph, subGraph)

    # build a minimum spanning tree
    MSTree = minimum_spanning_tree(G)

    # find odd vertexes
    odd_vertexes = find_odd_vertexes(MSTree)

    # add minimum weight matching edges to MST
    minimum_weight_matching(MSTree, G, odd_vertexes)

    # Find a eulerian tour. This block of code calculates the length it would take to visit all
    # the points on the tour
    eulerian_tour = find_eulerian_tour(MSTree, G)

    current = eulerian_tour[0]
    path = [current]
    visited = [False] * len(eulerian_tour)
    visited[0] = True

    length = 0

    for v in eulerian_tour[1:]:
        if not visited[eulerian_tour.index(v)]:
            path.append(v)
            visited[eulerian_tour.index(v)] = True
            length += G[current][v]

            current = v

    return length, path


# The graph is made using the nodes included in the list sub. To calculate using the full graph,
# use a list of all nodes in the graph.
# O(n^2)
def build_graph(g, sub):
    graph = {}

    for v in range(g.size):
        if v in sub:
            for u in range(g.size):
                if v != u and u in sub:
                    if v not in graph:
                        graph[v] = {}
                    graph[v][u] = g.edgeWeights[(g.indexes[u], g.indexes[v])]

    return graph


# Finds subtrees of the graph which form a cycle
# O(log*n)
class UnionFind:
    def __init__(self):
        self.weights = {}
        self.parents = {}

    def __getitem__(self, object):
        if object not in self.parents:
            self.parents[object] = object
            self.weights[object] = 1
            return object

        # find path of objects leading to the root
        path = [object]
        root = self.parents[object]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        # compress the path and return
        for ancestor in path:
            self.parents[ancestor] = root
        return root

    @property
    def __iter__(self):
        return iter(self.parents)

    def union(self, *objects):
        roots = [self[x] for x in objects]
        heaviest = max([(self.weights[r], r) for r in roots])[1]
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest


# All subtrees are analyzed and any containing cycles are ommitted
# O(n)
def minimum_spanning_tree(graph):
    tree = []
    subtrees = UnionFind()

    # If any subtree is cyclical, it is omitted. However, if it is not, it is joined with
    for W, u, v in sorted((graph[u][v], u, v) for u in graph for v in graph[u]):
        if subtrees[u] != subtrees[v]:
            tree.append((u, v, W))
            subtrees.union(u, v)

    return tree


# Find the vertexes which have an odd number of edges
# O(n)
def find_odd_vertexes(MST):
    tmp_g = {}
    vertexes = []
    for edge in MST:
        if edge[0] not in tmp_g:
            tmp_g[edge[0]] = 0

        if edge[1] not in tmp_g:
            tmp_g[edge[1]] = 0

        tmp_g[edge[0]] += 1
        tmp_g[edge[1]] += 1

    for vertex in tmp_g:
        if tmp_g[vertex] % 2 == 1:
            vertexes.append(vertex)

    return vertexes


# Find the smallest weighted minimum matching set
# O(n)
def minimum_weight_matching(MST, G, odd_vert):
    import random
    random.shuffle(odd_vert)

    while odd_vert:
        v = odd_vert.pop()
        length = float("inf")
        u = 1
        closest = 0
        for u in odd_vert:
            if v != u and G[v][u] < length:
                length = G[v][u]
                closest = u

        MST.append((v, closest, length))
        odd_vert.remove(closest)


# Takes the union of the min span tree and minimum weight matching and returns a eulerian circuit
# O(n^2)
def find_eulerian_tour(MatchedMSTree, G):
    # find neigbours
    neighbours = {}
    for edge in MatchedMSTree:
        if edge[0] not in neighbours:
            neighbours[edge[0]] = []

        if edge[1] not in neighbours:
            neighbours[edge[1]] = []

        neighbours[edge[0]].append(edge[1])
        neighbours[edge[1]].append(edge[0])

    # finds the hamiltonian circuit
    start_vertex = MatchedMSTree[0][0]
    EP = [neighbours[start_vertex][0]]

    while len(MatchedMSTree) > 0:
        for i, v in enumerate(EP):
            if len(neighbours[v]) > 0:
                break

        while len(neighbours[v]) > 0:
            w = neighbours[v][0]

            remove_edge_from_matchedMST(MatchedMSTree, v, w)

            del neighbours[v][(neighbours[v].index(w))]
            del neighbours[w][(neighbours[w].index(v))]

            i += 1
            EP.insert(i, w)

            v = w

    return EP


def remove_edge_from_matchedMST(MatchedMST, v1, v2):
    for i, item in enumerate(MatchedMST):
        if (item[0] == v2 and item[1] == v1) or (item[0] == v1 and item[1] == v2):
            del MatchedMST[i]

    return MatchedMST
