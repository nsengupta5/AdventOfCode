def getData():
    boards = []
    with open('input.txt') as file:
        nums = file.readline().rstrip().split(',')
        while (file.readline() != ""):
            board = []
            for i in range(5):
                row = file.readline().rstrip().split(' ')
                board.append([x for x in row if x != ''])
                
            boards.append(board)

    return (nums, boards)

def part1():
    data = getData()
    boards = data[1]
    nums = data[0]

    winners = []
    index = -1
    while len(winners) < len(boards):
        index += 1
        for k, board in enumerate(boards):
            if k not in winners:
                for i, row in enumerate(board):
                    for j, col in enumerate(row):
                        if col == nums[index]:
                            board[i][j] = -1

                found = False
                for row in board:
                    if row == [-1] * 5:
                        winners.append(k)
                        found = True
                        break

                if not found:
                    for col in zip(*board):
                        if list(col) == [-1] * 5:
                            winners.append(k)
                            break

    total_score = 0
    for row in boards[winners[-1]]:
        for col in row:
            if col != -1:
                total_score += int(col)

    total_score *= int(nums[index])
    print(total_score)
    
if __name__ == "__main__":
    part1()
