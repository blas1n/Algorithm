import bisect

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        answer = []
        potions.sort()
        for spell in spells:
            pos = bisect.bisect_left(potions, success / spell)
            answer.append(len(potions) - pos)
        return answer