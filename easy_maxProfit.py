# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class SelfImplement:
    def maxProfit(self, list_price):
        if len(list_price) < 2:
            return 0
        
        min_price = list_price[0]
        max_profit = 0
        for cur_price in list_price[1:]:
            max_profit = max(max_profit, cur_price - min_price)
            min_price = min(min_price, cur_price)
        return max_profit

test_cases = [
    ([7,6,4,3,1], 0),
    ([7,1,5,3,6,4], 5)
]


for idx, (test_case, output) in enumerate(test_cases):
    if SelfImplement().maxProfit(test_case) != output:
        print(f'error at test case: {idx}')
    





