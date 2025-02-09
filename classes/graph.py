from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        for u, v in edges:
            self.add_edge(u, v)

    def add_edge(self, u, v):
        """Ajoute une arête entre u et v (graphe non orienté)"""
        self.graph[u].append(v)
        self.graph[v].append(u)

    def find_all_paths(self, start, end, path=[]):
        """Trouve tous les chemins de start à end"""
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph:
            return []

        paths = []
        for node in self.graph[start]:
            if node not in path:
                new_paths = self.find_all_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

edges = [
    ("Mercury", "Venus"), ("Venus", "Mercury"),
    ("Venus", "Earth"), ("Earth", "Venus"),
    ("Earth", "Mars"), ("Mars", "Earth"),
    ("Mars", "Jupiter"), ("Jupiter", "Mars"),
    ("Jupiter", "Saturn"), ("Saturn", "Jupiter"),
    ("Saturn", "Uranus"), ("Uranus", "Saturn"),
    ("Uranus", "Neptune"), ("Neptune", "Uranus"),

    ("Mercury", "Earth"), ("Earth", "Mercury"),
    ("Venus", "Mars"), ("Mars", "Venus"),
    ("Earth", "Jupiter"), ("Jupiter", "Earth"),
    ("Mars", "Saturn"), ("Saturn", "Mars"),
    ("Jupiter", "Uranus"), ("Uranus", "Jupiter"),
    ("Saturn", "Neptune"), ("Neptune", "Saturn"),

    ("Mercury", "Mars"), ("Mars", "Mercury"),
    ("Venus", "Jupiter"), ("Jupiter", "Venus"),
    ("Earth", "Saturn"), ("Saturn", "Earth"),
    ("Mars", "Uranus"), ("Uranus", "Mars"),
    ("Jupiter", "Neptune"), ("Neptune", "Jupiter"),
    ("Earth", "Neptune"), ("Neptune", "Earth"),

    ("Mercury", "Saturn"), ("Saturn", "Mercury"),
    ("Venus", "Uranus"), ("Uranus", "Venus"),
    ("Earth", "Neptune"), ("Neptune", "Earth"),
    ("Mars", "Jupiter"), ("Jupiter", "Mars"),
    ("Jupiter", "Neptune"), ("Neptune", "Jupiter"),
    ("Saturn", "Earth"), ("Earth", "Saturn"),
    ("Uranus", "Mars"), ("Mars", "Uranus")
]

