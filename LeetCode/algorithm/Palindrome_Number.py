class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elem = []
        while x > 0:
            elem.append(x % 10)
            x //= 10
        for i in range(len(elem) // 2):
            if elem[i] != elem[-i - 1]:
                return False
        return True