from robotic_chess.chess import Board # import chess lib
from robotic_chess.gcode import Parser # import gcode lib
import robotic_chess.octoprint # import printer lib
# main code goes here

def letter_to_number(letter): # convert chess columns (a-h) to numbers (1-8)
  if letter=='a':
    return 1
  elif letter=='b':
    return 2
  elif letter=='c':
    return 3
  elif letter=='d':
    return 4
  elif letter=='e':
    return 5
  elif letter=='f':
    return 6
  elif letter=='g':
    return 7
  elif letter=='h':
    return 8
    
def notation_to_coords(move='a1a2'): # use complex function to convert a square-square move to [[coordx,coordy],[coordx,coordy]] format
  return [[15.9375+((letter_to_number(move[0:1])-1)*31.875),15.9375+((int(move[1:2])-1)*31.875)],[15.9375+((letter_to_number(move[2:3])-1)*31.875),15.9375+((int(move[3:4])-1)*31.875)]]

def human_move():
  while True:
    		h_move = str(input('Input move: '))
    		if len(h_move)==4:
      		break
      print('Input invalid. Should be formatted as [start][end], 	e.g. a1a2 for square a1 to square a2')
    return h_move

def computer_move(board):
	best_move = board.computer_move()
	best_move_coords = notation_to_coords(move=best_move)
	if get_capture(best_move):
		capture_coords={'x':best_move_coords[1][0],'y':best_move_coords[1][1],'z':piece_height}
		printer.run_gcode(p.add_movement(z=20, speed=1000))
		printer.run_gcode(p.add_movement(x=capture_coords['x'], y=capture_coords['y'], z=capture_coords['z'], speed=500))
		printer.run_gcode(p.add_fan())
		printer.run_gcode(p.add_movement(z=20, speed=1000))
		# move to bin
		printer.run_gcode(p.add_fan(speed=0))
		printer.run_gcode(p.add_home())
	printer.run_gcode(p.add_movement(x=best_move_coords[0][0], y=best_move_coords[0][1], z=piece_height, speed=500))
	printer.run_gcode(p.add_fan())
	printer.run_gcode(p.add_movement(z=20, speed=1000))
	printer.run_gcode(p.add_movement(x=best_move_coords[1][0], y=best_move_coords[1][1], z=piece_height, speed=500))
	printer.run_gcode(p.add_fan(speed=0))
	printer.run_gcode(p.add_home())

b = Board() # initialise classes
p = Parser()
printer = robotic_chess.octoprint.Printer()

piece_height = 100 # define piece height in mm

printer.run_gcode(p.setup(rel_pos=False))

playing = True # track game state
mode = 0 # track game mode (0 = human vs. computer, 1 = human vs. human-controlled computer, 2 = computer vs. computer) - functionality will be added later

while playing: # while game is ongoing
  if mode!=2: # if human is playing
    b.opponent_move(human_move()) # take move
  else: # if computer vs computer
    # take move from stockfish (see below)
    pass # placeholder
  # check for win after each move
  if mode!=1: # if computer is playing
    # see above
  else: # if human vs human
    # take move from remote human (for future version v2)
    pass # placeholder
  # check for win after each move
