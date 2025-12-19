from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        word_map1 = dict(Counter(word1))
        word_map2 = dict(Counter(word2))

        return set(word_map1.keys()) == set(word_map2.keys()) and Counter(word_map1.values()) == Counter(word_map2.values())