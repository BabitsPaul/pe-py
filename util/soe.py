from math import sqrt


def count_upper(n, primes):
    return len(primes) <= n


def sieve_of_eratosthenes(n, bound=count_upper, primes=[2]):
    i = primes[len(primes) - 1] + 1
    while bound(n, primes):
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

        i += 1

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