class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerable_num = 0
        if flowerbed[0] == 0 and (len(flowerbed) < 2 or flowerbed[1] == 0):
            flowerable_num += 1
            flowerbed[0] = 1

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerable_num += 1
                flowerbed[i] = 1

        if len(flowerbed) > 1 and flowerbed[-2] == 0 and flowerbed[-1] == 0:
            flowerable_num += 1

        return flowerable_num >= n
