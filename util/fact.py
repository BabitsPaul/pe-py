from util.soe import prime_generator


def factorize_distinct(n, primes=prime_generator()):
    factors = []

    for p in primes:
        if n % p == 0:
            factors.append(p)

    return factors


def factorize_all(n, primes=prime_generator()):
    factors = []

    for p in primes:
        while n % p == 0:
            factors.append(p)
            n /= p

    return factors


def factors(n, primes=prime_generator()):
    result = {}

    for p in primes:
        while n % p == 0:
            if p in result:
                result[p] += 1
            else:
                result[p] = 1

            n /= p

        if n == 0:
            break

    return result


def divisors(n):
    return [x for x in range(1, n) if n % x == 0]


def gcd(a, b):
    a, b = max(a, b), min(a, b)

    while b != 0:
        a, b = b, a % b

    return a
