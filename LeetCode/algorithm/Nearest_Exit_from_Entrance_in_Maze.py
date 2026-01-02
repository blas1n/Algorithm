from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        level, r, c = 0, len(maze), len(maze[0])
        queue = deque([entrance])
        maze[entrance[0]][entrance[1]] = '+'
        while queue:
            level += 1
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= r or ny < 0 or ny >= c:
                        continue
                    if maze[nx][ny] == '.':
                        if nx == 0 or ny == 0 or nx == r - 1 or ny == c - 1:
                            return level
                        maze[nx][ny] = '+'
                        queue.append([nx, ny])
        return -1