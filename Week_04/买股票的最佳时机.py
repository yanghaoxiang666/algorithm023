'''
算法流程:
遍历整个股票交易日价格列表 price，策略是所有上涨交易日都买卖（赚到所有利润），所有下降交易日都不买卖（永不亏钱）。
设 tmp 为第 i-1 日买入与第 i 日卖出赚取的利润，即 tmp = prices[i] - prices[i - 1] ；
当该天利润为正 tmp > 0，则将利润加入总利润 profit；当利润为 00 或为负，则直接跳过；
遍历完成后，返回总利润 profit。
复杂度分析：
时间复杂度 O(N)O(N) ： 只需遍历一次price；
空间复杂度 O(1)O(1) ： 变量使用常数额外空间。
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0: profit += tmp
        return profit
