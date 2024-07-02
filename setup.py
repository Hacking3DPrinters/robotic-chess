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
    system('mv config.ini ~/.config/octoprint-cli.ini')
  elif platform.system()=='Windows':
    setup()
    system('tar -xf stockfish-windows.zip')
    system('mkdir C:/Users/'+getpass.getuser()+'/stockfish/')
    system('move stockfish/stockfish-windows-x86-64-sse41-popcnt.exe C:/Users/'+getpass.getuser()+'/stockfish/stockfish.exe')
  else:
    raise OSError('OS unsupported.')
