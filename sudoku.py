import pygame
from Button import Button
import gameFunctions as gf

def main():
    try:
        pygame.init()
        pygame.display.set_caption('Group 115 Sudoku')
        icon = pygame.image.load("images/icon.png")
        pygame.display.set_icon(icon)

        #Initialize variables
        screenWidth = 1200 #Keeping a 2:3 aspect ratio
        screenHeight = 800
        #Phase Switches
        gameMenu = True
        inGame = False
        postGame = False
        helpMenu = False
        missingSquares = 0
        screen = pygame.display.set_mode(((screenWidth, screenHeight)))
        clock = pygame.time.Clock()
        while gameMenu or inGame or postGame:
            while gameMenu: #Main menu state
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if easyButton.rect.collidepoint(pygame.mouse.get_pos()):
                            print("Easy")
                            missingSquares = 30
                            gameMenu = False
                            inGame = True
                        elif mediumButton.rect.collidepoint(pygame.mouse.get_pos()):
                            print("Medium")
                            missingSquares = 40
                            gameMenu = False      
                            inGame = True                  
                        elif hardButton.rect.collidepoint(pygame.mouse.get_pos()):
                            print("Hard")
                            missingSquares = 50
                            gameMenu = False
                            inGame = True
                screen.fill("white")
                sudokuTitle = Button(screen,"sudokuTitle", "Sudoku", ("white"), (screenWidth/2), 150, 300, 100, 0)
                sudokuTitle.font = pygame.font.Font("fonts/sourGummy.ttf", 100)
                sudokuTitle.prep_msg(sudokuTitle.msg)
                easyButton = Button(screen,"easyButton", "Easy", (0, 255, 0), (screenWidth/2), (screenHeight/2)-75, 200, 50, 20)
                mediumButton = Button(screen,"mediumButton", "Medium", (255, 255, 0), (screenWidth/2), (screenHeight/2), 200, 50, 20)           
                hardButton = Button(screen,"hardButton", "Hard", (255, 0, 0), (screenWidth/2), (screenHeight/2)+75, 200, 50, 20)
                sudokuTitle.draw_button()
                easyButton.draw_button()
                mediumButton.draw_button()
                hardButton.draw_button()            
                pygame.display.flip()
                clock.tick(60)
            
            #Preparation for the game
            filledBoard, board = gf.generateBoard(9, missingSquares)
            gf.printBoard(filledBoard)#Prints answer key to the console
            print("")
            gf.printBoard(board)#Prints the board to the console
            print("Game Event Log:")
            squares = gf.generateVisualBoard(screen, board, screenWidth, screenHeight) #Generates the visual board with each square as an object
            gameTime = 0

            while inGame: #Game state
                buttons = []
                gameTime += 1
                screen.fill("white")
                buttons.extend(gf.displayBoard(screen, screenWidth, screenHeight, squares, gameTime))
                if helpMenu:
                    buttons.append(gf.displayHelpScreen(screen, screenWidth, screenHeight))
                gf.eventListener(squares, buttons)
                if gf.eventType == "reset":
                    print("Resetting board")
                    squares = gf.generateVisualBoard(screen, board, screenWidth, screenHeight)
                elif gf.eventType == "restart":
                    print("Restarting game")
                    gameMenu = True
                    inGame = False
                    postGame = False
                    helpMenu = False
                elif gf.eventType == "exit":
                    print("Exiting game")
                    gameMenu = False
                    inGame = False
                    postGame = False
                elif gf.eventType == "help":
                    print("Help menu")
                    helpMenu = True
                elif gf.eventType == "exitHelp":
                    print("Exiting help menu")
                    helpMenu = False
                gameState = gf.checkGameState(filledBoard, squares)                
                if gameState == "Lost" or gameState == "Won":
                    inGame = False
                    postGame = True
                pygame.display.flip()
                clock.tick(60)

            while postGame: #Post game state
                screen.fill("white")
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        postGame = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if restartButton.rect.collidepoint(pygame.mouse.get_pos()):
                            print("Restart button clicked")
                            postGame = False
                            gameMenu = True
                        elif exitButton.rect.collidepoint(pygame.mouse.get_pos()):
                            print("Exit button clicked")
                            postGame = False
                if gameState == "Lost":
                    restartButton = gf.displayLoseScreen(screen, screenWidth, screenHeight)                        
                elif gameState == "Won":
                    exitButton = gf.displayWinScreen(screen, screenWidth, screenHeight)
                pygame.display.flip()
                clock.tick(60)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
