symbol = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

prefix = {
    "I": set(["V", "X"]),
    "X": set(["L", "C"]),
    "C": set(["D", "M"]),
}

class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        cur_prefix = ""
        for c in s:
            if cur_prefix:
                if c in prefix[cur_prefix]:
                    answer += symbol[c] - symbol[cur_prefix]
                    cur_prefix = ""
                    continue
                else:
                    answer += symbol[cur_prefix]
                cur_prefix = ""
            if c in prefix:
                cur_prefix = c
            else:
                answer += symbol[c]
        if cur_prefix:
            answer += symbol[cur_prefix]
        return answer