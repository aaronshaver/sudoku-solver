# "easy" puzzle according to Funster 1,000+ Sudoku Puzzles
PUZZLE_INPUT = "  2 5 1  56     898 31 62 52 7   6 8   2 3   4 8   3 19 47 58 318     72  5 6 9  "

def build_grid(puzzle):
    output = []
    input_position = 0

    for i in range(0,9):
        row = []
        for j in range(0,9):
            element = puzzle[input_position]
            if (element != ' '):
                row.append(element)
            else:
                row.append(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
            input_position += 1
        output.append(row)
    return output

def is_unsolved(element):
    return len(element) > 1

def print_grid(grid):
    for i in range(0,9):
        if (i != 0 and i % 3 == 0):
            print("-----------")
        for j in range(0,9):
            if (j != 0 and j % 3 == 0):
                print('|', end='')
            element = grid[i][j]
            if is_unsolved(element):
                print('?', end='')
            else:
                print(element[0], end='')
        print()

def count_all(grid):
    """ counts both solved and unsolved candidate numbers
    closer to 81 is better; 729 is theoretical max but unlikely
    """
    total = 0
    for i in range(0,9):
        for j in range(0,9):
            total += len(grid[i][j])
    return total

grid = build_grid(PUZZLE_INPUT)
print_grid(grid)
print('\n', count_all(grid))