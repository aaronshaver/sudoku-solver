PUZZLE_INPUT = "  2 5 1  56     898 31 62 52 7   6 8   2 3   4 8   3 19 47 58 318     72  5 6 9  "

def build_grid(puzzle):
    output = []
    input_position = 0

    for i in range(0,9):
        row = []
        for j in range(0,9):
            row.append(puzzle[input_position])
            input_position += 1
        output.append(row)
    return output

def print_grid(grid):
    for i in range(0,9):
        for j in range(0,9):
            print(grid[i][j], end='')
        print()

grid = build_grid(PUZZLE_INPUT)
print_grid(grid)