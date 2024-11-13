#Imports
from random import randint, sample
import pygame
from Button import Button

def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end = " ")
        print()

def generateBoard():
    base = 3
    side = base*base

    # pattern for a baseline valid solution
    def pattern(r,c): 
        num = (base*(r%base)+r//base+c)%side
        return num
    # randomize rows, columns and numbers (of valid base pattern)
    def shuffle(s):
        return sample(s,len(s)) 
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    # produce board using randomized baseline pattern
    filledBoard = [[nums[pattern(r,c)] for c in cols] for r in rows ]
    return filledBoard

def removeNumbers(board, missingSquares):
    # remove numbers from the board to create the puzzle
    for i in range(missingSquares):
        while True:
            row = randint(0, 8)
            col = randint(0, 8)
            if board[row][col] != ".":
                board[row][col] = "."
                break
    return board

def generateVisualBoard(screen, board, screenWidth, screenHeight):
    #Define proportions
    boardLength = screenWidth*0.5
    leftBuffer = screenWidth*0.25   
    topBuffer = (screenHeight-boardLength)/2
    # Draw the board
    squares = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                squares.append(Button(screen, " ", "white", leftBuffer+((boardLength/9)*j)+(boardLength/18), topBuffer+((boardLength/9)*i)+(boardLength/18), (boardLength/9), (boardLength/9)))
            else:
                squares.append(Button(screen, str(board[i][j]), "light gray", leftBuffer+((boardLength/9)*j)+(boardLength/18), topBuffer+((boardLength/9)*i)+(boardLength/18), (boardLength/9), (boardLength/9)))
    return squares

def displayBoard(screen, board, screenWidth, screenHeight, squares):
    #Define proportions
    boardLength = screenWidth*0.5
    leftBuffer = screenWidth*0.25   
    topBuffer = (screenHeight-boardLength)/2 
    #Draw numbers
    for i in range(81):
        squares[i].draw_button()        
    #Draw innermost lines
    for y in range(1, 9):
        #Horizontal lines
        pygame.draw.line(screen, "gray", (leftBuffer, topBuffer+(boardLength/9)*y), ((leftBuffer+boardLength)-1, topBuffer+(boardLength/9)*y), 1)
        #Vertical lines
        pygame.draw.line(screen, "gray", (leftBuffer+(boardLength/9)*y, topBuffer), (leftBuffer+(boardLength/9)*y, (topBuffer+boardLength)-1), 1)
    #Draw inner lines
    pygame.draw.line(screen, "dark gray", (leftBuffer, topBuffer+(boardLength/3)), ((leftBuffer+boardLength)-1, topBuffer+(boardLength/3)), 3)
    pygame.draw.line(screen, "dark gray", (leftBuffer, topBuffer+(boardLength/3)*2), ((leftBuffer+boardLength)-1, topBuffer+(boardLength/3)*2), 3)
    pygame.draw.line(screen, "dark gray", (leftBuffer+(boardLength/3), topBuffer), (leftBuffer+(boardLength/3), (topBuffer+boardLength)-1), 3)
    pygame.draw.line(screen, "dark gray", (leftBuffer+(boardLength/3)*2, topBuffer), (leftBuffer+(boardLength/3)*2, (topBuffer+boardLength)-1), 3)
    #Draw outer lines
    pygame.draw.rect(screen, "black", (leftBuffer-2, topBuffer-2, boardLength+8, boardLength+8), 5)
    

def checkSquareClick(squares):
    for i in range(81):
        if squares[i].rect.collidepoint(pygame.mouse.get_pos()):
            print("Clicked on square: " + str(i))
            if squares[i].msg == " ":
                squares[i].button_color = (240, 220, 120)
            # squares[i].text_color = (240, 220, 120)
            return squares

def eventListener(screen, squares):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            print("Clicked at: " + str(mouseX) + ", " + str(mouseY))
            squares = checkSquareClick(squares)
