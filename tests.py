try:
  print('Testing engine...')
  import robotic_chess.engine
except SyntaxError:
  raise
except:
  pass
try:
  print('Testing gcode...')
  import robotic_chess.gcode
except SyntaxError:
  raise
except:
  pass
try:
  print('Testing octoprint...')
  import robotic_chess.octoprint
except SyntaxError:
  raise
except:
  pass
try:
  print('Testing main...')
  import robotic_chess.__main__
except SyntaxError:
  raise
except:
  pass
print('Completed testing.')
