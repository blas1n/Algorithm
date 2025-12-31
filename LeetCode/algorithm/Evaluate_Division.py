def dfs(start, end, graph):
    stack = [(start, 1.0)]
    visited = set()
    while stack:
        node, val = stack.pop()
        if node not in graph:
            return -1

        if node == end:
            return val

        for edge, cost in graph[node]:
            if edge not in visited:
                visited.add(edge)
                stack.append((edge, val * cost))

    return -1

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        flattened = [item for sublist in equations for item in sublist]
        graph = { key: [] for key in flattened }
        for i in range(len(equations)):
            lhs, rhs = equations[i]
            if not graph[lhs]:
                graph[lhs].append((lhs, 1.0))
            if not graph[rhs]:
                graph[rhs].append((rhs, 1.0))
            graph[lhs].append((rhs, values[i]))
            graph[rhs].append((lhs, 1 / values[i]))

        answer = []
        for start, end in queries:
            answer.append(dfs(start, end, graph))
        return answer