%
G21 ; use mm
G28 ; return to home position
G90 ; set absolute position mode
G00 X20 Y20 Z20 ; the machine should move 2cm forward in all directions
G00 X10 ; the machine should move 1cm backward in the X-axis
G00 Y10 ; the machine should move 1cm backward in the Y-axis
G00 Z10 ; the machine should move 1cm backward in the Z-axis
G01 X20 Y20 Z20 F150 ; the machine should move 1cm forward in all directions over 4 seconds
G01 X10 F300 ; the machine should move 1cm backward in the X-axis over 2 seconds
G01 Y10 F300 ; the machine should move 1cm backward in the Y-axis over 2 seconds
G01 Z10 F300 ; the machine should move 1cm backward in the Z-axis over 2 seconds
G28 ; return to home position
G91 ; set relative position mode
G00 X10 ; the machine should move 1cm forward in the X-axis
G01 X-10 F300 ; the machine should move 1cm backward in the X-axis over 2 seconds
G00 Y10 ; the machine should move 1cm forward in the Y-axis
G01 Y-10 F600 ; the machine should move 1cm backward in the Y-axis over 1 second
G00 Z10 ; the machine should move 1cm forward in the Z-axis
G01 Z-10 F1200 ; the machine should move 1cm backward in the Z-axis over 0.5 seconds
G28 ; return to home position
G90 ; set absolute position mode
G00 X20 Y20 Z20 ; the machine should oscillate quickly
G00 X0 Y0 Z0 ; and keep doing it
G00 X20 Y20 Z20 ; at top speed
G00 X0 Y0 Z0 ; for a bit then stop
%