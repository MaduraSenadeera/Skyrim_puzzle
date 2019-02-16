

#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9736263
#    Student name: Madura Senadeera
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  FOUR PIECE JIGSAW PUZZLE
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "draw_attempt".
#  You are required to complete this function so that when the
#  program is run it produces a picture of a jigsaw puzzle whose
#  state of completion is determined by data stored in a list which
#  specifies the locations of the pieces.  You are also required to
#  provide a solution to your particular puzzle.  See the instruction
#  sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

size_of_pieces = 300 # pixels (excluding any protruding "tabs")
half_piece_size = size_of_pieces / 2
max_tab_size = 100 # pixels
box_size = size_of_pieces + (max_tab_size * 2)
half_box_size = box_size / 2
left_border = max_tab_size
gap = max_tab_size
top_bottom_border = max_tab_size
canvas_height = (top_bottom_border + size_of_pieces) * 2
canvas_width = (size_of_pieces * 2 + left_border) * 2
template_centres = [[-(size_of_pieces + half_piece_size), -half_piece_size], # bottom left
                    [-half_piece_size, -half_piece_size], # bottom right
                    [-(size_of_pieces + half_piece_size), half_piece_size], # top left
                    [-half_piece_size, half_piece_size]] # top right
box_centre = [gap + (box_size / 2), 0]

#
#--------------------------------------------------------------------#



#-----Functions for Drawing the Background---------------------------#
#
# The functions in this section are called by the main program to
# draw the background for the puzzle, i.e., the template for the
# pieces and the box they're kept in.  You should not change any of
# the code in this section.  Note that each of these functions
# leaves the turtle's pen up and at its standard width and colour.
#


# Draw the box that contains unused puzzle pieces.  (The box is
# larger than the puzzle pieces to allow for tabs sticking out on
# any of their four sides.)
def draw_box():

    # Determine the position of the box's bottom-left corner
    bottom_left = [box_centre[0] - half_box_size,
                   box_centre[1] - half_box_size]

    # Go to the bottom-left corner and get ready to draw
    penup()
    goto(bottom_left)
    width(5)
    color('black')
    pendown()
    
    # Walk around the box's perimeter
    setheading(0) # point east
    for side in [1, 2, 3, 4]:
        forward(box_size)
        left(90)

    # Reset the pen
    width(1)
    penup()
 

# Draw the individual squares of the jigsaw's template
def draw_template(show_template = False):

    # Only draw if the argument is True
    if show_template:

        # Set up the pen
        width(3)
        color('grey')

        # Draw a box for each centre coordinate
        for centre_x, centre_y in template_centres:
            
            # Determine the position of this square's bottom-left corner
            bottom_left = [centre_x - half_piece_size,
                           centre_y - half_piece_size]

            # Go to the bottom-left corner and get ready to draw
            penup()
            goto(bottom_left)
            pendown()
        
            # Walk around the square's perimeter
            setheading(0) # point east
            for side in [1, 2, 3, 4]:
                forward(size_of_pieces)
                left(90)

        # Reset the pen
        width(1)
        color('black')
        penup()


# As a debugging aid, mark the coordinates of the centres of
# the template squares and the box
def mark_coords(show_coords = False):

    # Only mark the coordinates if the argument is True
    if show_coords:

        # Don't draw lines between the coordinates
        penup()

        # Go to each coordinate, draw a dot and print the coordinate
        color('black')
        for x_coord, y_coord in template_centres + [box_centre]:
            goto(x_coord, y_coord)
            dot(4)
            write(str(x_coord) + ', ' + str(y_coord),
                  font = ('Arial', 12, 'normal'))

    # Reset the pen
    width(1)
    penup()
               
#
#--------------------------------------------------------------------#



#-----Test data------------------------------------------------------#
#
# These are the data sets you will use to test your code.
# Each of the data sets is a list specifying the locations of
# jigsaw puzzle pieces:
#
# 1. The name of the piece, from 'Piece A' to 'Piece D'
# 2. The place to put the piece, either in the template, denoted
#    'Top left', 'Top right', 'Bottom left' or 'Bottom right', or
#    in the unused pieces box, denoted 'In box'
# 3. An optional mystery value, 'X', whose purpose will be
#    revealed only in the second part of the assignment
#
# Each data set does not necessarily mention all pieces.  Also notice
# that several pieces may be in the box at the same time, in which
# case they should just be drawn on top of each other.
#
# You can create further data sets, but do not change any of the
# given ones below because they will be used to test your submission.
#
# Most importantly, you must write your own data set at the end
# to provide the correct solution to your puzzle.
#

