

def makeChange(cents, denoms, denom_index):

    if denom_index >= len(denoms):
        return 1

    denom = denoms[denom_index]
    ways = 0
    i = 0

    while i <= cents:
        amount_remaining = cents - i * denom
        ways += makeChange(amount_remaining, denoms, denom_index + 1)
        i += denom

    return ways


if __name__ == "__main__":
    denoms = [25, 10, 5, 1]
    print makeChange(100, denoms, 0)
