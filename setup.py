from setuptools import setup
from os import system
import platform
import getpass

if __name__ == "__main__":
  if platform.system()=='Linux':
    setup()
    system('git clone https://github.com/official-stockfish/Stockfish.git')
    system('cd Stockfish/src/ && make -j build')
    system('sudo mv Stockfish/src/stockfish /usr/local/bin/')
    system('sudo chmod a+x /usr/local/bin/stockfish')
  elif platform.system()=='Windows':
    setup()
    system('git clone https://github.com/official-stockfish/Stockfish.git')
    system('cd Stockfish/src/ && make -j build')
    system('move Stockfish/src/stockfish C:/Users/'+str(getpass.getuser())+'/stockfish')
  else:
    raise OSError('OS unsupported.')