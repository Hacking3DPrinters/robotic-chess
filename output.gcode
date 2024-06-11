%
G91 ; set relative position
G21 ; mm
G00 X0 Y20 Z0 ; go to set home
G01 X10 Z10 F1000
G00 X0 Y20 Z0 ; go to set home
M106 S255 ; use fan
G01 X10 Z10 F100
M106 S0 ; use fan
%
