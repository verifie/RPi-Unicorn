# RPi-Unicorn
Playing with the Raspberry Pi Unicorn Hat (8x8 RGB LED).  Code intended to be generic upto Unicorn Driver to port to other 8x8 devices.


Current version doesn't work and is based on code that started tweaking examples and not structured in any way.
Next stage is to move closer to object oriented formation.

Functionality wise, the next stage is to show a series of characters, sequentially.  Presentation methods to show a sequence of tect by writing to a long message buffer, then drawing specific positions to the Unicorn array.  Final stage for this program will be to take an input when calling the Python 3 program, along with control characters that specify letter by letter, scroll, speed and colour options.
