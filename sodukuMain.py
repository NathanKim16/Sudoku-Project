import pygame
import copy
from Button import Button
import gameFunctions as gf

def main():
    try:
        pygame.init()
        #Initialize variables
        screenWidth = 1200 #Keeping a 2:3 aspect ratio
        screenHeight = 800
        gameMenu = True
        inGame = False
        missingSquares = 0
        screen = pygame.display.set_mode(((screenWidth, screenHeight)))
        clock = pygame.time.Clock()        
        while gameMenu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameMenu = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY = pygame.mouse.get_pos()
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
            Button(screen, "Sudoku", ("white"), (screenWidth/2), 100, 200, 50).draw_button()
            easyButton = Button(screen, "Easy", (0, 255, 0), (screenWidth/2), (screenHeight/2)-75, 200, 50)
            mediumButton = Button(screen, "Medium", (255, 255, 0), (screenWidth/2), (screenHeight/2), 200, 50)           
            hardButton = Button(screen, "Hard", (255, 0, 0), (screenWidth/2), (screenHeight/2)+75, 200, 50)
            easyButton.draw_button()
            mediumButton.draw_button()
            hardButton.draw_button()
            
            pygame.display.flip()
            clock.tick(60)
        filledBoard = gf.generateBoard()
        board = copy.deepcopy(filledBoard) #Necessary to keep the original board
        board = gf.removeNumbers(board, missingSquares)
        gf.printBoard(filledBoard)
        gf.printBoard(board)
        squares = gf.generateVisualBoard(screen, board, screenWidth, screenHeight)
        
        while inGame:
            screen.fill("white")
            gf.displayBoard(screen, board, screenWidth, screenHeight, squares)
            gf.eventListener(screen, squares)
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
