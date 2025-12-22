class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                while stack:
                    if stack[-1] < 0:
                        stack.append(a)
                        break
                    elif stack[-1] < -a:
                        stack.pop()
                    elif stack[-1] == -a:
                        stack.pop()
                        break
                    else:
                        break
                else:
                    stack.append(a)

        return stack