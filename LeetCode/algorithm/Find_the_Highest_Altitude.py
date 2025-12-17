class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        answer, altitude = 0, 0
        for g in gain:
            altitude += g
            answer = max(answer, altitude)
        return answer