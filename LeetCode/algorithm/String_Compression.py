class Solution:
    def compress(self, chars: List[str]) -> int:
        read, write = 0, 0

        while read < len(chars):
            c = chars[read]
            cnt = 0
            while read < len(chars) and c == chars[read]:
                read += 1
                cnt += 1

            chars[write] = c
            write += 1
            if cnt > 1:
                for digit in str(cnt):
                    chars[write] = digit
                    write += 1

        return write