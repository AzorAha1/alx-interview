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
    """Determine the winner of each round."""
    maria_wins = 0
    ben_wins = 0

    for i in nums:
        prime_nums = [num for num in range(2, i + 1) if is_prime(num)]
        current_player = 'Maria'
        remainingnums = list(range(1, i + 1))
        while True:
            player = 'Maria' if current_player else 'Ben'
            chosen_prime = None
            for prime in prime_nums:
                if prime in remainingnums:
                    chosen_prime = prime
                    break
            if not chosen_prime:
                if player == 'Maria':
                    ben_wins += 1
                else:
                    maria_wins += 1
                break
            remainingnums = [
                num for num in remainingnums if num % chosen_prime != 0
                ]
            current_player = 'Maria' if current_player == 'Ben' else 'Ben'

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None