# flag: GJVWUSSL[[QOESXVZVULWY^WQL[W^XO

from pwn import process
import sudoku
from imp_task import perform_important_task

def get_board(proc: process, delim: str):
    board = []

    curr_line = proc.recvline(False).decode()
    while not curr_line.startswith(delim):
        if "flag" in curr_line:
            print(curr_line)
        curr_line = proc.recvline(False).decode()
    
    for _ in range(13):
        if curr_line.startswith(" |"):
            line = []
            for char in curr_line.split():
                if char.isdigit():
                    line.append(int(char))
                elif char == ".":
                    line.append(0)
            board.append(line)
        curr_line = proc.recvline(False).decode()

    return board

def write_answer(puzzle, solution, proc : process):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                ans = f"{row} {col} {solution[row][col]}"
                proc.sendline(ans.encode())
                
p = process("./sudoku_puzzle")
delims = "Here is your Puzzle:"
# board = get_board(p, delims)
# puzzle = sudoku.Sudoku(3, board=board)
# solution = puzzle.solve().board

for _ in range(421):
    try:
        print(f"Running game {_}")
        board = get_board(p, delims)
        puzzle = sudoku.Sudoku(3, board=board)
        solution = puzzle.solve().board
        write_answer(board, solution, p)
    except EOFError:
        perform_important_task()
        p.close()
        break
