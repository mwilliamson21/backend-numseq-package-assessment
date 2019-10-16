def is_prime(m):
    """returns boolean indicating whether m is prime"""
    if m > 1:
        for i in range(2, m):
            if m % i == 0:
                return False
        return True


def primes(n):
    """returns list of primes less than n"""
    prime_list = []
    for num in range(n):
        if is_prime(num):
            prime_list.append(num)
    return prime_list
