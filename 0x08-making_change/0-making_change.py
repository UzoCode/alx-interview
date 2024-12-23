#!/usr/bin/python3
"""
From within comes change
"""


def makeChange(coins, total):
    """
    Function that determines fewest number of coins 
    to meet a given amount total
    """
    if total <= 0:
        return 0
    dp = [0] + [float("inf")] * (total)
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1] if dp[-1] != float("inf") else -1
    
