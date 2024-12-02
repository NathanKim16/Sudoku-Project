#Imports
from random import randint, sample
import pygame
import copy
from Button import Button, boardButton
from sudoku_generator import SudokuGenerator

#ToDo List -------
#1. Cleanup win screen
#2. Cleanup lose screen
#3. Add menu buttons

def printBoard(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end = " ")
        print()

def generateBoard(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    filledBoard = copy.deepcopy(board)
    sudoku.remove_cells()
    board = sudoku.get_board()
    return filledBoard, board

def prepareTimer(time):
    time = time/60
    minutes = int(time/60)
    seconds = int(time%60)
    time = format(minutes + (seconds/100),".2f")
    time = time.replace(".", ":")
    return time

def generateVisualBoard(screen, board, screenWidth, screenHeight):
    #Define proportions
    boardLength = screenWidth*0.5
    leftBuffer = screenWidth*0.25   
    topBuffer = (screenHeight-boardLength)/2
    # Draw the board
    squares = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                squares.append(boardButton(screen,"boardButton", "", "white", leftBuffer+((boardLength/9)*j)+(boardLength/18), topBuffer+((boardLength/9)*i)+(boardLength/18), (boardLength/9), (boardLength/9), "blank", 0))
            else:
                squares.append(boardButton(screen,"boardButton", str(board[i][j]), "light gray", leftBuffer+((boardLength/9)*j)+(boardLength/18), topBuffer+((boardLength/9)*i)+(boardLength/18), (boardLength/9), (boardLength/9), "given", 0))
    return squares

def displayHelpScreen(screen, screenWidth, screenHeight):
    menuWidth = 2*(screenWidth/3)
    menuHeight = 2*(screenHeight/3)
    menuWidthBuffer = (screenWidth-menuWidth)/2
    menuHeightBuffer = (screenHeight-menuHeight)/2
    menuColor = "light blue"
    pygame.draw.rect(screen, menuColor, (menuWidthBuffer, menuHeightBuffer, menuWidth, menuHeight))
    Button(screen, "helpTitle", "How to play Sudoku", menuColor, menuWidthBuffer+200, menuHeightBuffer+50, 0, 0, 0).draw_button()
    helpText = [
        "Fill each 3 x 3 set with numbers 1–9.",
        "Each number can only appear once in each row, column, and set.",
        "Use the cursor or arrow keys to navigate the board.",
        "Click on a square to fill it with a number.",
        "Press 'Enter' to submit your entry for that square."
    ]
    for index, text in enumerate(helpText):
        helpText = Button(screen, "helpText", text, menuColor, menuWidthBuffer+(len(text)*6.5), menuHeightBuffer+120+(index*30), len(text)*11, 30, 0)
        helpText.font = pygame.font.Font(None, 30)
        helpText.prep_msg(helpText.msg)
        helpText.draw_button()
    exitHelpButton = Button(screen, "exitHelpButton","X", menuColor, menuWidthBuffer+(menuWidth-50), menuHeightBuffer+50, 30, 30, 0)
    exitHelpButton.draw_button()
    return exitHelpButton

def displayBoard(screen, screenWidth, screenHeight, squares, time):
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
    #Draw timer
    time = prepareTimer(time)
    timer = Button(screen,"timer", "Time: " + time, "white", screenWidth/2, 50, 200, 50, 0)
    timer.font = pygame.font.Font(None, 30)
    timer.prep_msg(timer.msg)
    timer.draw_button()
    #Draw help button
    helpButton = Button(screen, "helpButton", "", (255, 255, 255), screenWidth-37, 40, 23, 25, 0)
    helpButton.draw_button()
    help_image = pygame.image.load("images/help.svg")
    screen.blit(help_image, help_image.get_rect(topleft=(screenWidth-50, 25)))
    #Menu buttons
    resetButton = Button(screen, "resetButton", "Reset", (228, 8, 10), screenWidth/3, screenHeight-50, 100, 50, 10)
    restartButton = Button(screen, "restartButton", "Restart", (228, 8, 10), screenWidth/2, screenHeight-50, 150, 50, 10)
    exitButton = Button(screen, "exitButton", "Exit", (228, 8, 10), (screenWidth/3)*2, screenHeight-50, 100, 50, 10)
    resetButton.draw_button()
    restartButton.draw_button()
    exitButton.draw_button()
    return [resetButton, restartButton, exitButton, helpButton]

def displayWinScreen(screen, screenWidth, screenHeight):
    winText = Button(screen, "winText", "You win!", "white", screenWidth/2, screenHeight/3, 200, 50, 0)
    winText.text_color = "green"
    winText.font = pygame.font.Font("fonts/sourGummy.ttf", 100)
    winText.prep_msg(winText.msg)
    exitButton = Button(screen, "winExitButton", "Exit", "green", screenWidth/2, screenHeight/2, 200, 50, 10)
    winText.draw_button()
    exitButton.draw_button()
    return exitButton

def displayLoseScreen(screen, screenWidth, screenHeight):
    loseText = Button(screen, "loseText","You Lost", "white", screenWidth/2, screenHeight/3, 200, 50, 0)
    loseText.text_color = "red"
    loseText.font = pygame.font.Font("fonts/sourGummy.ttf", 100)
    loseText.prep_msg(loseText.msg)
    restartButton = Button(screen, "loseRestartButton", "Restart", (228, 8, 10), screenWidth/2, screenHeight/2, 200, 50, 10)
    loseText.draw_button()
    restartButton.draw_button()
    return restartButton

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
            print("Board Cleaned")
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
    if event.key == pygame.K_RIGHT:
        print("Pressed right")
        squareNum += 1
    if event.key == pygame.K_UP:
        print("Pressed up")
        squareNum -= 9
    if event.key == pygame.K_DOWN:
        print("Pressed down")
        squareNum += 9
    #Check if the square number is out of bounds
    if squareNum > 80:
        squareNum = squareNum - 81
    if squareNum < -80:
        squareNum = squareNum + 81
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

def eventListener(squares, buttons):
    global squareNum
    global eventType
    eventType = "none"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos() # Get the position of the mouse
            print("Clicked at: " + str(mouseX) + ", " + str(mouseY))
            #Check if a square was clicked
            squareNum = checkSquareClick(squares)
            #Check if a button in the button array was clicked
            for button in buttons:
                if button.rect.collidepoint(mouseX, mouseY):
                    print(button.msg + " button clicked")
                    eventType = (button.id).replace("Button", "")
        elif event.type == pygame.KEYDOWN:
            print("Key pressed")
            if "squareNum" not in globals() or squareNum == None:
                squareNum = 0
            #Check for arrow key presses
            squareNum = checkArrowInput(event, squares, squareNum)            
            if squares[squareNum].state != "given":
                checkNumberInput(event, squares, squareNum)
                checkNumberSubmit(event, squares, squareNum)
