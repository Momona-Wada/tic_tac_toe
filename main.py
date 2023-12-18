import pygame

pygame.init()

# functions ----------------------------------------------------------------------------------------------------------
def draw_grid():
    for i in range(1, 3):
        # draw two horizontal lines in window
        pygame.draw.line(screen, BLACK, (0, i * 200), (screen_width, i * 200), width=5)
        # draw two vertical lines in window
        pygame.draw.line(screen, BLACK, (i * 200, 0), (i * 200, screen_height), width=5)


def draw_board():
    for row_index, row in enumerate(board):
        for col_index, col in enumerate(row):
            if col == 1:
                # draw ⭕️
                pygame.draw.circle(screen, RED, (col_index * 200 + 100, row_index * 200 + 100), 80, 5)
            elif col == -1:
                # draw　❌
                pygame.draw.line(screen, BLUE, (col_index * 200 + 20, row_index * 200 + 20),
                                 (col_index * 200 + 180, row_index * 200 + 180), width=5)
                pygame.draw.line(screen, BLUE, (col_index * 200 + 180, row_index * 200 + 20),
                                 (col_index * 200 + 20, row_index * 200 + 180), width=5)

# --------------------------------------------------------------------------------------------------------------------


# generate a game window
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic Tac Toe ⭕️❌")

# set colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# make a board (0: empty, 1: ⭕️, -1: ❌)
board = [[0, 0, 0], [0 , 0, 0], [0, 0, 0]]
number = 1


# event main loop ==================================================================================================
running = True
while running:

    # fill back-ground color
    screen.fill(WHITE)

    # get the cursor position
    mx, my = pygame.mouse.get_pos()
    x = mx // 200
    y = my // 200
    # print(x, y)

    # draw grid in window
    draw_grid()

    # draw board
    draw_board()

    # check winner
    for row_index, row in enumerate(board):
        # check row
        if row == 3:
            print("⭕️win!")
        if row == -3:
            print("❌win!")
        # check column
        if board[0][row_index] + board[1][row_index] + board[2][row_index] == 3:
            print("⭕️win!")
        if board[0][row_index] + board[1][row_index] + board[2][row_index] == -3:
            print("❌win!")
        # check diagonal
        if board[0][0] + board[1][1] + board[2][2] == 3 or board[0][2] + board[1][1] + board[2][0] == 3:
            print("⭕️win!")
        if board[0][0] + board[1][1] + board[2][2] == 3 or board[0][2] + board[1][1] + board[2][0] == -3:
            print("❌win!")




    # get event
    for event in pygame.event.get():
        # finish when closed button is clicked
        if event.type == pygame.QUIT:
            running = False
        # finish when esc button is clicked
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if board[y][x] == 0:
                board[y][x] = number
                number *= -1

    # update
    pygame.display.update()
# ===================================================================================================================
pygame.quit()
