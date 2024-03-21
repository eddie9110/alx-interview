def minOperations(n: int) -> int:
    """method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file."""
    no_of_times = 0

    char1 = 'H'
    char2 = 'H'

    while (len(char2) < n):
        if n % len(char2) == 0:
            no_of_times += 2
            char1 = char2
            char2 += char2
        else:
            no_of_times += 1
            char2 += char1

    if len(char2) != n:
        return 0

    return no_of_times
