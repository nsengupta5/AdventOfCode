def getCommands():
    with open('input.txt') as file:
        tmp = file.read()

    return tmp.split('\n')

def main():
    x = 0
    y = 0
    aim = 0

    commands = getCommands()[:-1]
    for command in commands:
        data = command.split(' ')
        dist = int(data[1])
        if (data[0]) == 'forward':
            y += aim * dist
            x += dist
        elif (data[0]) == 'up':
            aim -= dist
        else:
            aim += dist

    print(x * y)

if __name__ == "__main__":
    main()
