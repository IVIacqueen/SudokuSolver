# Sudoku Solver
# Sudoku contain unique digits 1-9 in a 3x3 region, column, and row

NUM_OF_DIGITS = 9;
EMPTY_VALUE = "."

def main():
    
    sudoku = [["5","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]]
                
    # Master level sudoku board
    sudoku = [["5", "8", ".", ".", ".", ".", ".", "2", "4"]
                ,[".", ".", "6", ".", "4", ".", "9", ".", "."]
                ,[".", ".", "1", ".", "8", ".", "3", ".", "."]
                ,[".", ".", "2", ".", "7", ".", "8", ".", "."]
                ,[".", "1", ".", ".", ".", ".", ".", "4", "."]
                ,["8", ".", ".", "4", ".", "5", ".", ".", "7"]
                ,["1", ".", ".", "6", ".", "7", ".", ".", "9"]
                ,[".", "9", ".", ".", ".", ".", ".", "6", "."]
                ,[".", ".", "4", "8", "1", "9", "2", ".", "."]]
    

    solved_sudoku = copy_board(sudoku)

    insert_digit(solved_sudoku, 0, 0)

    display_board(solved_sudoku)


# Create a copy of the sudoku board to modify
def copy_board(sudoku):
    new_board = []
    for row in range(len(sudoku)):
        new_board.append([])
        for column in range(len(sudoku)):
            new_board[row].append(sudoku[row][column])
    return new_board

# Simpler solution
def solve_sudoku(board, row, column):
    # Goes to next row if column has reached the end
    if column == NUM_OF_DIGITS:
        column = 0
        row += 1
        # Case for when the end of the board has been reached
        if row == NUM_OF_DIGITS:
            return True

    # If the space is not empty, go to the next column
    if (board[row][column] != EMPTY_VALUE):
        return solve_sudoku(board, row, column + 1)

    # Insert digits 1-9 into the empty space
    for i in range(1, NUM_OF_DIGITS + 1):
        if is_valid_number(board, row, column, str(i)):
            board[row][column] = str(i)
            # Recursively call the function to check the next column
            if solve_sudoku(board, row, column + 1):
                return True
            # Reset the space if the digit did not work
            board[row][column] = EMPTY_VALUE
    
    return False

# Checks if a digit can be inserted inside a specific spot in the sudoku board
def is_valid_number(sudoku, row, column, digit):

    # Checks if digit is in its row
    for i in range(NUM_OF_DIGITS):
        if sudoku[row][i] == digit:
            return False

    # Checks if digit is in its column
    for i in range(NUM_OF_DIGITS):
        if sudoku[i][column] == digit:
            return False

    # Checks if digit is in its 3x3 region
    start_row = row - row%3
    start_column = column - column%3
    for i in range(3):
        for j in range(3):
            if sudoku[i + start_row][j + start_column] == digit:
                return False

    return True

# Original solution using LeetCode problem
def insert_digit(board, row, column):
    # Checks if column has reached the end of the row
    if column == NUM_OF_DIGITS:
        column = 0
        row += 1
        # Checks if the loop has reached the last index of the board
        if row == NUM_OF_DIGITS:
            return True
    
    # Only affect values that are empty in the board
    if board[row][column] == EMPTY_VALUE:
        # Test each possible digit in the empty space
        for digit in range(1, 10):
            board[row][column] = str(digit)
            # Checks if the added digit makes a solvable board
            if is_valid_sudoku(board):
                # Recursively calls the function to check the next column
                if insert_digit(board, row, column + 1):
                    return True
            # Resets space if the digit did not work
            board[row][column] = EMPTY_VALUE
    else:
        # Goes to next column if the space is not empty
        return insert_digit(board, row, column + 1)

    return False

# LeetCode problem
def is_valid_sudoku(sudoku):

    # Checking all 3x3 grid
    for i in range(0, NUM_OF_DIGITS, 3):
        for j in range(0, NUM_OF_DIGITS, 3):
            if three_by_three_section(sudoku, i, j) == False:
                return False

    # Checking all rows
    for i in range(len(sudoku)):
        if check_valid_section(sudoku[i]) == False:
            return False

    # Checking all columns
    for i in range(len(sudoku)):
        sudoku_column = []
        # create list with all the numbers in a column
        for j in range(len(sudoku)):
            sudoku_column.append(sudoku[j][i])
        # Check if the column is valid
        if check_valid_section(sudoku_column) == False:
            return False
    
    return True

def three_by_three_section(sudoku, row, column):
    # Check if the 3x3 section is valid
    section = []
    for i in range(3):
        for j in range(3):
            section.append(sudoku[row + i][column + j])
    return check_valid_section(section)

# Method to check if all elements in an array are unique digits of 1-9 (ignore ".")
def check_valid_section(section):
    count = 0
    unique_digits = set(section)
    unique_digits.discard(EMPTY_VALUE)

    for digit in section:
        if (digit != EMPTY_VALUE):
            count += 1

    return (len(unique_digits)) == count

# Display sudoku board
def display_board(sudoku):
    for i in range(len(sudoku)):
        print(sudoku[i])

if __name__ == "__main__":
    main()