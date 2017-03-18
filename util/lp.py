def list_prod(l):
    product = 1

    for i in l:
        product *= i

    return product


def fact(i):
    if i == 0:
        return 1

    return fact(i - 1) * i
