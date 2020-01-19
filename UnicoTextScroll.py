#!/usr/bin/env python

#########################################################################################################################################    
# UnicoText.py
# (c) Leighton Electronics. 2019 - 2020 onwards.
# 
# Description :         Show text and characters on the Raspberry Pi Unicorn Hat.
# Dependencies :        Raspberry Pi, Linux, Unicorn Hat Python Library, Python 3.
#
# Status :              10 Casual Dev coding.
#
# Version History
# Unicorn HAT.  Setting up a 'screen memory' array.
# 20191028 0000 PME - First draft.
# 20200117 0000 PME - Convert 2D multi-string character arrays to a single 3D array for each character.
# 20200118 0000 PME - Call multiple characters and show them sequentially
# 20200118 2257 PME - Added to git. Shows more than one character in one run (Logic modified to allow multiple runs).
# 20200119 2128 PME - Sequential character calling from a string of text using a LUT (Look Up Table). 
#                       Prep for scrolling: Assemble a long run of data, then read from positions according to time.
#                       Rotated display so Raspberry Pi power cable on top (Trial in this version).
# 20200119 2141 PME - Bug fix, rotation.
# 20200119 2145 PME - Starting work on reading data from a string (to changeout for a more dynamic method later). 
#                       This version should just read through the message on screen.  Next stage to populate a new pixel 3d variable using a LUT sequence.
#
#
# Next stage:
# Convert this to Object Oriented code (Its designed for it, but currently expanded from screen writing trials!)
# Message scrolling.

# ---------------------------------------------------------------------------------

# Import libraries.

import time
import unicornhat as unicorn

import characters
characters.init()



# ---------------------------------------------------------------------------------

#       MESSAGE STRING
msg = "Hello Alex."

# ---------------------------------------------------------------------------------

# Setup Hardware : Unicorn LED Raspberry Pi HAT.

def unicornSetup():
        unicorn.off()
        unicorn.clear()
        unicorn.set_layout(unicorn.AUTO)
        unicorn.rotation(180)
        unicorn.brightness(0.5)
        width,height=unicorn.get_shape()


unicornSetup()
# ---------------------------------------------------------------------------------

# Setting the starting Variables.

msg_speed = 0.5
colour = 1
column_position = 0
row_position = 0
within_columns = True
within_rows = True
fullpanel = True

# Inspect msg data to determine specification of task.
print("Message to display : ", msg)
msg_position = 0
msg_end = len(msg)
print("Message Length : ", msg_end)

# ---------------------------------------------------------------------------------

# Run the sequence in a permanent loop.

while True:

        # ---------------------------------------------------------------------------------


        msg_position_character = msg[msg_position]
        print("Current Message Position", msg_position)
        print("Current Message Character", msg_position_character)


        # Check to see if we have reached the end of the message,  If we have, set to zero and restart.
        if msg_position == msg_end:
                msg_position = 0
        
        
        # Increment the position by 1
        msg_position = msg_position + 1
        
        
        # ---------------------------------------------------------------------------------

        # Prepare the screen by setting row and column position as zero (starting point), and reset within flags.
        fullpanel = True
        
        column_position = 0
        row_position = 0
        within_columns = True
        within_rows = True

        #
        time.sleep(msg_speed)


        # ---------------------------------------------------------------------------------

        while fullpanel:
                #time.sleep(0.5)

                # Lookup the row data from the 3d character array.
                row_string_0 = chosen_char[0]
                row_string_1 = chosen_char[1]
                row_string_2 = chosen_char[2]
                row_string_3 = chosen_char[3]
                row_string_4 = chosen_char[4]
                row_string_5 = chosen_char[5]
                row_string_6 = chosen_char[6]
                row_string_7 = chosen_char[7]


                #print("Row string construction : ", row_string_0)


                # Computers can place items in row / column 0 (humans would call that row or column 1), but .. computers count from 1. So we must subtract
                # one from the count which mimics the row / column position starting from 0 not 1. (Go with it, it makes sense to a computer :)
                # Also, computers draw to a screen usually top to bottom, left to right.
                
                #row_position = len(row_string_0) - 1
                row_position = 7

                #print("Starting Row Position :", row_position)

                column_position = len(row_string_0) - 1
                #print("Starting Column Position :", column_position)


                # Setup the panel by passing Panel data array to the device library command

                # Setup a loop to setup each row in the panel.
                while within_rows:

                        # Add some delay for a visual debug.
                        #time.sleep(0.2)

                        #print("Row Position : ", row_position)
                        row = chosen_char[row_position]


                        # The program draws from right to left. To lightup the panel as we see it above, we must reverse the presentation of the array (7 to 0).
                        #row.reverse()
                        #print("Rows Data: ", row)


                        # Setup column data.
                        while within_columns:

                                # Add some delay for a visual debug.
                                #time.sleep(0.01)
                                               
                                # Select data from the position in the array
                                #print("Column Position : ", column_position) 
                                rgb_data = row[column_position]
                                #print("RGB Data : ", rgb_data)


                                # Set the colour

                                red = rgb_data[0]
                                #print("Red = ",red)

                                green = rgb_data[1]
                                #print("Green = ",green)

                                blue = rgb_data[2]
                                #print("Blue = ",blue)
                        

                                # Set the pixel   
                                #print("Column Position:", int(column_position), " Row:", int(row_position), "RGB:", int(red), int(green), int(blue))
                    
                                unicorn.set_pixel(int(column_position), int(row_position), int(red), int(green), int(blue))


                                # Prepare for the next item in the list by changing the position.  Set the Column position
                                column_position = column_position - 1

                                # Tell panel to show the colour.  You can do this here to create each pixel, or at the end of each column loop, or row loops to draw
                                # everything at once.  This way replicated the way a computer might normally 'draw' to a monitor
                                

                                # Check to see if we've passed the last column and exit the column setting loop if we have. Or allow the loop to repeat.
                                if column_position == 0:
                                        #print("End of Column")

                                        # Return column_position to first column
                                        column_position = len(row_string_0) - 1
                                        
                                        # Increment the row position.
                                        row_position = row_position - 1

                                        # Exit the column setting loop
                                        within_columns = False

                        # We are back within columns as we are starting a new row.
                        within_columns = True

                        if row_position < 0:
                                #print("End of Rows")

                                within_rows = False




                unicorn.show()
                fullpanel = False






