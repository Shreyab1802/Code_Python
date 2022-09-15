class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #         min_price = min(prices)
        #         min_price_index = prices.index(min_price)
        #         # if min_price_index != len(prices)-2:
        #         #     profit = max(prices[min_price_index:]) - min_price
        #         #     return profit
        #         max_price = max(prices)
        #         max_price_index = prices.index(max_price)

        #         if min_price_index != len(prices)-1:
        #             profit = min(prices[min_price_index:]) - prices[min_price_index]
        #             return profit

        #         else:
        #             return 0

        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            current_profit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit = max(current_profit, max_profit)
            else:
                left = right
            right += 1
        return max_profit
