from fltk import *
from constants import DIMENSION, WINDOW_WIDTH, WINDOW_LENGTH, WIDTH, LENGTH
from utils import convert_coordinates


def button(text, ax, ay, bx, by):
    rectangle(ax, ay, bx, by, 'Green', 'Green')
    len_text = len(text)
    texte((bx - ax) / 2 + ax - (len_text * 6), (by - ay) / 2 + ay - len_text, text, 'black', "nw", "Helvetica", 20)
    mise_a_jour()


def error_message(x, y, text):
    texte(x, y, text, "Red", "nw", "Helvetica", 24, 'erreur')
    mise_a_jour()


def delete_error_messages():
    efface('erreur')
    efface("possible_moves")
    efface('count_pawn')
    mise_a_jour()


def print_placed_pawns(number_pawn):
    cercle(300, 850, 40, 'black', 'black')
    cercle(570, 850, 40, 'white', 'white')
    texte(200, 900, f'Pions noirs  : {number_pawn[0]}      Pions blancs : {number_pawn[1]}', "black", "nw", "Helvetica",
          24,
          'count_pawn')
    mise_a_jour()


def print_winner(number_pawn):
    cree_fenetre(WIDTH, LENGTH)
    rectangle(0, 0, WIDTH, LENGTH, 'green', 'green')
    if number_pawn[0] > number_pawn[1]:
        texte(250, 400, "Les noirs ont gagnés", "Black", "nw", "Helvetica", 24)
    else:
        texte(250, 400, "Les blancs ont gagnés ", "White", "nw", "Helvetica", 24)
        print(number_pawn)
        print_placed_pawns(number_pawn)
    mise_a_jour()


def draw_page():
    cree_fenetre(WINDOW_WIDTH, WINDOW_LENGTH)
    rectangle(0, WINDOW_WIDTH, WINDOW_LENGTH, 0, 'green', 'green')
    draw_grid()
    texte(860, 25, 'TOUR', 'black', "nw", "Helvetica", 20)
    button('Sauver', 800, 240, 980, 200)
    mise_a_jour()


def draw_grid():
    for i in range(DIMENSION):
        ligne(0, (WIDTH / DIMENSION) * i, LENGTH, (WIDTH / DIMENSION) * i, 'white')
        ligne((LENGTH / DIMENSION) * i, 0, (LENGTH / DIMENSION) * i, WIDTH, 'white')
    mise_a_jour()


def print_possible_moves(possible_moves):
    for i in range(len(possible_moves)):
        x, y = convert_coordinates(possible_moves[i][1], possible_moves[i][0])
        cercle(x, y, 10, 'red', 'red', 1, 'possible_moves')
        mise_a_jour()


def print_table(board, row, col):
    for i in range(row):
        for j in range(col):
            if board[i][j] == 0:
                x, y = convert_coordinates(j, i)
                cercle(x, y, 40, 'black', 'black')
            if board[i][j] == 1:
                x, y = convert_coordinates(j, i)
                cercle(x, y, 40, 'white', 'white')
    mise_a_jour()


def print_current_player(current_player):
    if current_player == 0:
        cercle(900, 100, 40, 'black', 'black')
    else:
        cercle(900, 100, 40, 'white', 'white')
    mise_a_jour()


def print_board_game(board, number_pawn, current_player, possible_moves):
    print_placed_pawns(number_pawn)
    print_current_player(current_player)
    print_table(board, DIMENSION, DIMENSION)
    print_possible_moves(possible_moves)
    mise_a_jour()
