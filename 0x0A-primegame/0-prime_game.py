#!/usr/bin/python3
""" prime game module"""


def isWinner(x, nums):
    """
    Function that checks the winner
    args:
        x = number of rounds and nums is an array of n
    Return:
        name of the player that won the most rounds
        If winner cannot be determined, return None
        Assume n and x will not be larger than 10000
    """
    rounds = 0
    Maria = 0
    nums2 = max(nums)
    state = [True for _ in range(max(nums2 + 1, 2))]
    for x in range(2, int(pow(nums2, 0.5)) + 1):
        if not state[x]:
            continue
        for i in range(x * x, nums2 + 1, x):
            state[i] = False
    state[0] = state[1] = False

    for k in range(len(state)):
        if state[k]:
            rounds += 1
        state[k] = rounds
    
    for j in nums:
        Maria += state[j] % 2 == 1
    if Maria * 2 > len(nums):
        return "Maria"
    if Maria * 2 == len(nums):
        return None
    return "Ben"
