<p align="center">
  <img src="https://raw.githubusercontent.com/Hacking3DPrinters/robotic-chess/main/3DCHESS.png", width=20%, height=auto />
</p>


# Robotic Chess

An chess playing robot, powered by Stockfish and Octoprint.
For documentation, see [our wiki](https://github.com/Hacking3DPrinters/robotic-chess/wiki).

---

## Requirements

### Essentials
* 3-core CPU and at least 3GB of RAM (theoretically this can run with only 2 cores and 2GB of RAM, but at the risk of crashing / hanging your computer)
* A Linux-based operating system with sudo OR a Windows 10/11 operating system.
* Python 3.10+ and pip
* Octoprint server connected to a 3D printer
* An electromagnet connected to M106/M107 extruder fan control

### Recommended
* 4-core+ CPU and at least 6GB of RAM
* Python 3.11+ and pip
* Knowledge of simple Linux commands

---

## Installation

### Installation from wheel (beta for Linux)

First, visit [our releases page](https://github.com/Hacking3DPrinters/robotic-chess/releases) and download the `.whl` file from the desired version (the 'latest' version is recommended).

Then, run 
```pip install robotic_chess-0.2.1-py3.whl```
(replace 0.2.1 with the version number of your downloaded wheel).

You must then edit `~/.config/octoprint-cli.ini` and input the server details of your octoprint server.

### Installation from source (recommended for Windows or Linux dev builds)

First, clone our repo using `git clone https://github.com/Hacking3DPrinters/robotic-chess.git`, and enter the new directory. 
Then edit `config.ini` with your server details of the octoprint server.

Then run `python3 setup.py` to begin setup.

---

## Running

Run `python3 -m robotic_chess`.

---

## Contributing

Please feel free to fork our repo then submit a pull request: we'd love it if you would help us develop new features!

You can also submit a 'feature request' issue: give us some example code if you feel like contributing personally!

---

## Status

This project is in ACTIVE DEVELOPMENT.
