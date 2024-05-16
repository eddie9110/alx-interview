#!/usr/bin/python3
""" prime game module"""


def is_prime(num):
    """ function checks if a number is a prime number"""
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


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
    Maria = Ben = 0
    nums.sort()
    for check in range(x):
        round = 0
        list_of_nums = list(range(1, nums[check] + 1))

        while True:
            state = False
            for i, x in enumerate(list_of_nums):
                if x > 1 and is_prime(x):
                    for j in range(len(list_of_nums)):
                        if list_of_nums[j] % x == 0:
                            list_of_nums[j] = 0
                    state = True
                    round += 1
                    break
            if state is False:
                break
        if round % 2 != 0:
            Maria += 1
        else:
            Ben += 1
    # checking the winner
    if Maria > Ben:
        return "Maria"
    if Maria == Ben:
        return None
    return "Ben"
