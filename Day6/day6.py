def getData():
    with open("input2.txt") as file:
        data = file.read()

    fishes = data.split(',')
    fishes[-1] = fishes[-1][:-1]
    return [int(f) for f in fishes]

def main():
    data = getData()
    print(data)

if __name__ == "__main__":
    main()
