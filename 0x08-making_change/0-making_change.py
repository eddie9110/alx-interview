#!/usr/bin/python3
"""
determine the fewest number of coins needed to
meet a given amount of change
"""


def makeChange(coins, total):
    if total == 0:
        return 0
    if len(coins) == 0 or coins is None:
        return -1

    balance = total
    change = 0
    for coin in sorted(coins, reverse=True):
        while (balance >= coin and balance % coin >= 0):
            change += int(balance / coin)
            balance = balance % coin
    change = change if balance == 0 else -1
    return change
