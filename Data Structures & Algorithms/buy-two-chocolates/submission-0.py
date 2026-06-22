class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        prices.sort(reverse = True)

        min_one = prices.pop()
        min_two = prices.pop()

        if min_one + min_two > money:
            return money
        return money - (min_one + min_two)