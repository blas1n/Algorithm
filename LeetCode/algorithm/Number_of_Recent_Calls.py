class RecentCounter:

    def __init__(self):
        self.reqs = []

    def ping(self, t: int) -> int:
        self.reqs.append(t)
        n = 0
        for r in self.reqs[::-1]:
            if t - 3000 <= r:
                n += 1
            else:
                break
        return n