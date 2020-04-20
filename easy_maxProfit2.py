# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, list_price):
        if len(list_price) < 2:
            return 0
        
        all_profit = 0
        # prev_price = list_price[0]
        for idx_price, cur_price in enumerate(list_price[1:], start=1):
            if cur_price > list_price[idx_price - 1]:
                all_profit += cur_price - list_price[idx_price - 1]
        return all_profit


class SelfImplement:
    def maxProfit(self, list_price):
        if len(list_price) < 2:
            return 0
        
        all_profit = 0
        min_price = list_price[0]
        max_price = min_price
        for idx_price, cur_price in enumerate(list_price[1:], start=1):
            if cur_price > max_price:
                max_price = cur_price
                if idx_price == len(list_price) - 1:
                    all_profit += max_price - min_price
            else:
                all_profit += max_price - min_price
                min_price = cur_price
                max_price = min_price
        return all_profit

test_cases = [
    ([7,6,4,3,1], 0),
    ([7,1,5,3,6,4], 7),
    ([3,5,4,6,1,7], 10),
]


for idx, (test_case, solution) in enumerate(test_cases):
    output = Solution().maxProfit(test_case)
    if output != solution:
        print(f'error at test case: {idx}, current_output: {output}, expected solution: {solution}')
    





