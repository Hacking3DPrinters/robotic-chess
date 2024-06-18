from os import system as cmd
from os.path import exists
class PrinterError(Exception):
  pass
class Printer:
  def __init__(self):
    self.loaded_file=False
    cmd('octoprint-cli connection connect')
  def load_file(self, file='./output.gcode'):
    if exists(file):
      self.loaded_file=True
      cmd('octoprint-cli print select {path}'.format(path=str(file)))
    else:
      raise PrinterError('File selected was invalid')
  def start_file(self):
    if self.loaded_file:
      cmd('octoprint-cli print start')
      self.loaded_file=False
    else:
      raise PrinterError('No file selected using Printer.load_file()')
  def run_gcode(self,gcode):
    cmd('octoprint-cli gcode {command}'.format(command=str(gcode)))
  def connect(self):
    # should never be called
    cmd('octoprint-cli connection connect')
  def disconnect(self):
    cmd('octoprint-cli connection disconnect')
