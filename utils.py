from constants import CELL_SIZE


def init_board():
    board = [[''] * 8 for _ in range(8)]
    board[3][3] = 0
    board[3][4] = 1
    board[4][3] = 1
    board[4][4] = 0
    return board


def convert_coordinates(matrix_x, matrix_y):
    window_x = ((matrix_x + 1) * CELL_SIZE - CELL_SIZE / 2)
    window_y = ((matrix_y + 1) * CELL_SIZE - CELL_SIZE / 2)
    return window_x, window_y


def convert_postion(click_x, click_y):
    x = 0
    y = 0
    for i in range(9):
        if click_x <= i * 100:
            x = i - 1
            break
    for j in range(9):
        if click_y <= j * 100:
            y = j - 1
            break
    return x, y


def get_opponent(player):
    return 0 if player == 1 else 1


def is_in_button(ax, ay, bx, by, coord_click):
    if (bx > coord_click[0] > ax) and (ay > coord_click[1] > by):
        return True
