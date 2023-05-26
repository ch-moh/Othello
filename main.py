from fltk import *
from class_othello import Othello
from graphics import print_current_player, print_possible_moves, print_table, draw_page, print_placed_pawns, \
    delete_error_messages, print_board_game, error_message, print_winner
from utils import convert_postion, is_in_button


def play(load=False):
    draw_page()
    game = Othello()
    if load:
        game.set_loaded_game()
    print_current_player(game.current_player)
    while not game.game_over():

        ev = donne_ev()
        tev = type_ev(ev)

        print_board_game(game.board, game.count_pawn(), game.current_player, game.get_possible_moves())

        if tev == "ClicGauche":

            click_x = abscisse(ev)
            click_y = ordonnee(ev)

            if is_in_button(850, 240, 980, 200, (click_x, click_y)):
                game.save_board()
                ferme_fenetre()
            row = int(convert_postion(click_x, click_y)[1])
            col = int(convert_postion(click_x, click_y)[0])
            if game.is_valid_move(row, col):
                delete_error_messages()
                game.make_move(row, col)
                game.flip_tiles(row, col)
                game.switch_player()

            else:
                error_message(250, 950, "Mouvement invalide! Réessayez.")
        if tev == 'Quitte':  # on sort de la boucle
            ferme_fenetre()
    attente(1)
    ferme_fenetre()
    print_winner(game.count_pawn())
    attend_fermeture()
