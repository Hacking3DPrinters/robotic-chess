# Robotic Chess

An chess playing robot, powered by Stockfish and Octoprint.
For documentation, see [our wiki](https://github.com/Hacking3DPrinters/robotic-chess/wiki).

---

## Requirements

### Essentials
* 3-core CPU and at least 3GB of RAM (theoretically this can run with only 2 cores and 2GB of RAM, but at the risk of crashing / hanging your computer)
* A Linux-based operating system with sudo
* Python 3.10+ and pip
* Octoprint server connected to a 3D printer
* An electromagnet connected to M106/M107 extruder fan control

### Recommended
* 4-core+ CPU and at least 6GB of RAM
* Python 3.11+ and pip
* Knowledge of simple Linux commands

---

## Installation

### Installation from wheel (recommended)

First, visit [our releases page](https://github.com/Hacking3DPrinters/robotic-chess/releases) and download the `.whl` file from the desired version (the 'latest' version is recommended).

Then, run 
```pip install robotic_chess-0.2.1-py3.whl```
(replace 0.2.1 with the version number of your downloaded wheel).

### Installation from source (for development)

First, clone our repo using `git clone https://github.com/Hacking3DPrinters/robotic-chess.git`, and enter the new directory. Then do `pip install dist/robotic_chess-0.2.1-py3-none-any.whl` (replace 0.2.1 with the desired version number). 

---

## Running

### Running from wheel (recommended)

Run `python3 -m robotic_chess`.

### Running from source (for development)

If installed from .whl: Follow instructions above.

Otherwise, run `cd {CLONED_DIR}/src/robotic_chess` (where {CLONED_DIR} is the directory you cloned into) and `python3 __init__.py`. 

---

## Contributing

Please feel free to fork our repo then submit a pull request: we'd love it if you would help us develop new features!

You can also submit a 'feature request' issue: give us some example code if you feel like contributing personally!

---

## Status

This project is in ACTIVE DEVELOPMENT.