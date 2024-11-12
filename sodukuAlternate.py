from random import randint, sample
import pygame
from Button import Button
def generateBoard():
    base  = 3
    side  = base*base

    # pattern for a baseline valid solution
    def pattern(r,c): 
        num = (base*(r%base)+r//base+c)%side
        return num

    # randomize rows, columns and numbers (of valid base pattern)
    def shuffle(s):
        print(s) 
        print(sample(s,len(s)) )
        return sample(s,len(s)) 
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    # produce board using randomized baseline pattern
    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

    # remove numbers from the board to create the puzzle
    # for i in range(64):
    #     while True:
    #         row = randint(0, 8)
    #         col = randint(0, 8)
    #         if board[row][col] != ".":
    #             board[row][col] = "."
    #             break
    return board

def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end = " ")
        print()

def main():
    try:
        pygame.init()
        screenWidth = 1000
        screenHeight = 700
        screen = pygame.display.set_mode((screenWidth, screenHeight))
        clock = pygame.time.Clock()
        gameMenu = True
        while gameMenu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameMenu = False
            screen.fill("white")
            title = Button(screen, "Sudoku", ("white"), (screenWidth/2), (screenHeight/2)-250)
            easyButton = Button(screen, "Easy", (0, 255, 0), (screenWidth/2), (screenHeight/2)-75)
            mediumButton = Button(screen, "Medium", (255, 255, 0), (screenWidth/2), (screenHeight/2))            
            hardButton = Button(screen, "Hard", (255, 0, 0), (screenWidth/2), (screenHeight/2)+75)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
