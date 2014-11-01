# Write function to compute Nth fibonacci number
# F_0 = 0, F_1 = 1
# F_n = F_n-1 + F_n-2

memoize = {0: 0, 1: 1}


def fib(n):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = fib(n - 1) + fib(n - 2)

    return memoize[n]


if __name__ == "__main__":
    print fib(10)
