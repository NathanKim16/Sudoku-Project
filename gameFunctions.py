#Imports
from random import randint, sample
import pygame
from Button import Button, boardButton

#ToDo List -------
#1. Cleanup win screen
#2. Cleanup lose screen
#3. Add menu buttons

def printBoard(board):
    for i in range(9):
        for j in range(9):
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
                squares.append(boardButton(screen, "", "white", leftBuffer+((boardLength/9)*j)+(boardLength/18), topBuffer+((boardLength/9)*i)+(boardLength/18), (boardLength/9), (boardLength/9), "blank"))
            else:
                squares.append(boardButton(screen, str(board[i][j]), "light gray", leftBuffer+((boardLength/9)*j)+(boardLength/18), topBuffer+((boardLength/9)*i)+(boardLength/18), (boardLength/9), (boardLength/9), "given"))
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
    #TODO: Draw the menu buttons

def displayWinScreen(screen, screenWidth, screenHeight):
    Button(screen, "You win!", "green", screenWidth/2, screenHeight/2, 200, 50).draw_button()

def displayLoseScreen(screen, screenWidth, screenHeight):
    Button(screen, "You lose!", "red", screenWidth/2, screenHeight/2, 200, 50).draw_button()

def updateSelectedSquare(squares, squareNum):
    #Clear any previously selected squares
    for j in range(81):
        if squares[j].state == "given":
            squares[j].button_color = "light gray"
            squares[j].prep_msg(squares[j].msg)
        if squares[j].state == "blank":
            squares[j].button_color = "white"
        if squares[j].state == "filled" or squares[j].state == "sketched":
            squares[j].button_color = "white"
            squares[j].prep_msg(squares[j].msg)
            print("Fixed square number: " + str(squares[j].msg))
    #Set the selected square        
    squares[squareNum].button_color = (240, 220, 120)
    squares[squareNum].prep_msg(squares[squareNum].msg)#Corrects the rendered color around the number
        
def prepareNumberInput(squares, squareNum, number):
    squares[squareNum].msg = str(number)
    squares[squareNum].text_color = "dark gray"
    squares[squareNum].prep_msg(str(number))
    squares[squareNum].state = "sketched"

def checkSquareClick(squares):
    for i in range(81):
        if squares[i].rect.collidepoint(pygame.mouse.get_pos()):
            print("Clicked on square: " + str(i))
            updateSelectedSquare(squares, i)
            return i
        
def checkNumberSubmit(event, squares, squareNum):
    if event.key == pygame.K_RETURN:
        print("Submitted number")
        squares[squareNum].state = "filled"
        squares[squareNum].text_color = "black"
        squares[squareNum].prep_msg(str(squares[squareNum].msg))


def checkNumberInput(event, squares, squareNum):
    if event.key == pygame.K_1:
        print("Pressed 1")
        prepareNumberInput(squares, squareNum, 1)
    elif event.key == pygame.K_2:
        print("Pressed 2")
        prepareNumberInput(squares, squareNum, 2)
    elif event.key == pygame.K_3:
        print("Pressed 3")
        prepareNumberInput(squares, squareNum, 3)
    elif event.key == pygame.K_4:
        print("Pressed 4")
        prepareNumberInput(squares, squareNum, 4)
    elif event.key == pygame.K_5:
        print("Pressed 5")
        prepareNumberInput(squares, squareNum, 5)
    elif event.key == pygame.K_6:
        print("Pressed 6")
        prepareNumberInput(squares, squareNum, 6)
    elif event.key == pygame.K_7:
        print("Pressed 7")
        prepareNumberInput(squares, squareNum, 7)
    elif event.key == pygame.K_8:
        print("Pressed 8")
        prepareNumberInput(squares, squareNum, 8)
    elif event.key == pygame.K_9:
        print("Pressed 9")
        prepareNumberInput(squares, squareNum, 9)

def checkArrowInput(event, squares, squareNum):
    if event.key == pygame.K_LEFT:
        print("Pressed left")
        squareNum -= 1
        updateSelectedSquare(squares, squareNum)
    if event.key == pygame.K_RIGHT:
        print("Pressed right")
        squareNum += 1
        updateSelectedSquare(squares, squareNum)
    if event.key == pygame.K_UP:
        print("Pressed up")
        squareNum -= 9
        updateSelectedSquare(squares, squareNum)
    if event.key == pygame.K_DOWN:
        print("Pressed down")
        squareNum += 9
        updateSelectedSquare(squares, squareNum)
    return squareNum

def checkGameState(board, squares):
    count = 0
    for i in range(81):
        if squares[i].state == "blank" or squares[i].state == "sketched":
            count += 1
    if count == 0:
        print("Board filled")
        for i in range(81):
            if int(squares[i].msg) != board[i//9][i%9]:
                return "Lost"           
        return "Won"

def eventListener(screen, squares):
    global squareNum
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos() # Get the position of the mouse
            print("Clicked at: " + str(mouseX) + ", " + str(mouseY))
            #Check if a square was clicked
            squareNum = checkSquareClick(squares)
            #Check if a menu button was clicked
            #TODO: if button.rect.collidepoint(pygame.mouse.get_pos()):
        elif event.type == pygame.KEYDOWN:
            print("Key pressed")
            if "squareNum" not in globals():
                squareNum = 0
            #Check for arrow key presses
            squareNum = checkArrowInput(event, squares, squareNum)
            checkNumberSubmit(event, squares, squareNum)
            if squares[squareNum].state != "given":
                checkNumberInput(event, squares, squareNum)