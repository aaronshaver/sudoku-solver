# input format is starting upper left, do left to right whole row,
# then additional rows top to bottom

# "easy" puzzle #13 from Funster 1,000+ Sudoku Puzzles
# PUZZLE_INPUT = "3    2697 8    32     6   843 79 1 2  6 4 9  7 1 23 649   3     63    4 2579    6"

# "medium" puzzle #150 from Funster 1,000+ Sudoku Puzzles
PUZZLE_INPUT = " 82 6   7 4   1  99  4  6   9  8     3 692 8     1  7   8  7  33  2   5 7   3 82 "

# "hard" puzzle #330 from Funster 1,000+ Sudoku Puzzles
# PUZZLE_INPUT = "15 23         45    2   9  2  7   566  321  979   6  8  9   1    64         57 42"

given_numbers = 0

def build_grid(puzzle):
    output = []
    input_position = 0

    for i in range(0,9):
        row = []
        for j in range(0,9):
            element = puzzle[input_position]
            if (element != ' '):
                row.append([element])
                global given_numbers
                given_numbers += 1
            else:
                # basically we create ALL the "pencil marks"/candidates for all empty spaces
                row.append(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
            input_position += 1
        output.append(row)
    return output

def is_solved(element):
    return len(element) == 1

def print_grid(grid):
    print()
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
    print('\nUnsolved squares:', get_num_unsolved_squares(grid))

def get_num_unsolved_squares(grid):
    total = 0
    for i in range(0,9):
        for j in range(0,9):
            if not is_solved(grid[i][j]):
                total += 1
    return total

def get_num_candidates(grid):
    total = 0
    for i in range(0,9):
        for j in range(0,9):
            element = grid[i][j]
            if not is_solved(element):
                total += len(element)
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

def get_block(ul_row_num, ul_col_num, grid):
    """ ul_ params are the upper left row and column numbers """
    output = []
    for col_modifier in range(0,3):
        for row_modifier in range(0,3):
            output.append(grid[ul_row_num + row_modifier][ul_col_num + col_modifier])
    return output

def cull_by_known_columns(grid):
    # ought to refactor this and its sister methods: most of the code is the same
    """ reduces initial candidates by eliminating based on initial, known numbers by column scanning """
    for column_num in range(0,9):
        column = get_column(column_num, grid)
        for row_num in range(0,9):
            current_element = grid[row_num][column_num]
            if not is_solved(current_element):
                solved_elements = [x for x in column if is_solved(x)]
                for solved in solved_elements:
                    solved_value = solved[0]
                    if solved_value in current_element:
                        grid[row_num][column_num].remove(solved_value)
                        if is_solved(grid[row_num][column_num]):
                            print(grid[row_num][column_num][0], end='')
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
                    solved_value = solved[0]
                    if solved_value in current_element:
                        grid[row_num][column_num].remove(solved_value)
                        if is_solved(grid[row_num][column_num]):
                            print(grid[row_num][column_num][0], end='')
    return grid

def get_block_coords(row_num, col_num):
    """ returns the upper left coordinates of the block in which the input coords exist """
    return [row_num - (row_num % 3), col_num - (col_num % 3)]

def cull_by_known_blocks(grid):
    """ reduces initial candidates by eliminating based on initial, known numbers by block scanning """
    for row_num in range(0,9):
        for column_num in range(0,9):
            current_element = grid[row_num][column_num]
            if not is_solved(current_element):
                block_coords = get_block_coords(row_num, column_num)
                current_block = get_block(ul_row_num=block_coords[0], ul_col_num=block_coords[1], grid=grid)
                solved_elements = [x for x in current_block if is_solved(x)]
                for solved in solved_elements:
                    solved_value = solved[0]
                    if solved_value in current_element:
                        grid[row_num][column_num].remove(solved_value)
                        if is_solved(grid[row_num][column_num]):
                            print(grid[row_num][column_num][0], end='')
    return grid

grid = build_grid(PUZZLE_INPUT)
print('\nOriginal puzzle:')
print_grid(grid)

print('\nReal-time display of new solved squares:')
while get_num_unsolved_squares(grid) > 0:
    grid = cull_by_known_columns(grid)
    grid = cull_by_known_rows(grid)
    grid = cull_by_known_blocks(grid)

print('\n\nSolved puzzle:')
print_grid(grid)