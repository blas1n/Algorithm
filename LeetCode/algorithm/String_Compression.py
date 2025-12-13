class Solution:
    def compress(self, chars: List[str]) -> int:
        read, write = 0, 0

        while read < len(chars):
            c = chars[read]
            cnt = 0

            while read < len(chars) and c == chars[read]:
                read += 1
                cnt += 1

            if cnt > 1:
                str_cnt = list(str(cnt))
                chars[write + 1:read] = str_cnt
                read = write + len(str_cnt) + 1
            write = read
        return write