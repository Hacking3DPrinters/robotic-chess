<p align="center">
  <img src="https://raw.githubusercontent.com/Hacking3DPrinters/robotic-chess/main/3DCHESS.png", width=20%, height=auto />
</p>


# Robotic Chess

An chess playing robot, powered by Stockfish.
For documentation, see [our wiki](https://github.com/Hacking3DPrinters/robotic-chess/wiki).

---

## Installation

### Installation from wheel

First, visit [our releases page](https://github.com/Hacking3DPrinters/robotic-chess/releases) and download the `.whl` and `requirements.txt` files from the desired version.

Then, run 
```pip install robotic_chess-0.2.1-py3.whl```
(replace 0.2.1 with the version number of your downloaded wheel).

Finally, run 
```pip install -r requirements.txt```
to install dependencies.

THIS DOES NOT INSTALL STOCKFISH OR OCTOPRINT (will be included in the future).

### Installation from source 

First, clone our repo using `git clone https://github.com/Hacking3DPrinters/robotic-chess.git`, and enter the new directory. Then do `pip install dist/robotic_chess-0.2.1-py3-none-any.whl` (replace 0.2.1 with the desired version number), followed by `pip install -r requirements.txt`.

THIS DOES NOT INSTALL STOCKFISH OR OCTOPRINT (will be included in the future).
