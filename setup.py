from setuptools import setup
from os import system

if __name__ == "__main__":
  setup()
  system('git clone https://github.com/official-stockfish/Stockfish.git')
  system('cd Stockfish/src/')
  system('make -j build')
  system('sudo mv ./stockfish /usr/local/bin/')
  system('sudo chmod a+x /usr/local/bin/stockfish')
  