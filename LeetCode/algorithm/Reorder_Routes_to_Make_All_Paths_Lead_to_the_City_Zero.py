class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for end, start in connections:
            graph[start].append((end, 0))
            graph[end].append((start, 1))
        
        answer = 0
        stack = [0]
        visited = set()

        while stack:
            i = stack.pop()
            visited.add(i)

            for j, cost in graph[i]:
                if j not in visited:
                    stack.append(j)
                    visited.add(j)
                    answer += cost

        return answer