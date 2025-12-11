class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        for i, c in enumerate(s):
            if c.lower() in 'aeiou':
                vowels.append((i, c))

        answer = list(s)
        for i in range(len(vowels) // 2):
            rev_i = -i - 1
            answer[vowels[i][0]] = vowels[rev_i][1]
            answer[vowels[rev_i][0]] = vowels[i][1]
        return ''.join(answer)
