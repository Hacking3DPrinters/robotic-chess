print('Initialising libraries...')
import robotic_chess.octoprint # import printer lib

from robotic_chess.gcode import Parser # import gcode lib
from robotic_chess.chess import Engine  # import chess lib

from multiprocessing import cpu_count as cpus
from math import ceil as roundup
from math import floor as rounddown
import sys # import exit lib
# main code goes here
print('Initialised.')

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

def human_move(): # take move from human
  while True: # while move is invalid
    h_move = str(input('Input move: ')) # take a move
    if len(h_move)==4: # if move is valid
      break # break loop
    print('Input invalid. Should be formatted as [start][end], 	e.g. a1a2 for square a1 to square a2') # if move is invalid, print error message
    return h_move # return move

def robot_move(best_move): # make move
  best_move_coords = notation_to_coords(move=best_move) # get coords for best move
  if get_capture(best_move): # if move is a capture
    capture_coords={'x':best_move_coords[1][0],'y':best_move_coords[1][1],'z':piece_height} # find coords for the capture
    printer.run_gcode(p.add_movement(x=capture_coords['x'], y=capture_coords['y'], z=capture_coords['z'], speed=500)) # go to those coords
    printer.run_gcode(p.add_fan()) # pick up piece
    printer.run_gcode(p.add_movement(z=20, speed=1000)) # move up
    printer.run_gcode(p.add_movement(x=191.25,y=255,speed=500))
    printer.run_gcode(p.add_fan(speed=0)) # release piece
    printer.run_gcode(p.add_home()) # go home
  printer.run_gcode(p.add_movement(x=best_move_coords[0][0], y=best_move_coords[0][1], z=piece_height, speed=500)) # find coords of start square and go there
  printer.run_gcode(p.add_fan()) # pick up piece
  printer.run_gcode(p.add_movement(z=20, speed=1000)) # move up
  printer.run_gcode(p.add_movement(x=best_move_coords[1][0], y=best_move_coords[1][1], z=piece_height, speed=500)) # find coords of end square and go there
  printer.run_gcode(p.add_fan(speed=0)) # release piece
  printer.run_gcode(p.add_home()) # go home

print('Robotic Chess v1.0.0')
print('MIT Licence 2024 Benjamin Porter and Zachary Birket')
print()
if __name__ == "__main__":
if cpus()<3:
  print('Not enough CPUs.')
  sys.exit()

print('Please select a game mode:')
print('Mode 0: Physical Human vs. Virtual Computer')
print('Mode 1: Physical Human vs. Virtual Human')
print('Mode 2: Virtual Computer vs. Virtual Computer')

mode = int(input('Mode (0/1/2): ')) # track game mode (0 = human vs. computer, 1 = human vs. human-controlled computer, 2 = computer vs. computer) - functionality will be added later

if mode==0 or mode==1 or mode==2: # check if mode is valid
  pass
else:
  print('Mode invalid. Please retry.') # otherwise exit
  sys.exit()

b = Engine(cpu=round(roundup((cpus()-2)))) # initialise classes
p = Parser()
printer = robotic_chess.octoprint.Printer()
print('Please select a rating:')
print('Valid ratings are between 100 and 3100')
b.engine_skill(int(input('Rating: ')))

piece_height = 100 # define piece height in mm

printer.run_gcode(p.setup(rel_pos=False))

playing = True # track game state

while playing: # while game is ongoing
  if mode==0: # if human vs computer
    b.opponent_move(human_move()) # take move
  elif mode==1: # if human vs human
    print(human_move) # display human move to remote human
  else: # if computer vs computer
    computer_move(b.engine_move()) # take move and record for opponent
  if mode==0: # if human vs computer
    computer_move(b.engine_move())
  elif mode==1: # if human vs human
    # take move from remote human
    pass
  else:
    computer_move(b.engine_move()) # take move and record for opponent
  # check for win after each move
