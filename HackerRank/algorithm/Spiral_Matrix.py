class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dx, dy = 1, 0
        x, y = 0, 0
        width, height = len(matrix[0]), len(matrix)
        minX, maxX, minY, maxY = 0, width - 1, 0, height - 1
        answer = []
        for _ in range(width * height):
            answer.append(matrix[y][x])
            if dx == 1 and x == maxX:
                dx = 0
                dy = 1
                minY += 1
            elif dy == 1 and y == maxY:
                dx = -1
                dy = 0
                maxX -= 1
            elif dx == -1 and x == minX:
                dx = 0
                dy = -1
                maxY -= 1
            elif dy == -1 and y == minY:
                dx = 1
                dy = 0
                minX += 1
            x += dx
            y += dy
        return answer