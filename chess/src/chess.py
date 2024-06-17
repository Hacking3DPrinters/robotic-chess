from stockfish import Stockfish
stockfish_path="" # place path to stockfish here
class Board:
    def __init__(self,fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR',cpu=2,ram=2048):
        self.stockfish = Stockfish(path=stockfish_path, parameters={"Threads": cpu, "Hash": ram})
        if self.stockfish.is_fen_valid(fen):
            self.stockfish.set_fen_position(fen)
    def engine_skill(self,rating=3000):
        self.stockfish.set_elo_rating(rating)
    def get_piece(self,square='a1'):
        return self.stockfish.get_what_is_on_square(square)
    def get_capture(self,move='a1a2'):
        return self.stockfish.will_move_be_a_capture(move)
    def engine_move(self):
        return self.stockfish.get_best_move()
    def opponent_move(self,moves=['a1a2']):
        # multiple moves can be defined
        self.stockfish.make_moves_from_current_position(moves)
    