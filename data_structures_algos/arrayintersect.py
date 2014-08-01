
def intersect(xs, ys):

    snd = dict()

    for y in ys:
        snd[y] = "whatever"

    matches = []

    for x in xs:
        if x in snd.keys():
            matches.append(x)

    return matches

if __name__ == "__main__":
    a = [1, 5, 6, 8, 9, 15]
    b = [2, 3, 4, 5, 9, 20, 31, 33, 34]
    print intersect(a, b)