def valid(set, num, pos):
    # Check row
    for i in range(len(set[0])):
        if set[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(set)):
        if set[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if set[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(set):
    find = find_empty(set)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(set, i, (row, col)):
            set[row][col] = i

            if solve(set):
                return True

            set[row][col] = 0

    return False

def find_empty(set):
    for i in range(len(set)):
        for j in range(len(set[0])):
            if set[i][j] == 0:
                return (i, j)  # row, col

    return None

def print_board(set):
    for i in range(len(set)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(set[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(set[i][j])
            else:
                print(str(set[i][j]) + " ", end="")
