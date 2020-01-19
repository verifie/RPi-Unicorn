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
# 20191028 PME - First draft.
# 20200117 PME - Convert 2D multi-string character arrays to a single 3D array for each character.
# 20200118 PME - Call multiple characters and show them sequentially
# 20200118 2257 PME - Added to git.
#
# Next stage:
# Convert this to Object Oriented code (Its designed for it, but currently expanded from screen writing trials!)

# ---------------------------------------------------------------------------------

# Import libraries.

import time
import unicornhat as unicorn

import characters
characters.init()



# ---------------------------------------------------------------------------------

# Setup Hardware : Unicorn LED Raspberry Pi HAT.

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()


# ---------------------------------------------------------------------------------

# Setting the starting Variables.

r = 255
g = 0
b = 0

colour = 1
column_position = 0
row_position = 0
within_columns = True
within_rows = True
fullpanel = True

letter_count = 0

# ---------------------------------------------------------------------------------

# Run the colour sequence in a loop.

while True:

	# Add some delay.
        #time.sleep(0.5)

        # Set all pixels this colour.

        # ---------------------------------------------------------------------------------

        # Alternate letters with pause in time.

        if letter_count == 0:

                # Choose a letter
                chosen_char = characters.characters.A

        if letter_count == 1:

                # Choose a letter
                chosen_char = characters.characters.l

        if letter_count == 2:

                # Choose a letter
                chosen_char = characters.characters.e

        if letter_count == 3:

                # Choose a letter
                chosen_char = characters.characters.x

        letter_count = letter_count + 1

        if letter_count == 4:
                letter_count = 0
        
        time.sleep(1)







        while fullpanel:
                #time.sleep(0.5)

                # Not used, but part of a for loop to automatically create the item below.
                n = 0






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
                                if column_position < 0:
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
                                #print("End of rows")

                                within_rows = False




                unicorn.show()
                fullpanel = False






