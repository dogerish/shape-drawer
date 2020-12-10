# Python part of the .vrpython file
# Load it on vr.vex.com (File -> Load From Your Device),
# then press start in the upper right corner.

# ------------------------------------------
# 
# Project:      Shape Drawer
# Author:       dogerish
# Created:      December 10, 2020
# Description:  VEXcode that draws an equilateral polygon
#               with the pen, given a number of sides and
#               the size of a square (or side length)
# 
# ------------------------------------------

# Library imports
from vexcode import *

# size of 1 square, in MM
square = 200
# number of sides for the shape to have
sideCount = 10

# goes forward one square
def forward(): drivetrain.drive_for(FORWARD, square, MM)
# travels to or from the offset (MM)
def go_offset(os, direction=FORWARD): drivetrain.drive_for(direction, os, MM)

def main():
    # offset before drawing shape
    offset = 900 - square/2
    # angle to turn each side
    angInc = (360/sideCount, DEGREES)
    # turn faster
    drivetrain.set_turn_velocity(400, PERCENT)  
    go_offset(offset) # go to offset
    pen.move(DOWN) # start drawing
    # loop thru all the sides
    for i in range(sideCount):
        forward() # advance
        drivetrain.turn_for(RIGHT, *angInc) # turn by angle increment
    pen.move(UP) # stop drawing now
    go_offset(offset, REVERSE) # return to home

# VR threads — Do not delete
vr_thread(main())
