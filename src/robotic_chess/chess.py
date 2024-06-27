print('Loading python-chess lib...')
import chess
print('Loading stockfish lib...')
from stockfish import Stockfish
print('Loading stockfish engine...')
stockfish_path="/usr/local/bin/stockfish" # place path to stockfish here
class Engine:
    def __init__(self,fenstr='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR',cpu=2,ram=2048):
        self.stockfish = Stockfish(path=stockfish_path, parameters={"Threads": cpu, "Hash": ram})
        if self.stockfish.is_fen_valid(fenstr):
            self.stockfish.set_fen_position(fenstr)
        self.board = chess.Board(fen=fenstr)
    def engine_skill(self,rating=3000):
        self.stockfish.set_elo_rating(rating)
    def get_piece(self,square='a1'):
        return self.stockfish.get_what_is_on_square(square)
    def get_capture(self,move='a1a2'):
        return self.stockfish.will_move_be_a_capture(move)
    def engine_move(self):
        move=self.stockfish.get_best_move())
        self.board.push_uci(move)
        return move
    def opponent_move(self,move):
        # expects an UCI string
        self.board.push_uci(move)
        self.stockfish.make_moves_from_current_position([move.uci()])
    def check_win(self):
        return self.board.outcome()

class Board(chess.Board):
    pass

class Move(chess.Move):
    pass

print('Chesslib v2')
print('MIT Licence 2024 Benjamin Porter')