# The following data set doesn't require drawing any jigsaw pieces
# at all.  You may find it useful as a dummy argument when you
# first start developing your "draw_attempt" function.

attempt_00 = []

# Each of the following data sets put just one piece in the box.
# You may find them useful when creating your individual pieces.

attempt_01 = [['Piece A', 'In box']]
attempt_02 = [['Piece B', 'In box']]
attempt_03 = [['Piece C', 'In box']]
attempt_04 = [['Piece D', 'In box']]

# Each of the following data sets put just one piece in a
# location in the template.

attempt_05 = [['Piece A', 'Top left']]
attempt_06 = [['Piece B', 'Bottom right']]
attempt_07 = [['Piece C', 'Top right']]
attempt_08 = [['Piece D', 'Bottom left']]
attempt_09 = [['Piece A', 'Bottom left']]
attempt_10 = [['Piece B', 'Top left']]
attempt_11 = [['Piece C', 'Bottom right']]
attempt_12 = [['Piece D', 'Top right']]

# Each of the following data sets put all four pieces in the
# box, but in different orders.

attempt_13 = [['Piece A', 'In box'], ['Piece B', 'In box'],
              ['Piece C', 'In box'], ['Piece D', 'In box']]
attempt_14 = [['Piece D', 'In box'], ['Piece C', 'In box'],
              ['Piece B', 'In box'], ['Piece A', 'In box']]
attempt_15 = [['Piece C', 'In box'], ['Piece D', 'In box'],
              ['Piece A', 'In box'], ['Piece B', 'In box']]

# Each of the following data sets uses between two and four pieces,
# either in the template or in the box

attempt_16 = [['Piece A', 'Top right'], ['Piece B', 'Bottom left']]
attempt_17 = [['Piece D', 'Bottom right'], ['Piece C', 'In box']]
attempt_18 = [['Piece C', 'Bottom right'], ['Piece A', 'Bottom right']]
attempt_19 = [['Piece B', 'In box'], ['Piece D', 'Top left'],
              ['Piece C', 'In box']]
attempt_20 = [['Piece C', 'Top left'], ['Piece D', 'Top right'],
              ['Piece A', 'Bottom left']]
attempt_21 = [['Piece A', 'In box'], ['Piece D', 'Bottom left'],
              ['Piece C', 'Top right']]
attempt_22 = [['Piece A', 'Bottom left'], ['Piece B', 'Top right'],
              ['Piece C', 'Bottom right'], ['Piece D', 'In box']]
attempt_23 = [['Piece D', 'Bottom right'], ['Piece C', 'In box'],
              ['Piece B', 'Top right'], ['Piece A', 'Top left']]
attempt_24 = [['Piece C', 'Bottom right'], ['Piece D', 'Top left'],
              ['Piece A', 'In box'], ['Piece B', 'In box']]
attempt_25 = [['Piece D', 'Bottom left'], ['Piece B', 'In box'],
              ['Piece C', 'Bottom right'], ['Piece A', 'Top right']]
attempt_26 = [['Piece C', 'Bottom left'], ['Piece B', 'In box'],
              ['Piece A', 'Bottom right'], ['Piece D', 'Top right']]
attempt_27 = [['Piece C', 'Bottom left'], ['Piece D', 'In box'],
              ['Piece A', 'Top left'], ['Piece B', 'Top right']]

# Each of the following data sets is a complete attempt at solving
# the puzzle using all four pieces (so there are no pieces left in the box)

attempt_28 = [['Piece A', 'Bottom left'], ['Piece B', 'Bottom right'],
              ['Piece C', 'Top left'], ['Piece D', 'Top right']]
attempt_29 = [['Piece A', 'Top right'], ['Piece B', 'Bottom right'],
              ['Piece C', 'Top left'], ['Piece D', 'Bottom left']]
attempt_30 = [['Piece A', 'Bottom left'], ['Piece B', 'Top left', 'X'],
              ['Piece C', 'Bottom right'], ['Piece D', 'Top right']]
