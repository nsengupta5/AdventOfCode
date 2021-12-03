def getNums():
    with open('input.txt') as file:
        tmp = file.read()

    return [int(x) for x in tmp.split('\n') if x != '']

def getCount(nums):
    counter = 0
    for i in range(len(nums) - 1):
        if nums[i + 1] > nums[i]:
            counter += 1

    print(counter)

def part1():
    nums = getNums()
    getCount(nums)

def part2():
    nums = getNums()
    windows = []
    for i in range(len(nums) - 2):
        win_sum = nums[i] + nums[i + 1] + nums[i + 2]
        windows.append(win_sum)

    getCount(windows)

if __name__ == "__main__":
    part1()
    part2()
