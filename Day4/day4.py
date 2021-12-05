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

def getTotalScore(board, index):
    total_score = 0
    for row in board:
        for col in row:
            if col != -1:
                total_score += int(col)

    total_score *= int(index)
    return total_score

def main():
    data = getData()
    boards = data[1]
    nums = data[0]

    winner_index = []
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
                        winner_index.append(index)
                        found = True
                        break

                if not found:
                    for col in zip(*board):
                        if list(col) == [-1] * 5:
                            winner_index.append(index)
                            winners.append(k)
                            break

    print("Part 1: " + str(getTotalScore(boards[winners[0]], nums[winner_index[0]])))
    print("Part 2: " + str(getTotalScore(boards[winners[-1]], nums[winner_index[-1]])))
    
if __name__ == "__main__":
    main()
