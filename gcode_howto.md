SYNTAX
Begin and end a program with '%'.
Each command should be on a new line.
Comments should be written with ';' (equivalent of # python)

POSITION COMMANDS

G28 [X Y Z] - Go at full speed to home position [with specific axis or axes]
G90 - Set absolute position mode (xyz coords)
G91 - Set relative position mode (xyz coords will be added to current coords)

UNITS COMMANDS

G20 - Set inches mode
G21 - Set mm mode (use this)

MOVING COMMANDS

G00 - Move to location at top speed (for positioning)
Examples (absolute position mode G90):
	G00 X0 Y0 Z0 - move to X=0 Y=0 Z=0 at top speed
	G00 X10 - move X-axis to X=10mm at top speed
Examples (relative position mode G91):
	G01 X10 - move X-axis 10mm in the positive direction at top speed

G01 - Move to location at Fmm/min (for work)
Examples (absolute position mode G90):
	G01 X0 Y0 Z0 F1000 - move to X=0 Y=0 Z=0 at 1000mm/min
	G01 X10 F2000 - move X-axis to X=10mm at 2000mm/min
Examples (relative position mode G91):
	G01 X10 F2000 - move X-axis 10mm in the positive direction at 2000mm/min
