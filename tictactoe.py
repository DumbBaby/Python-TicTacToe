board = ([0, 0, 0],
        [0, 0, 0],
        [0, 0, 0])
play = True
print("Tic Tac Toe!")
print("Enter a number corresponding to the square you would like to move!")
print("1 2 3")
print("4 5 6")
print("7 8 9")
def wincheck():
    for i in range(3):
        if((board[i][0] and board[i][1] and board[i][2] == 1) and board[i][0] + board[i][1] + board[i][2] == 3):
            return("1win")
        if((board[0][i] and board[1][i] and board[2][i] == 1) and board[0][i] + board[1][i] + board[2][i] == 3):
            return("1win")
        if((board[0][0] and board[1][1] and board[2][2] == 1) and board[0][0] + board[1][1] + board[2][2] == 3):
            return("1win")
        if((board[0][2] and board[1][1] and board[2][0] == 1) and board[0][2] + board[1][1] + board[2][0] == 3):
            return("1win")
        if((board[i][0] and board[i][1] and board[i][2] == 2) and board[i][0] + board[i][1] + board[i][2] == 6):
            return("2win")
        if((board[0][i] and board[1][i] and board[2][i] == 2) and board[0][i] + board[1][i] + board[2][i] == 6):
            return("2win")
        if((board[0][0] and board[1][1] and board[2][2] == 2) and board[0][0] + board[1][1] + board[2][2] == 6):
            return("2win")
        if((board[0][2] and board[1][1] and board[2][0] == 2) and board[0][2] + board[1][1] + board[2][0] == 6):
            return("2win")
    if(board[0].count(0) == 0 and board[1].count(0) == 0 and board[2].count(0) == 0):
        return("draw")
def printboard():
    def num2let(num):
        if num == 0:
            return("[ ]")
        if num == 1:
            return("[O]")
        if num == 2:
            return("[X]")
    row0 = str(num2let(board[0][0])) + str(num2let(board[0][1])) + str(num2let(board[0][2]))
    row1 = str(num2let(board[1][0])) + str(num2let(board[1][1])) + str(num2let(board[1][2]))
    row2 = str(num2let(board[2][0])) + str(num2let(board[2][1])) + str(num2let(board[2][2]))
    print(row0)
    print(row1)
    print(row2)
while play == True:
    validinput = False
    while validinput == False and play == True:
        play1m = int(input("Which square would you like to move to? "))
        for i in range(9):
            if i < 3:
                row = 0
            if i > 2 and i < 6:
                row = 1
            if i > 5:
                row = 2
            if play1m == i+1 and board[row][((i + 1) % 3) - 1] == 0:
                board[row][((i + 1) % 3) - 1] = 1
                if wincheck() == "1win":
                    print("O wins!")
                    play = False
                    break
                if wincheck() == "draw":
                    print("Draw!")
                    play = False
                    break
                validinput = True
    printboard()
    validinput = False
    while validinput == False and play == True:
        play2m = int(input("Which square would you like to move to? "))
        for i in range(9):
            if i < 3:
                row = 0
            if i > 2 and i < 6:
                row = 1
            if i > 5:
                row = 2
            if play2m == i+1 and board[row][((i + 1) % 3) - 1] == 0:
                board[row][((i + 1) % 3) - 1] = 2
                if wincheck() == "2win":
                    print("X wins!")
                    play = False
                    break
                if wincheck() == "draw":
                    print("Draw!")
                    play = False
                    break
                validinput = True
    printboard()