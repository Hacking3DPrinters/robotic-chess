from robotic_chess.chess import Board
import robotic_chess.gcode
import robotic_chess.octoprint
# main code goes here
def letter_to_number(letter):
  if letter='a':
    return 1
  elif letter='b':
    return 2
  elif letter='c':
    return 3
  elif letter='d':
    return 4
  elif letter='e':
    return 5
  elif letter='f':
    return 6
  elif letter='g':
    return 7
  elif letter='h':
    return 8
def notation_to_coords(move='a1a2'):
  return [[1.59375+(letter_to_number(move[0:1])-1*3.1875),1.59375+(int(move[1:2])-1*3.1875)],[1.59375+(letter_to_number(move[2:3])-1*3.1875),1.59375+(int(move[3:4])-1*3.1875)]]
board = Board()