attempt_31 = [['Piece A', 'Bottom right'], ['Piece B', 'Top right'],
              ['Piece C', 'Bottom left', 'X'], ['Piece D', 'Top left']]
attempt_32 = [['Piece D', 'Top right', 'X'], ['Piece A', 'Bottom left', 'X'],
              ['Piece B', 'Top left'], ['Piece C', 'Bottom right']]
attempt_33 = [['Piece A', 'Top right', 'X'], ['Piece B', 'Bottom right'],
              ['Piece C', 'Top left'], ['Piece D', 'Bottom left', 'X']]

# Here you must provide a list which is the correct solution to
# your puzzle.

# ***** Put the solution to your puzzle in this list
solution = [['Piece A','Top left'],['Piece B','Top right'],['Piece C','Bottom right'],['Piece D','Bottom left']] 

#
#--------------------------------------------------------------------#

#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "draw_attempt" function.
#

# Draw the jigsaw pieces as per the provided data set


#-----Puzzle Pieces -------------------------------------------------#

## Setup a function definition for each of the puzzle pieces allowing them to be easily recalled.
## it was important every puzzle piece began drawing from the same position, therefore all pieces begin drawing from the top left-hand corner
## First piece of the puzzle is located in the first quadrant (top left puzzle piece)
def pieceA(position):
## if statement introduced incoporated with the draw_attempt function to identify what is presented in each of the attempt lists
## position is defined as what is found in attempt[1] and if it equals one of the following, a goto function is incoporated to go to the specific position
    if position == 'In box':
        goto(200,150) 
    elif position == 'Top left':
        goto(-600,300)
    elif position == 'Top right':
        goto(-300,300) 
    elif position == 'Bottom left':
        goto(-600,0)
    elif position == 'Bottom right':
        goto(-300,0)  

    ## drawing puzzle piece A, basic puzzle piece
    pensize(5)
    pendown()
    fillcolor('black')
    begin_fill()
    setheading(0)
    forward(300)
    right(90)
    forward(125)
    left(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    left(90)
    forward(125)
    right(90)
    forward(125)
    left(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    left(90)
    forward(125)
    right(90)
    forward(300)
    end_fill()
    
    ## red background diamond 
    penup()
    setheading(0)
    forward(210)
    pendown()
    fillcolor('red')
    begin_fill()
    setheading(245)
    forward(290)
    setheading(300)
    forward(40)
    setheading(270)
    forward(2.52972560799)
    setheading(0)
    forward(17.5592959)
    right(90)
    forward(30)
    setheading(300)
    forward(20)
    setheading(270)
    forward(2.6794919243)
    setheading(0)
    forward(40.00000000005)
    left(90)
    forward(50)
    right(90)
    forward(125)
    left(90)
    forward(125)
    right(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    right(90)
    forward(125)
    left(90)
    forward(90)
    end_fill()


    ## drawing grey skyrim logo, quadrant 1
    fillcolor('dimgray')
    penup()
    forward(210)
    setheading(0)
    forward(230)
    right(90)
    forward(10)
    setheading(260)
    pendown()
    begin_fill()
    forward(20)
    setheading(330)
    forward(15)
    setheading(180)
    forward(15)
    setheading(260)
    forward(125)
    setheading(330)
    forward(30)
    setheading(180)
    forward(30)
    setheading(260)
    forward(45)
    setheading(330)
    forward(15)
    setheading(340)
    forward(15)
    setheading(350)
    forward(15)
    setheading(50)
    forward(15)
    setheading(70)
    forward(15)
    setheading(110)
    forward(15)
    setheading(300)
    forward(20)
    setheading(310)
    forward(15)
    setheading(330)
    forward(15)
    setheading(110)
    forward(20)
    setheading(330)
    forward(15)
    setheading(100)
    forward(5)
    setheading(90)
    forward(5)
    setheading(80)
    forward(5)
    setheading(70)
    forward(15)
    setheading(60)
    forward(5)
    setheading(90)
    forward(5)
    setheading(85)
    forward(15)
    setheading(80)
    forward(5)
    setheading(60)
    forward(15)
    setheading(30)
    forward(5)
    setheading(18)
    forward(5)
    setheading(20)
    forward(15)
    setheading(40)
    forward(15)
    setheading(80)
    forward(5)
    setheading(90)
    forward(0.312200737)
    setheading(180)
    forward(28.105449242)
    setheading(220)
    forward(20)
    setheading(200)
    forward(5)
    setheading(150)
    forward(15)
    setheading(140)
    forward(5)
    setheading(60)
    forward(5)
    setheading(40)
    forward(15)
    setheading(70)
    forward(5)
    setheading(150)
    forward(5)
    setheading(140)
    forward(5)
    setheading(70)
    forward(5)
    setheading(40)
    forward(5)
    setheading(20)
    forward(5)
    setheading(100)
    forward(15)
    setheading(80)
    forward(15)
    setheading(70)
    forward(5)
    setheading(60)
    forward(5)
    setheading(260)
    forward(5)
    setheading(270)
    forward(5)
    setheading(280)
    forward(5)
    setheading(300)
    forward(5)
    setheading(320)
    forward(5)
    setheading(0)
    forward(2.520428142)
    setheading(270)
    forward(46.335609439)
    left(90)
    forward(48)
    setheading(250)
    forward(15)
    setheading(240)
    forward(10)
    setheading(230)
    forward(10)
    setheading(220)
    forward(20)
    setheading(250)
    forward(2)
    setheading(270)
    forward(2)
    setheading(290)
    forward(2)
    setheading(270)
    forward(0.969389542)
    setheading(180)
    forward(16.12090932891)
    left(90)
    forward(125)
    right(90)
    forward(20)
    setheading(140)
    forward(20)
    setheading(160)
    forward(20)
    setheading(150)
    forward(20)
    setheading(290)
    forward(20)
    setheading(250)
    forward(10)
    setheading(140)
    forward(20)
    setheading(160)
    forward(20)
    setheading(150)
    forward(20)
    setheading(260)
    forward(20)
    setheading(290)
    forward(10)
    setheading(270)
    forward(2.10845022875)
    setheading(180)
    forward(5.496940606)
    setheading(270)
    forward(50)
    right(90)
    forward(12)
    setheading(119.25429703408)
    forward (100)
    setheading(65.5)
    forward(280)
    setheading(180)
    forward(0.24544)
    setheading(270)
    forward(2.035091775)
    end_fill()
    penup()

## Second piece of the puzzle is located in the second quadrant (top right puzzle piece)
def pieceB(position):
    if position == 'In box':
        goto(200,150) 
    elif position == 'Top left':
        goto(-600,300)
    elif position == 'Top right':
        goto(-300,300) 
    elif position == 'Bottom left':
        goto(-600,0)
    elif position == 'Bottom right':
        goto(-300,0) 


    pensize(5)
    penup()
    # Drawing basic outline of puzzle Piece B
    setheading(0)
    forward(300)
    fillcolor('black')
    begin_fill()
    pendown()
    setheading(0)
    backward(300)
    right(90)
    forward(125)
    left(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    left(90)
    forward(125)
    left(90)
    forward(125)
    right(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    right(90)
    forward(125)
    left(90)
    forward(300)
    end_fill()
    penup()

    # drawing red diamond background
    left(90)
    forward(210)
    pendown()
    fillcolor('red')
    begin_fill()
    setheading(295)
    forward(290)
    setheading(240)
    forward(40)
    setheading(270)
    forward(2.52972560799)
    setheading(180)
    forward(17.5592959)
    left(90)
    forward(30)
    setheading(240)
    forward(20)
    setheading(270)
    forward(2.6794919243)
    setheading(180)
    forward(40.00000000005)
    right(90)
    forward(50)
    left(90)
    forward(125)
    right(90)
    forward(125)
    right(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    right(90)
    forward(125)
    right(90)
    forward(90)
    end_fill()

    ## drawing grey skyrim logo, quadrant 2
    penup()
    forward(210)
    fillcolor('dimgray')
    setheading(180)
    forward(230)
    left(90)
    forward(10)
    pendown()
    begin_fill()
    setheading(295)
    forward(280)
    setheading(240.7457029)
    forward(98)
    setheading(270)
    forward(0.7328024735)
    right(90)
    forward(15.441819034)
    right(90)
    forward(50)
    left(90)
    forward(5)
    setheading(70)
    forward(10)
    setheading(100)
    forward(20)
    setheading(210)
    forward(20)
    setheading(220)
    forward(20)
    setheading(200)
    forward(20)
    setheading(110)
    forward(13)
    setheading(70)
    forward(20)
    setheading(200)
    forward(20)
    setheading(220)
    forward(20)
    setheading(250)
    forward(10)
    setheading(270)
    forward(1.31370142573)
    setheading(180)
    forward(33.371186818)
    right(90)
    forward(125)
    right(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(2)
    setheading(110)
    forward(5)
    setheading(115)
    forward(15)
    setheading(130)
    forward(5)
    setheading(140)
    forward(5)
    setheading(150)
    forward(5)
    setheading(160)
    forward(10)
    setheading(50)
    forward(15)
    setheading(40)
    forward(5)
    setheading(30)
    forward(5)
    setheading(210)
    forward(5)
    setheading(200)
    forward(5)
    setheading(190)
    forward(5)
    setheading(210)
    forward(5)
    setheading(220)
    forward(5)
    setheading(170)
    forward(15)
    setheading(180)
    forward(0.096480829)
    left(90)
    forward(40.27448931)
    left(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(35)
    setheading(290)
    forward(20)
    setheading(280)
    forward(30)
    setheading(30)
    forward(15)
    setheading(250)
    forward(20)
    setheading(50)
    forward(15)
    setheading(60)
    forward(15)
    setheading(290)
    forward(15)
    setheading(310)
    forward(15)
    setheading(10)
    forward(15)
    setheading(20)
    forward(15)
    setheading(30)
    forward(15)
    setheading(100)
    forward(45)
    setheading(180)
    forward(30)
    setheading(30)
    forward(30)
    setheading(100)
    forward(125)
    setheading(180)
    forward(15)
    setheading(30)
    forward(15)
    setheading(100)
    forward(20)
    end_fill()
    penup()

## defining a function to allow for the third piece to be drawn, (quadrant 3)
def pieceC(position):
    if position == 'In box':
        goto(200,150) 
    elif position == 'Top left':
        goto(-600,300)
    elif position == 'Top right':
        goto(-300,300) 
    elif position == 'Bottom left':
        goto(-600,0)
    elif position == 'Bottom right':
        goto(-300,0) 

## drawing outline of basic puzzle piece
    pensize(5)
    penup()
    setheading(0)
    forward(300)
    setheading(270)
    forward(300)
    fillcolor('black')
    begin_fill()
    pendown()
    setheading(90)
    forward(300)
    left(90)
    forward(125)
    left(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    left(90)
    forward(125)
    left(90)
    forward(125)
    left(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    left(90)
    forward(125)
    left(90)
    forward(300)
    end_fill()

## drawing background diamond shape of puzzle piece
    penup()
    setheading(90)
    forward(250)
    setheading(180)
    forward(137)
    pendown()
    fillcolor('red')
    begin_fill()
    setheading(240)
    forward(285)
    setheading(270)
    forward(3.182759922)
    setheading(180)
    forward(20.5)
    setheading(90)
    forward(125)
    right(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    right(90)
    forward(125)
    right(90)
    forward(125)
    right(90)
    forward(50)
    left(90)
    forward(50)
    setheading(90)
    forward(22)
    setheading(60)
    forward(30)
    setheading(90)
    forward(2.01923788699)
    setheading(180)
    forward(15)
    setheading(270)
    forward(50)
    right(90)
    forward(12)
    end_fill()

## drawing grey skyrim logo, quadrant 3
    penup()
    setheading(180)
    forward(23)
    pendown()
    fillcolor('dimgray')
    begin_fill()
    setheading(240.7457029)
    forward(70)
    setheading(150)
    forward(10)
    setheading(240)
    forward(10)
    setheading(180)
    forward(25)
    setheading(90)
    forward(40)
    right(90)
    forward(10)
    setheading(290)
    forward(20)
    setheading(30)
    forward(20)
    setheading(50)
    forward(20)
    setheading(70)
    forward(20)
    setheading(95)
    forward(20)
    setheading(100)
    forward(20)
    setheading(70)
    forward(10)
    setheading(90)
    forward(0.394545057102)
    setheading(180)
    forward(88)
    setheading(315)
    forward(20)
    setheading(280)
    forward(20)
    setheading(270)
    forward(20)
    setheading(250)
    forward(20)
    setheading(240)
    forward(40)
    setheading(230)
    forward(20)
    setheading(270)
    forward(2.405951887)
    setheading(0)
    forward(40.888188217)
    right(90)
    forward(50)
    right(90)
    forward(25)
    setheading(240)
    forward(5)
    setheading(230)
    forward(5)
    setheading(220)
    forward(25)
    setheading(180)
    forward(0.134950873)
    setheading(270)
    forward(70)
    setheading(60.74570296592)
    forward(70)
    setheading(220)
    forward(40)
    setheading(180)
    forward(3.566289529)
    setheading(90)
    forward(58.869388714)
    right(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    right(90)
    forward(50)
    setheading(50)
    forward(10)
    setheading(70)
    forward(5)
    setheading(110)
    forward(10)
    setheading(120)
    forward(5)
    setheading(180)
    forward(2.217775381)
    setheading(90)
    forward(48.9140392382)
    right(90)
    forward(125)
    right(90)
    forward(50)
    left(90)
    forward(15)
    end_fill()
    penup()

## defining function to draw pieceD, quadrant 4
def pieceD(position):
    if position == 'In box':
        goto(200,150) 
    elif position == 'Top left':
        goto(-600,300)
    elif position == 'Top right':
        goto(-300,300) 
    elif position == 'Bottom left':
        goto(-600,0)
    elif position == 'Bottom right':
        goto(-300,0) 

## drawing basic outline of puzzle piece
    pensize(5)
    setheading(270)
    forward(300)
    pendown()
    fillcolor('black')
    begin_fill()
    setheading(0)
    forward(300)
    left(90)
    forward(125)
    right(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    right(90)
    forward(125)
    left(90)
    forward(125)
    left(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    left(90)
    forward(125)
    left(90)
    forward(300)
    end_fill()

## drawing red diamond in background
    penup()
    setheading(90)
    forward(250)
    right(90)
    forward(137)
    pendown()
    fillcolor('red')
    begin_fill()
    setheading(300)
    forward(285)
    setheading(270)
    forward(3.182759922)
    setheading(0)
    forward(20.5)
    setheading(90)
    forward(125)
    right(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    right(90)
    forward(125)
    left(90)
    forward(125)
    left(90)
    forward(50)
    right(90)
    forward(50)
    setheading(90)
    forward(22)
    setheading(120)
    forward(30)
    setheading(90)
    forward(2.01923788699)
    setheading(0)
    forward(15)
    right(90)
    forward(50)
    left(90)
    forward(12)
    end_fill()


## drawing grey skyrim logo, quadrant 4
    penup()
    setheading(0)
    forward(26)
    fillcolor('dimgray')
    begin_fill()
    setheading(299.25429703408)
    pendown()
    forward(140)
    setheading(90)
    forward(100)
    left(90)
    forward(10)
    setheading(250)
    forward(20)
    setheading(150)
    forward(20)
    setheading(130)
    forward(20)
    setheading(110)
    forward(20)
    setheading(85)
    forward(20)
    setheading(80)
    forward(20)
    setheading(110)
    forward(5)
    setheading(90)
    forward(2.50490931365)
    right(90)
    forward(95.64505452)
    setheading(280)
    forward(20)
    setheading(300)
    forward(20)
    setheading(310)
    forward(10)
    setheading(0)
    forward(3.389059634)
    setheading(270)
    forward(25)
    setheading(240)
    forward(20)
    setheading(250)
    forward(20)
    setheading(250)
    forward(40)
    setheading(320)
    forward(30)
    setheading(320)
    forward(10)
    setheading(300)
    forward(5)
    setheading(240)
    forward(60)
    setheading(300)
    forward(50)
    setheading(0)
    forward(2.379430875)
    setheading(90)
    forward(30)
    setheading(160)
    forward(10)
    setheading(130)
    forward(15)
    setheading(50)
    forward(28)
    setheading(0)
    forward(1.040687281)
    setheading(90)
    forward(27.323486225)
    right(90)
    forward(30)
    setheading(130)
    forward(45)
    setheading(110)
    forward(10)
    setheading(40)
    forward(5)
    setheading(90)
    forward(2.917135804)
    setheading(180)
    forward(1.484578346)
    right(90)
    forward(125)
    left(90)
    forward(125)
    left(90)
    forward(50)
    right(90)
    forward(12)
    end_fill()
    penup()

## defining a function to easily draw the error symbol for the code, very similar to the missing image message seen on chrome
def error_piece(position):
    ## similar to the process conducted for the puzzle pieces, if statements are to be utilised to determine whether the values correspond correctly to the lists and if so,
    # the cursor will go to the specific position to draw the error piece
    if position == 'Top left':
        goto(-487.5,200)
    elif position == 'Top right':
        goto(-187.5,200) 
    elif position == 'Bottom left':
        goto(-487.5,-100)
    elif position == 'Bottom right':
        goto(-187.5,-100)
 
    pencolor('black')
    shape('square')
    color('black')
    setheading (270)
    pensize(10)
    pendown()
    forward(100)
    left(90)
    forward(75)
    left(90)
    forward(75)
    penup()
    forward(25)
    left(90)
    forward(25)
    pendown()
    forward(50)
    penup()
    backward(40)
    setheading(270)
    pendown()
    forward(35)
    left(90)
    forward(35)
    penup()
    setheading(90)
    forward(17.5)
    left(90)
    forward(7.5)
    shapesize(0.5,0.5)
    stamp()
    right(90)
    forward(10)
    left(90)
    forward(10)
    shapesize(0.5,0.5)
    stamp()
    setheading(180)
    forward(20)
    setheading(90)
    forward(7.5)
    setheading(180)
    forward(37.5)
    setheading(270)
    forward(25)
    setheading(0)
    forward(21)
    shapesize(0.75,0.75)
    stamp()
    setheading (270)
    forward(60)
    shapesize(0.5,0.5)
    stamp()
    setheading(90)
    forward(10)
    setheading(0)
    forward(10)
    stamp()
    forward(10)
    stamp()
    forward(10)
    setheading(270)
    forward(10)
    stamp()
#---------------------------------------------------------------------#

#-----Draw_attempt function-------------------------------------------#
    
## Modifying the draw_attempt function to properly allow for the execution of each of the lists presented at the top of the file      
def draw_attempt(attempt):
    ## to allow for the function to be neat and efficient in execution, a 'for' loop is utilised to iterate lists and gather certain information rather than constantly repeating the same tasks
    # to do this a variable named nested_list is introduced to represents the inner lists with attempt(which is a nested list)

    
    for nested_list in attempt:
        position = nested_list[1] # referring to the lists, [1] in the list is the position for where the puzzle piece is to be found, therefore we allow this variable to be created 
        if len(nested_list) == 2: ## this line is very important as it records the length of the nested list, and if it is equal to 2 the follow will be executed
            if nested_list[0] == 'Piece A': ## this nested if statments utilise multiple 'if' and 'elif' functions to present what is found in [0] which is the puzzle pieces, therefore the following is done
                pieceA(position)
            elif nested_list[0] == 'Piece B':
                pieceB(position)
            elif nested_list[0] == 'Piece C':
                pieceC(position)
            elif nested_list[0] == 'Piece D':
                pieceD(position)
        else: ## if the list does not have a length of 2, it will execute the following as the lists having a length of 3 include the 'X' value which is the error piece.
            error_piece(position)
            
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your jigsaw pieces.  Do not change any of this code except
# where indicated by comments marked '*****'.
#
    
# Set up the drawing canvas
setup(canvas_width, canvas_height)

# Give the canvas a neutral background colour
# ***** You can change the background colour if necessary to ensure
# ***** good contrast with your puzzle pieces
bgcolor('light grey')

# Give the window a title
# ***** Replace this title with one that describes the picture
# ***** produced by solving your puzzle
title('Four Piece Jigsaw Puzzle - SKYRIM')

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(True)

# Draw the box that holds unused jigsaw puzzle pieces
draw_box()

# Draw the template that holds the jigsaw pieces
# ***** If you don't want to display the template change the
# ***** argument below to False
draw_template(True)

# Mark the centres of the places where jigsaw puzzle pieces must
# be drawn
# ***** If you don't want to display the coordinates change the
# ***** argument below to False
mark_coords(False)

# Call the student's function to display the attempted solution

# ***** Change the argument to this function to test your
# ***** code with different data sets
draw_attempt(solution)

# Exit gracefully by hiding the cursor and releasing the window
tracer(True)
hideturtle()
done()
#
#--------------------------------------------------------------------#

