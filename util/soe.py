from math import *


def count_upper(n, primes):
    return len(primes) <= n


def sieve_of_eratosthenes(n, bound=count_upper, primes=[2]):
    # TODO speed up
    i = primes[len(primes) - 1] + 1
    test_bound = 10
    while bound(n, primes):
        is_prime = True

        if i >= test_bound:
            test_bound *= 10
        upper = test_bound

        for p in primes:
            if p > upper:
                break

            if i % p == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(i)

        i += 2

    return primes


def prime_generator():
    primes = [2]
    i = 3

    while 1:
        is_prime = 1

        upper = sqrt(i)

        for p in primes:
            if p > upper:
                break

            if i % p == 0:
                is_prime = 0
                break

        if is_prime:
            primes.append(i)
            yield i

        i += 1


def soe_fast(max):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

    # start off with lower = first number not in primes and
    # upper = lower ^ 2
    lower = 32
    upper = 1024

    while lower < max:
        n = list(range(lower, upper))

        for p in primes:
            for m in range(ceil(lower / p), ceil(upper / p)):
                n[p * m - lower] = 0

        primes += [p for p in n if p != 0]

        lower = upper
        upper = min(max + 1, upper + 1024)

    return primes
