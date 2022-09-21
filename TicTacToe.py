import random

# printInt = "integer"
# printFloat = "float"
# printString = "string"
# printList = "list"
# printTuple = "tuple"
# printDictionary = "dictionary"
# printBoolean = "boolean"
#
#
# print(f"All the different data types in Python are: \n{printInt}\n{printFloat}\n{printString}\n{printList}\n{printTuple}\n{printDictionary}\n{printBoolean}")

# alphabet = "abcdefghijklmnopqrstuvwxyz"
#
# search = input("Input a random integer (1-26): ")
# if int(search) > 26 or int(search) < 1:
#     exit("Invalid input. Try again.")
#
# search = int(search)
#
# if (search >= 21 and search % 10 == 1) or search == 1:
#     print(alphabet[search - 1] + " is the " + str(search) + "st letter in the English alphabet.")
# elif (search >= 21 and search % 10 == 2) or search == 2:
#     print(alphabet[search - 1] + " is the " + str(search) + "nd letter in the English alphabet.")
# elif (search >= 21 and search % 10 == 2) or search == 3:
#     print(alphabet[search - 1] + " is the " + str(search) + "rd letter in the English alphabet.")
# else:
#     print(alphabet[search - 1] + " is the " + str(search) + "th letter in the English alphabet.")

tictactoe = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]


def rowChecker(row):
    while row > 2 or row < 0:
        row = int(input("Invalid row. Enter new row: "))

    return row


def colChecker(col):
    while col > 2 or col < 0:
        col = int(input("Invalid column. Enter new column: "))

    return col


def spotTaken(row, col):
    if tictactoe[row][col] != "-":
        return True
    else:
        return False
        # row = rowChecker(int(input("Input new row: ")))
        # col = colChecker(int(input("Input new col: ")))


def horizontalWin(tictactoe):
    win = False
    for row in range(len(tictactoe)):
        str = ""
        for col in range(len(tictactoe[0])):
            str = str + tictactoe[row][col]
        if str == "XXX" or str == "YYY":
            win = True

    return win

def verticalWin(tictactoe):
    win = False
    for col in range(len(tictactoe[0])):
        str = ""
        for row in range(len(tictactoe)):
            str = str + tictactoe[row][col]
        if str == "XXX" or str == "YYY":
            win = True

    return win

def diagonalWin(tictactoe):
    str = ""
    win = False
    for row in range(len(tictactoe)):
        for col in range(len(tictactoe[0])):
            if row == col:
                str = str + tictactoe[row][col]
        if str == "XXX" or str == "YYY":
            win = True

    str = tictactoe[2][0] + tictactoe[1][1] + tictactoe[0][2]
    if str == "XXX" or str == "YYY":
        win = True

    return win


print("Welcome to TicTacToe. Here is your board: ")

# Tictactoe printer
for x in range(len(tictactoe)):
    for y in range(len(tictactoe[0])):
        print(tictactoe[x][y] + "\t", end="")
    print("")

print("Let us roll a dice to decide who goes first.")

turnDecider = random.randint(0, 10)
currentTurn = None
turnCounter = 0
placeTaken = False

if turnDecider % 2 == 1:
    currentTurn = 1
    print("Player X begins. Lucky you!")
elif turnDecider % 2 == 0:
    currentTurn = 2
    print("Player Y begins. Lucky you! \n")

for turnCounter in range(9):
    # Player X Input
    if currentTurn % 2 == 1:
        print("\nPlayer X:")
        row = rowChecker(int(input("Please choose a row: ")))
        col = colChecker(int(input("Please choose a column: ")))

        while spotTaken(row, col):
            print("Spot is taken.")
            row = rowChecker(int(input("Please choose a row: ")))
            col = colChecker(int(input("Please choose a column: ")))

        tictactoe[row][col] = "X"
        currentTurn = currentTurn + 1
        turnCounter = turnCounter + 1
    # Player Y Input
    elif currentTurn % 2 == 0:
        print("\nPlayer Y:")
        row = rowChecker(int(input("Please choose a row: ")))
        col = rowChecker(int(input("Please choose a column: ")))

        while spotTaken(row, col):
            print("Spot is taken.")
            row = rowChecker(int(input("Please choose a row: ")))
            col = colChecker(int(input("Please choose a column: ")))

        tictactoe[row][col] = "Y"
        currentTurn = currentTurn - 1
        turnCounter = turnCounter + 1

    # Tictactoe printer
    for x in range(len(tictactoe)):
        for y in range(len(tictactoe[0])):
            print(tictactoe[x][y] + "\t", end="")
        print("")

    if horizontalWin(tictactoe) or verticalWin(tictactoe) or diagonalWin(tictactoe):
        if currentTurn == 1:
            print("Player Y wins!")
            exit()
        elif currentTurn == 2:
            print("Player X wins!")
            exit()

    if turnCounter == 9:
        print("It ends in a draw!")
        exit()