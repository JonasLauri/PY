#! /usr/bin/env python3
# Game Tic Tac Toe
import random, copy

board = {"top-L": "", "top-M": "", "top-R": "",
         "mid-L": "", "mid-M": "", "mid-R": "",
         "low-L": "", "low-M": "", "low-R": ""
         }

def printBoard(board):
    #Prints out the board
    print(board["top-L"] + " | " + board["top-M"] + " | " + board["top-R"])
    print("-------")
    print(board["mid-L"] + " | " + board["mid-M"] + " | " + board["mid-R"])
    print("-------")
    print(board["low-L"] + " | " + board["low-M"] + " | " + board["low-R"])

    
def inputPlayerLetter():
    #The player choose which letter they want to be
    letter = ""
    while not(letter == "X" or letter == "O"):
        print("Do you want to be X or O?")
        letter = input().upper()
    #Then return player and computer data set
    if letter == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]


def whoGoesFirst():
    #Randomly choose how goes first
    if random.randint(0, 1) == 0:
        return "computer"
    else:
        return "player"


def playAgain():
    #Return True if yes or False if no
    print("Do you want play again? (yes or no)")
    return input().lower().startswith('y')


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
    return ((bo["top-R"] == le and bo["top-M"] == le and bo["top-L"] == le) or
            (bo["mid-R"] == le and bo["mid-M"] == le and bo["mid-L"] == le) or
            (bo["low-R"] == le and bo["low-M"] == le and bo["low-L"] == le) or
            (bo["top-R"] == le and bo["mid-R"] == le and bo["low-R"] == le) or
            (bo["top-M"] == le and bo["mid-M"] == le and bo["low-M"] == le) or
            (bo["top-L"] == le and bo["mid-L"] == le and bo["low-L"] == le) or
            (bo["top-R"] == le and bo["mid-M"] == le and bo["low-L"] == le) or
            (bo["top-L"] == le and bo["mid-M"] == le and bo["low-R"] == le))


def getBoardCopy(board):
    #Making dublicate board
    copyBoard = copy.copy(board)
    return copyBoard


def isSpaceFree(board, move):
    #Checking if space is free
    return board[move] == ""


def getPlayerMove(board):
    move = ""
    while move not in "top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R".split() or not isSpaceFree(board, move):
        print("What is your next move? top-, mid-, low- & L, M, R")
        move = input()
    return move


def chooseRandomMoveFromList(board, movesList):
    #Returning possible moves and make random move
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):
    #Computers turn
    if computerLetter == "X":
        playerLetter = "O"
    else:
        playerLetter = "X"
        
    #If can win next move
    for i in board.keys():
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
            
    #If player can win in one move
    for i in board.keys():
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    #Try to take one of the corners
    move = chooseRandomMoveFromList(board, ["top-L", "top-R", "low-L", "low-R"])
    if move != None:
        return move

    #Try to take center
    if isSpaceFree(board, "mid-M"):
        return "mid-M"

    #Take that's left - sides
    chooseRandomMoveFromList(board, ["top-M", "mid-L", "mid-R", "low-M"])


def isBoardFull(board):
    #Checking boards fullness
    for i in board.keys():
        if isSpaceFree(board, i):
            return False
    return True

#Begining the game
print("Welcome to tic tac toe!")

while True:
    #Start
    theBoard = {"top-L": "", "top-M": "", "top-R": "",
         "mid-L": "", "mid-M": "", "mid-R": "",
         "low-L": "", "low-M": "", "low-R": ""
         }
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print("The " + turn + " goes first")
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == "player":
            #Players turn
            printBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            if isWinner(theBoard, playerLetter): #Check for win
                printBoard(theBoard)
                print("You win the game!")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard): #Check for tie
                    printBoard(theBoard)
                    print("The game is tie!")
                    break
                else:
                    turn = "computer"
                    
        else:
            #Computers turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter): #Check for win
                printBoard(theBoard)
                print("Computer beats you, you lost!")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard): #Check for tie
                    printBoard(theBoard)
                    print("The game is tie!")
                    break
                else:
                    turn = "player"

    if not playAgain():
        #Terminate a game
        break
