#!/usr/bin/python3
"""this is a prime game"""


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Determine the winner of each round using dynamic programming."""
    if not nums or x < 1:
        return None

    # Find the maximum number in nums
    max_num = max(nums)

    # Implement the Sieve of Eratosthenes to find all primes up to max_num
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False

    # Count the number of primes up to each index
    prime_count = [0] * (max_num + 1)
    for i in range(2, max_num + 1):
        prime_count[i] = prime_count[i - 1] + is_prime[i]

    player_1 = 0
    for p in nums:
        # Maria wins if the count of primes up to p is odd
        player_1 += prime_count[p] % 2 == 1

    # Determine the overall winner
    if player_1 * 2 == len(nums):
        return None

    if player_1 * 2 > len(nums):
        return "Maria"  # Maria wins more rounds than Ben

    return "Ben"  # Ben wins more rounds than Maria
