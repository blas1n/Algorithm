import queue

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r, d = queue.Queue(), queue.Queue()
        for i, s in enumerate(senate):
            if s == 'R':
                r.put(i)
            else:
                d.put(i)

        order = len(senate)
        while r.qsize() > 0 and d.qsize() > 0:
            if r.get() < d.get():
                r.put(order)
            else:
                d.put(order)
            order += 1

        return 'Radiant' if r.qsize() > 0 else 'Dire'