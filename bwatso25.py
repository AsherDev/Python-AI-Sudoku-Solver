#2-Dimensional Array that holds a hardcoded Sudoku puzzle
board = [
    [9,0,0,1,7,0,4,0,2],
    [1,6,0,0,4,0,0,9,5],
    [0,0,8,0,0,3,0,0,0],
    [0,1,0,9,0,0,5,7,3],
    [0,4,0,0,0,0,0,2,0],
    [5,8,9,0,0,7,0,1,0],
    [0,0,0,4,0,0,7,0,0],
    [6,7,0,0,2,0,0,5,8],
    [3,0,1,0,5,8,0,0,6]
]

#Function to print the sudoku board to the user
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end = "")

#Function that returns the row and column of an empty space, if there are no empty spaces it returns None
def find_empty(board):
    #For each row
    for i in range(len(board)):
        #for each column
        for j in range(len(board[0])):
            #If empty
            if board[i][j] == 0:
                #return value
                return (i, j)
    #There are no empty spaces
    return None

#Function that returns True or False based on whether or not a number in a position is valid based on Sudoku rules (only 1 of each number can exist in a row/column/3x3-square)
def valid(board, number, position):
    #Check current row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False
    #Check current Column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False
    
    #Check 3x3 square
    square_column = position[1] // 3
    square_row = position[0] // 3

    for i in range(square_row*3, square_row*3 + 3):
        for j in range(square_column * 3, square_column*3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False
    return True

#Recursive Function that implements the Depth-First-Search algorithm to find the solution. Returns True if solution is found, False otherwise
def solve(board):
    empty_space = find_empty(board)
    #If there is no empty space on the board then we have found the solution
    if not empty_space:
        return True
    else:
        row, column = empty_space
    #Try numbers 1-9 in the empty space
    for i in range(1,10):
        #Check if the current number is valid number, if it is valid, enter the number into the empty space
        if valid(board, i, (row, column)):
            board[row][column] = i

            #Solve the new board with the new number
            if solve(board):
                return True
            
            #If the solution isnt valid, reset the value
            board[row][column] = 0
    #return false if the solution is wrong
    return False

#Main Function
def main():
    print("\nCOSC350 PROGRAMMING ASSIGNMENT 2- Python Sudoku Solver\n")

    print("AUTHOR: Bryce Watson\n")
    print("STUDENT NUMBER: 220199390\n")
    print("UNE Account name: bwatso25\n")

    print("ABOUT THE PROGRAM: When run, this program takes a hardcoded sudoku puzzle as a 2-Dimensional array and solves it using a Depth-First-Search algorithm.\n")

    print("HOW THE ALGORITHM WORKS: The program finds an empty space on the board (0) by searching each row from left to right. e.g if the first row has no empty spaces then it moves to row 2.") 
    print("Once it finds an empty space, it tries numbers from 1-9 until it finds a number that appears to fit. Once it finds a number that appears to work, it moves on to the next empty space. If a valid number for the next space cannot be found,")
    print("It backtracks to the previous space and continues trying numbers for that previous space. Once it finds another number that works for the previous space, it continues onto the next space. This repeats for the entire board until a solution is found.\n")

    print("\nSodoku Puzzle:\n")
    print_board(board)

    print("\nSolving the Puzzle...\n")
    solve(board)

    print("\nSolved Sudoku Puzzle:\n")
    print_board(board)

if __name__ == "__main__":
    main()