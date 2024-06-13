import random as r

class Sudoku():

    def __init__(self, board_size):
        self.board_size = board_size
        self.difficulties = ['easy', 'medium', 'hard', 'expert']
        self.board_levels = {"easy": (36, 46), "medium": (46, 56), "hard": (56, 61), "expert": (61, 64)}
        self.user_start_board = []


    def play_sudoku(self):
        sudoku_board = self.generate_sudoku()
        difficulty = input("Choose difficulty(easy, medium, hard, expert): ")
        start = input("You can see solved sudoku puzzle by typing 'Sudoku' right now or press enter to continue.")
        if start.lower() == "sudoku":
        	self.print_board(sudoku_board)
        if difficulty in self.difficulties:
            empty_blocks = r.randint(self.board_levels[difficulty][0], self.board_levels[difficulty][1])
        else:
            raise ValueError("Invalid difficulty level. Choose from 'easy', 'medium', 'hard', 'expert'.")


        user_start_board = self.generate_difficulty_board(sudoku_board, empty_blocks)
        print("Sudoku start board:")
        self.print_board(user_start_board)

        while not self.check_full(user_start_board):
            self.user_input(user_start_board, sudoku_board)
            print("\nSudoku:")
            self.print_board(user_start_board)

        print("Congratulations! You've completed the Sudoku puzzle!")


    def generate_sudoku(self):
        board = [[0 for x in range(self.board_size + 1)] for x in range(self.board_size + 1)]
        
        self.solve_sudoku(board)

        return board


    def check_numbers(self, board, row, col, num):
            for i in range(self.board_size + 1):
                if board[row][i] == num or board[i][col] == num:
                    return False
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False
            return True


    def solve_sudoku(self, board):
        for row in range(self.board_size + 1):
            for col in range(self.board_size + 1):
                if board[row][col] == 0:
                    numbers = list(range(1, 10))
                    r.shuffle(numbers)
                    for num in numbers:
                        if self.check_numbers(board, row, col, num):
                            board[row][col] = num
                            if self.solve_sudoku(board):
                                return True
                            board[row][col] = 0
                    return False
        return True


    def print_board(self, board):
        for i in range(self.board_size + 1):
            if i % 3 == 0 and i != 0:
                print("----------------------- ")
            for j in range(self.board_size + 1):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                if j == self.board_size:
                    print(board[i][j])
                else:
                    print(str(board[i][j]) + " ", end="")


    def check_full(self, board):
        for row in range(self.board_size):
            for col in range(self.board_size):
                if board[row][col] == 0:
                    return False
        return True


    def user_input(self, board, sudoku_main_board):
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


    def generate_difficulty_board(self, board, empty_blocks):
    	count = 0
    	user_start_board = [[0 for x in range(self.board_size + 1)]for x in range(self.board_size + 1)]
    	for i in range(self.board_size + 1):
    		for j in range(self.board_size + 1):
    			user_start_board[i][j] = board[i][j]

    	while count < empty_blocks:
    		row, col = r.randint(0, self.board_size), r.randint(0, self.board_size)
    		if user_start_board[row][col] != 0:
    			user_start_board[row][col] = 0
    			count += 1

    	return user_start_board


if __name__ == "__main__":
    sudoku = Sudoku(8)
    sudoku.play_sudoku()
