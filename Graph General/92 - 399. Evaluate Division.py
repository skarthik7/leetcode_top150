class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for (x, y), val in zip(equations, values):
            if x in graph:
                graph[x][y] = val
            else:
                graph[x] = {y: val}
            if y in graph:
                graph[y][x] = 1.0 / val
            else:
                graph[y] = {x: 1.0 / val}

        def dfs(x, y, visited):
            if x not in graph:
                return -1.0
            if y in graph[x]:
                return graph[x][y]
            for neighbor, val in graph[x].items():
                if neighbor not in visited:
                    visited.add(neighbor)
                    prod = dfs(neighbor, y, visited)
                    if prod != -1:
                        return val * prod
            return -1.0

        answers = []
        for x, y in queries:
            answers.append(dfs(x, y, set()))
        return answers