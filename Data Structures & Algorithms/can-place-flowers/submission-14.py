class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        for i in range(len(flowerbed)):
            if i == 0 and flowerbed[i] == 0 and i + 1 < len(flowerbed) and flowerbed[i + 1] != 1:
                flowerbed[i] =1
                n-=1
            if i == len(flowerbed)-1 and flowerbed[i] == 0 and flowerbed[i - 1] != 1:
                flowerbed[i] = 1
                n-=1
            if flowerbed[i] == 0 and flowerbed[i - 1] != 1 and flowerbed[i + 1] != 1:
                flowerbed[i] = 1
                n-=1
            if n == 0:
                return True

        return n <= 0
            
