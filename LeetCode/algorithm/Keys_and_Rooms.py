class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        visited = [False] * len(rooms)
        
        while stack:
            i = stack.pop()
            visited[i] = True
            
            for j in rooms[i]:
                if not visited[j]:
                    stack.append(j)
                    visited[j] = True

        return all(visited)