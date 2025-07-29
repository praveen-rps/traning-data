from collections import defaultdict

from datastructures.graphs import Graph


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, vertex1, vertex2):
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def hasCycle(self,v,visited,parent):
        visited.add(v)
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                if self.hasCycle(neighbor,visited,v):
                    return True
            elif parent != neighbor:
                return True
        return False

    def check_cycle(self):
        visited = set()
        for vertex in self.graph:
            if vertex not in visited:
                if self.hasCycle(vertex, visited, None):
                    return True
        return False

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('A','B')
    graph.add_edge('B','C')
    graph.add_edge('C','D')
    graph.add_edge('D','A')

    if graph.check_cycle():
         print("Graph has cycle")
    else:
         print("Graph has no cycle")