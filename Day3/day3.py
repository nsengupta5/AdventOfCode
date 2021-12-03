def getData():
    with open('input.txt') as file:
        data = file.read()

    return [x for x in data.split('\n') if x != '']

def convertToDecimal(rate):
    total = 0
    for i, c in enumerate(reversed(rate)):
        if c == '1':
            total += pow(2, i)

    return total

def getRating(data, importance):
    index = 0
    point_len = len(data[0])

    while (index < point_len):
        if (len(data) == 1):
            return convertToDecimal(data[0])

        ones = 0
        zeros = 0

        for point in data:
            if point[index] == '1':
                ones += 1
            else:
                zeros += 1

        if importance == 0:
            if zeros > ones:
                data = list(filter(lambda point: (point[index] == '1'), data))
            else:
                data = list(filter(lambda point: (point[index] == '0'), data))
        else:
            if zeros > ones:
                data = list(filter(lambda point: (point[index] == '0'), data))
            else:
                data = list(filter(lambda point: (point[index] == '1'), data))

        index += 1

    return convertToDecimal(data[0])

def part1():
    data = getData()
    point_len = len(data[0])
    index = 0
    gamma = ""
    epsilon = ""

    while (index < point_len):
        ones = 0
        zeros = 0

        for point in data:
            if point[index] == '1':
                ones += 1
            else:
                zeros += 1
        
        if ones > zeros:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

        index += 1

    print(convertToDecimal(gamma) * convertToDecimal(epsilon))

def part2():
    oxygen = getData()
    co2 = oxygen.copy()

    print(getRating(oxygen, 1) * getRating(co2, 0))

if __name__ == "__main__":
    part1()
    part2()
