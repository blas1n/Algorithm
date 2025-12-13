class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        short_word = ''.join([char1 + char2 for char1, char2 in zip(word1, word2)])
        if len(word1) > len(word2):
            return short_word + word1[len(word2):]
        if len(word1) < len(word2):
            return short_word + word2[len(word1):]
        return short_word
