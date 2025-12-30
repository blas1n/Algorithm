class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        answer = 0
        stack = []
        visited = [False] * len(isConnected)
        for city in range(len(isConnected)):
            if visited[city]:
                continue

            answer += 1
            stack.append(city)

            while stack:
                i = stack.pop()
                visited[i] = True
                for j in range(len(isConnected)):
                    if (isConnected[i][j] and not visited[j]):
                        stack.append(j)
                        visited[j] = True

        return answer