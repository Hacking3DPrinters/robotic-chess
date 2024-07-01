print('Loading python-chess lib...')
import chess
print('Loading stockfish lib...')
from stockfish import Stockfish
print('Loading stockfish engine...')
import getpass
import platform
if platform.system()=='Linux':
    stockfish_path="/usr/local/bin/stockfish" # place path to stockfish here
elif platform.system()=='Windows':
    stockfish_path="C:/Users/"+str(getpass.getuser())+"/stockfish"
else:
    raise OSError('Unsupported OS')
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
        move=self.stockfish.get_best_move()
        self.board.push_uci(move)
        self.stockfish.make_moves_from_current_position([move])
        return move
    def opponent_move(self,move):
        # expects an UCI string
        self.board.push_uci(move)
        self.stockfish.make_moves_from_current_position([move])
    def check_win(self):
        return self.board.is_game_over()

class Board(chess.Board):
    pass

class Move(chess.Move):
    pass

print('Chesslib v2')
print('MIT Licence 2024 Benjamin Porter')
