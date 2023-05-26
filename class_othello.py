import pickle
from constants import FILE_NAME
from utils import get_opponent, init_board


class Othello:
    def __init__(self):
        self.board = init_board()
        self.current_player = 1

    def set_loaded_game(self):
        with open(FILE_NAME, 'rb') as f1:
            board = pickle.load(f1)
        self.board = board["board"]
        self.current_player = board["current_player"]

    def switch_player(self):
        if self.current_player == 1:
            self.current_player = 0

        else:
            self.current_player = 1

    def get_possible_moves(self):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        possible_moves = []

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == '':
                    for direction in directions:
                        r, c = row + direction[0], col + direction[1]
                        if 0 <= r < len(self.board) and 0 <= c < len(self.board[row]) and self.board[r][c] == get_opponent(self.current_player):
                            r += direction[0]
                            c += direction[1]
                            while 0 <= r < len(self.board) and 0 <= c < len(self.board[row]) and self.board[r][c] == get_opponent(
                                    self.current_player):
                                r += direction[0]
                                c += direction[1]
                            if 0 <= r < len(self.board) and 0 <= c < len(self.board[row]) and self.board[r][c] == self.current_player:
                                possible_moves.append((row, col))
                                break

        return possible_moves

    def save_board(self):
        game_status = {'current_player': self.current_player, 'board': self.board}
        with open(FILE_NAME, 'wb') as f1:
            pickle.dump(game_status, f1)

    def make_move(self, row, col):
        self.board[row][col] = self.current_player
    def is_valid_move(self, row, col):
        # Vérifier si la case est vide
        if self.board[row][col] != '':
            return False

        # Liste des directions possibles
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        # Vérifier pour chaque direction
        for drow, dcol in directions:
            path_list = []
            r, c = row + drow, col + dcol
            # Vérifier si la case adjacente est occupée par l'adversaire
            if 0 <= r < len(self.board) and 0 <= c < len(self.board) and self.board[r][c] == get_opponent(self.current_player):
                path_list.append((r, c))
                # Continuer dans la direction tant qu'on rencontre des pions adverses
                r += drow
                c += dcol
                while 0 <= r < len(self.board) and 0 <= c < len(self.board) and self.board[r][c] == get_opponent(self.current_player):
                    path_list.append((r, c))
                    r += drow
                    c += dcol
                # Si on rencontre une case vide, le mouvement est valide
                if 0 <= r < len(self.board) and 0 <= c < len(self.board) and self.board[r][c] == self.current_player:
                    return True, path_list

        # Aucune direction n'a permis de capturer des pions adverses
        return False

    def count_pawn(self):
        black_pawn = 0
        white_pawn = 0
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == 0:
                    black_pawn += 1
                elif self.board[row][col] == 1:
                    white_pawn += 1
        return black_pawn, white_pawn

    def flip_tiles(self, row, col):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        flipped_tiles = []

        for direction in directions:
            r, c = row, col
            tiles_to_flip = []
            r += direction[0]
            c += direction[1]

            while 0 <= r < len(self.board) and 0 <= c < len(self.board[0]) and self.board[r][c] == get_opponent(self.current_player):
                tiles_to_flip.append((r, c))
                r += direction[0]
                c += direction[1]

                if 0 <= r < len(self.board) and 0 <= c < len(self.board[0]) and self.board[r][c] == self.current_player:
                    flipped_tiles.extend(tiles_to_flip)

        for r, c in flipped_tiles:
            self.board[r][c] = self.current_player

    def game_over(self):
        result = False
        if len(self.get_possible_moves()) == 0:
            result = True
        return result



