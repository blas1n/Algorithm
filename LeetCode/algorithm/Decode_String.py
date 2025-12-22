class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            c = s[i]
            if c == ']':
                word = []
                while stack:
                    cur = stack.pop()
                    if cur == '[':
                        scale = stack.pop()
                        stack.extend(word[::-1] * scale)
                        break
                    word.extend(cur)
            elif c.isdigit():
                scale_idx = i + 1
                while s[scale_idx].isdigit():
                    scale_idx += 1
                stack.append(int(s[i:scale_idx]))
                i = scale_idx - 1
            else:
                stack.append(c)
            i += 1
        return ''.join(stack)