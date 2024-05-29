import random


def play_sudoku():
    sudoku_board = generate_sudoku()
    difficulty = input("Choose difficulty(easy, medium, hard, expert): ")
    start = input("You can see solved sudoku puzzle by typing 'Sudoku' right now or press enter to continue.")
    if start.lower() == "sudoku":
    	print_board(sudoku_board)
    if difficulty == 'easy':
        empty_blocks = random.randint(36, 46)
    elif difficulty == 'medium':
        empty_blocks = random.randint(46, 56)
    elif difficulty == 'hard':
        empty_blocks = random.randint(56, 61)
    elif difficulty == 'expert':
        empty_blocks = random.randint(61, 64)
    else:
        raise ValueError("Invalid difficulty level. Choose from 'easy', 'medium', 'hard', 'expert'.")

    user_start_board = generate_difficulty_board(sudoku_board, empty_blocks)
    print("Sudoku start board:")
    print_board(user_start_board)

    while not check_full(user_start_board):
        user_input(user_start_board, sudoku_board)
        print("\nSudoku:")
        print_board(user_start_board)

    print("Congratulations! You've completed the Sudoku puzzle!")


def generate_sudoku():
    board = [[0 for x in range(9)] for x in range(9)]
    
    solve_sudoku(board)

    return board


def check_numbers(board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        return True


def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                numbers = list(range(1, 10))
                random.shuffle(numbers)
                for num in numbers:
                    if check_numbers(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("----------------------- ")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def check_full(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return False
    return True


def user_input(board, sudoku_main_board):
    while True:
        try:
            row, col, num = map(int, input("\nEnter row, column and number (1-9) separated by spaces: ").split())
            if row < 1 or row > 9 or col < 1 or col > 9 or num < 1 or num > 9:
                print("Invalid input. Please enter numbers between 1 and 9.")
                continue
            if board[row-1][col-1] != 0:
                print("Cell is already filled. Choose another cell.")
                continue
            if sudoku_main_board[row-1][col-1] == num:
            	board[row-1][col-1] = num
            	break
            else:
            	print("Nice try, but it is incorrect answer.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")


def generate_difficulty_board(board, empty_blocks):
	count = 0
	user_start_board = [[0 for x in range(9)]for x in range(9)]
	for i in range(9):
		for j in range(9):
			user_start_board[i][j] = board[i][j]

	while count < empty_blocks:
		row, col = random.randint(0, 8), random.randint(0, 8)
		if user_start_board[row][col] != 0:
			user_start_board[row][col] = 0
			count += 1

	return user_start_board


if __name__ == "__main__":
	play_sudoku()
