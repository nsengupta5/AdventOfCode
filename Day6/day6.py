def getData():
    with open("input2.txt") as file:
        data = file.read()

    fishes = data.split(',')
    fishes[-1] = fishes[-1][:-1]
    return [int(f) for f in fishes]

def getTotalBirths(f, num_days, total):
    if f + 9 > num_days:
        return total

    children = []
    f += 9
    while (f <= num_days):
        children.append(f)
        total += 1
        f += 7

    sub_total = total
    for c in children:
        sub_total += getTotalBirths(c, num_days, 0)

    return sub_total

def main():
    data = getData()
    num_days = 256
    total = len(data)
    children = []

    for f in data:
        start = f + 1
        children.append(start)
        total += 1

        start += 7
        while (start <= num_days):
            children.append(start)
            total += 1
            start += 7

    for k in children:
        total += getTotalBirths(k, num_days, 0)

    print(total)

if __name__ == "__main__":
    main()
