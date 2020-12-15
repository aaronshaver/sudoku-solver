from itertools import chain

# input format is starting upper left, do left to right whole row,
# then additional rows top to bottom

# "easy" puzzle #13 from Funster 1,000+ Sudoku Puzzles
# PUZZLE_INPUT = "3    2697 8    32     6   843 79 1 2  6 4 9  7 1 23 649   3     63    4 2579    6"

# "medium" puzzle #150 from Funster 1,000+ Sudoku Puzzles
# PUZZLE_INPUT = " 82 6   7 4   1  99  4  6   9  8     3 692 8     1  7   8  7  33  2   5 7   3 82 "

# "hard" puzzle #150 from Funster 1,000+ Sudoku Puzzles
PUZZLE_INPUT = " 4  9 8 6926           692 6 9  5      914      6  5 7 937           7198 5 4  6 "

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
            print("░░░░░░░░░░░")
        for j in range(0,9):
            if (j != 0 and j % 3 == 0):
                print('░', end='')
            element = grid[i][j]
            if not is_solved(element):
                print('.', end='')
            else:
                print(element[0], end='')
        print()
    print('\nUnsolved squares:', get_num_unsolved_squares(grid))

def get_other_rows_cols_solved(row_num, col_num, grid):
    """ for a given coordinate square, get solved numbers from the the four other rows (2) and columns (2)
    that radiate from its 3x3 block """

    # I have a feeling there's a more clever way to do this but I'm tired
    lookup_table = {
        0: [1,2],
        1: [0,2],
        2: [0,1],
        3: [4,5],
        4: [3,5],
        5: [3,4],
        6: [7,8],
        7: [6,8],
        8: [6,7]
    }
    rows_to_check = lookup_table[row_num]
    cols_to_check = lookup_table[col_num]

    all_solved = []
    all_solved.append([x for x in get_row(rows_to_check[0], grid) if is_solved(x)])
    all_solved.append([x for x in get_row(rows_to_check[1], grid) if is_solved(x)])
    all_solved.append([x for x in get_column(cols_to_check[0], grid) if is_solved(x)])
    all_solved.append([x for x in get_column(cols_to_check[1], grid) if is_solved(x)])
    return [x[0] for x in list(chain.from_iterable(all_solved))]  # wow this is ugly

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

def get_column(col_num, grid):
    column = []
    for row_num in range (0,9):
        column.append(grid[row_num][col_num])
    return column

def get_row(row_num, grid):
    row = []
    for col_num in range (0,9):
        row.append(grid[row_num][col_num])
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
    for col_num in range(0,9):
        column = get_column(col_num, grid)
        for row_num in range(0,9):
            current_element = grid[row_num][col_num]
            if not is_solved(current_element):
                solved_elements = [x for x in column if is_solved(x)]
                for solved in solved_elements:
                    solved_value = solved[0]
                    if solved_value in current_element:
                        grid[row_num][col_num].remove(solved_value)
    return grid

def cull_by_known_rows(grid):
    """ reduces initial candidates by eliminating based on initial, known numbers by row scanning """
    for row_num in range(0,9):
        row = get_row(row_num, grid)
        for col_num in range(0,9):
            current_element = grid[row_num][col_num]
            if not is_solved(current_element):
                solved_elements = [x for x in row if is_solved(x)]
                for solved in solved_elements:
                    solved_value = solved[0]
                    if solved_value in current_element:
                        grid[row_num][col_num].remove(solved_value)
    return grid

def get_block_coords(row_num, col_num):
    """ returns the upper left coordinates of the block in which the input coords exist """
    return [row_num - (row_num % 3), col_num - (col_num % 3)]

def cull_by_known_blocks(grid):
    """ reduces initial candidates by eliminating based on initial, known numbers by block scanning """
    for row_num in range(0,9):
        for col_num in range(0,9):
            current_element = grid[row_num][col_num]
            if not is_solved(current_element):
                block_coords = get_block_coords(row_num, col_num)
                current_block = get_block(ul_row_num=block_coords[0], ul_col_num=block_coords[1], grid=grid)
                solved_elements = [x for x in current_block if is_solved(x)]
                for solved in solved_elements:
                    solved_value = solved[0]
                    if solved_value in current_element:
                        grid[row_num][col_num].remove(solved_value)
    return grid

def get_four_count_nums(candidates, disallowed_nums):
    """ if there are four of a given number in the rows and columns not shared by the square
    under test, and the number isn't already in the block, that number has to be in the square
    under test (I think) """
    collector = {}
    for num in candidates:
        if num not in collector.keys():
            collector[num] = 1
        else:
            old_value = collector[num]
            collector[num] = old_value + 1
    output = []
    for key, value in collector.items():
        if value == 4 and [key] not in disallowed_nums:
            output.append(key)
    return output

def cull_by_four_cross_lines(grid):
    """ for each square, get solved numbers from the four other rows (2 of them) and columns (2 of them)
    that radiate from its 3x3 block, and use that to see if there's a provably-correct solved square """
    for row_num in range(0,9):
        for col_num in range(0,9):
            current_element = grid[row_num][col_num]
            if not is_solved(current_element):
                candidates = get_other_rows_cols_solved(row_num, col_num, grid)
                # need to remove numbers already in block from the candidates, because there can be
                # cases where the number of "four numbers" is more than one
                # there's likely a more efficient way to do this, of course
                block_coords = get_block_coords(row_num, col_num)
                solved_current_block = get_block(ul_row_num=block_coords[0], ul_col_num=block_coords[1], grid=grid)
                disallowed_nums = [x for x in solved_current_block if is_solved(x)]
                fours = get_four_count_nums(candidates, disallowed_nums)
                if len(fours) == 1:
                    grid[row_num][col_num] = [fours[0]]
    return grid

grid = build_grid(PUZZLE_INPUT)
print('\nOriginal puzzle:')
print_grid(grid)

while get_num_unsolved_squares(grid) > 0:
    grid = cull_by_known_columns(grid)
    grid = cull_by_known_rows(grid)
    grid = cull_by_known_blocks(grid)
    grid = cull_by_four_cross_lines(grid)
    print_grid(grid)

print('\n\nSolved puzzle:')
print_grid(grid)
