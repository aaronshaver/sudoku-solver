# sudoku-solver

_[Warning: Dirty code ahead! I did this project over a few afternoons just to satisfy my curiosity. I wanted to see how far I could get without looking up any algorithms on the Internet. Since it was just for fun, I didn't bother with things like unit tests, performance optimizations, parameterized configuration, clean code refactoring, etc.]_

Note: While the program can solve a lot of sudoku puzzles (including all the medium difficulty ones I've thrown at it from a puzzle book I sourced from), it still has trouble with some of the hardest puzzles.

Edit 2020-12-15: I read up on sudoku algorithms. If I wanted to extend this project, I'd keep the existing functions and then, after they've been run a few times with no improvement (i.e. the number of unsolved squares stays the same for a couple cycles), I'd run the updated grid through a backtracing algorithm. This would be a hybrid approach. Against a hard puzzle, my functions are fast and can solve at least a few squares to get it started (and drastically reduce the number of candidates for unsolved squares!), then turn it over to backtracing (which is slow but solves every sudoku eventually).

## Usage

1. Update the value of the `PUZZLE_INPUT` string in the code to change which puzzle the program solves
1. Run `python main.py` (Python 3.x required)
