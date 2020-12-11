# input format is starting upper left, do left to right whole row,
# then additional rows top to bottom

# "easy" puzzle #13 from Funster 1,000+ Sudoku Puzzles
PUZZLE_INPUT = "3    2697 8    32     6   843 79 1 2  6 4 9  7 1 23 649   3     63    4 2579    6"

def build_grid(puzzle):
    output = []
    input_position = 0

    for i in range(0,9):
        row = []
        for j in range(0,9):
            element = puzzle[input_position]
            if (element != ' '):
                row.append([element])
            else:
                # basically we create ALL the "pencil marks"/candidates for all empty spaces
                row.append(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
            input_position += 1
        output.append(row)
    return output

def is_solved(element):
    return len(element) == 1

def print_grid(grid):
    for i in range(0,9):
        if (i != 0 and i % 3 == 0):
            print("-----------")
        for j in range(0,9):
            if (j != 0 and j % 3 == 0):
                print('|', end='')
            element = grid[i][j]
            if not is_solved(element):
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

def get_column(column_num, grid):
    column = []
    for row_num in range (0,9):
        column.append(grid[row_num][column_num])
    return column

def get_row(row_num, grid):
    row = []
    for column_num in range (0,9):
        row.append(grid[row_num][column_num])
    return row

def cull_by_known_columns(grid):
    """ reduces initial candidates by eliminating based on initial, known numbers by column scanning """
    for column_num in range(0,9):
        column = get_column(column_num, grid)
        for row_num in range(0,9):
            current_element = grid[row_num][column_num]
            if not is_solved(current_element):
                solved_elements = [x for x in column if is_solved(x)]
                for solved in solved_elements:
                    grid[row_num][column_num].remove(solved[0])
    return grid

def cull_by_known_rows(grid):
    """ reduces initial candidates by eliminating based on initial, known numbers by row scanning """
    for row_num in range(0,9):
        row = get_row(row_num, grid)
        for column_num in range(0,9):
            current_element = grid[row_num][column_num]
            if not is_solved(current_element):
                solved_elements = [x for x in row if is_solved(x)]
                for solved in solved_elements:
                    if solved[0] in current_element:
                        grid[row_num][column_num].remove(solved[0])
    return grid

grid = build_grid(PUZZLE_INPUT)
grid = cull_by_known_columns(grid)
grid = cull_by_known_rows(grid)
print_grid(grid)
print('\n', count_all(grid))