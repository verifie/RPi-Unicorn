# characters

# Version History
# 20200119 2231 PME - Amending character name for space to  .
# ---------------------------------------------------------------------------------

# Define characters in typeface definitions.
def init():

    print("Function : callCharacters")

    global character_smiley
    global character_smiley_cheeky
    global character_poppy
    global character_A
    global character_B
    global character_C
    global character_D
    global character_E
    global character_G
    global character_H
    global character_I
    global character_J
    global character_K
    global character_L
    global character_M
    global character_N
    global character_O
    global character_P
    global character_Q
    global character_R
    global character_S
    global character_T
    global character_U
    global character_V
    global character_W
    global character_Y
    global character_Z
    global character_a
    global character_b
    global character_c
    global character_d
    global character_e
    global character_f
    global character_g
    global character_h
    global character_i
    global character_j
    global character_k
    global character_l
    global character_m
    global character_n
    global character_o
    global character_p
    global character_q
    global character_r
    global character_s
    global character_t
    global character_u
    global character_v
    global character_w
    global character_x
    global character_y
    global character_z
    global character_0
    global character_1
    global character_2
    global character_3
    global character_4
    global character_5
    global character_6
    global character_7
    global character_8
    global character_9
    global character_arrow_up
    global character_arrow_down
    global character_arrow_left
    global character_arrow_right
    global character_exclaim
    global character_add
    global character_divide
    global character_subtract
    global character_multiply
    global character_
    global character_-
    global character_dot
    global character_pound


    # ---------------------------------------------------------------------------------

    # Define colour swatch key. Format Red, Green, Blue, 0-255.

    a = [0,0,0]                 # Black
    w = [255,255,255]           # White
    r = [255,0,0]               # Red
    t = [255,150,150]           # Light Red
    g = [0,255,0]               # Green
    h = [150,255,150]           # Light Green
    b = [0,0,255]               # Blue
    n = [150,250,150]           # Light Blue
    p = [255,0,255]             # Purple
    y = [255,255,0]             # Yellow
    o = [200,100,0]             # Orange
    l = [255,0,200]             # Pink
    q = o                       # Character Colour (Change to RGB or previously defined colour as wanted)


    # ---------------------------------------------------------------------------------

    # Define typeface global character_s.


    character_poppy = [
    [a,a,a,r,r,a,a,g],
    [a,a,r,r,r,g,g,g],
    [a,a,r,r,r,r,g,a],
    [r,r,r,a,a,r,r,r],
    [r,r,r,a,r,r,r,a],
    [a,r,r,r,r,r,a,a],
    [a,a,r,h,a,a,a,a],
    [a,a,a,h,a,a,a,a]]


    character_smiley_cheeky = [
    [a,a,b,b,b,b,b,a],
    [a,y,y,y,y,y,y,a],
    [y,y,a,n,y,a,n,y],
    [y,y,y,y,y,y,y,y],
    [y,y,y,y,y,y,y,y],
    [y,y,a,r,r,r,a,y],
    [a,y,y,r,r,r,y,a],
    [a,a,y,y,r,y,a,a]]


    character_smiley = [
    [a,a,a,a,a,a,a,a],
    [a,w,w,a,a,w,w,a],
    [a,w,n,a,a,n,w,a],
    [a,a,a,a,a,a,a,a],
    [a,w,a,a,a,a,w,a],
    [a,w,a,a,a,a,w,a],
    [a,a,w,w,w,w,a,a],
    [a,a,a,a,a,a,a,a]]


    character_A = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,q,a,q,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,q,q,q,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [q,q,q,a,q,q,q,a]]


    character_B = [
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,q,q,q,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,q,q,q,a,a,a]]


    character_C = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,q,q,a,a],
    [a,a,q,a,a,a,q,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,a,q,a,a,a,q,a],
    [a,a,a,q,q,q,a,a]]


    character_D = [
    [a,a,a,a,a,a,a,a],
    [a,q,q,q,a,a,a,a],
    [a,q,a,a,q,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,q,a,a,a],
    [a,q,q,q,a,a,a,a]]


    character_E = [
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,q,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,q,q,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,a,q,q,q,q,a,a]]


    character_F = [
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,q,q,q,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,q,q,q,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a]]


    character_G = [
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,q,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,q,q,q,a],
    [a,q,a,a,a,q,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,q,q,q,a,a,a]]


    character_H = [
    [a,a,a,a,a,a,a,a],
    [q,q,q,a,q,q,q,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,q,q,q,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [q,q,q,a,q,q,q,a]]


    character_I = [
    [a,a,a,a,a,a,a,a],
    [a,q,q,q,q,q,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,q,q,q,q,q,a,a]]


    character_J = [
    [a,a,a,a,a,a,a,a],
    [a,q,q,q,q,q,q,a],
    [a,a,a,a,q,a,a,a],
    [a,a,a,a,q,a,a,a],
    [a,a,a,a,q,a,a,a],
    [a,q,a,a,q,a,a,a],
    [a,q,a,a,q,a,a,a],
    [a,a,q,q,a,a,a,a]]


    character_K = [
    [a,a,a,a,a,a,a,a],
    [a,q,a,a,a,a,q,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,q,a,a,a],
    [a,q,q,q,a,a,a,a],
    [a,q,a,a,q,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,a,q,a]]


    character_L = [
    [a,a,a,a,a,a,a,a],
    [q,q,q,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,q,a],
    [a,q,q,q,q,q,q,a]]


    character_M = [
    [a,a,a,a,a,a,a,a],
    [q,q,a,a,a,q,q,a],
    [q,a,q,a,q,a,q,a],
    [q,a,q,a,q,a,q,a],
    [q,a,a,q,a,a,q,a],
    [q,a,a,a,a,a,q,a],
    [q,a,a,a,a,a,q,a],
    [q,a,a,a,a,a,q,a]]


    character_N = [
    [a,a,a,a,a,a,a,a],
    [q,q,a,a,a,a,q,a],
    [q,a,q,a,a,a,q,a],
    [q,a,a,q,a,a,q,a],
    [q,a,a,a,q,a,q,a],
    [q,a,a,a,q,a,q,a],
    [q,a,a,a,a,q,q,a],
    [q,a,a,a,a,a,q,a]]


    character_O = [
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,q,a,a,a,q,a,a],
    [q,a,a,a,a,a,q,a],
    [q,a,a,a,a,a,q,a],
    [a,q,a,a,a,a,q,a],
    [a,q,q,a,a,q,a,a],
    [a,a,a,q,q,a,a,a]]


    character_P = [
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,q,q,q,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a]]


    character_Q = [
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,q,a,a,a,q,a,a],
    [q,a,a,a,a,a,q,a],
    [q,a,a,q,a,a,q,a],
    [q,a,a,a,q,a,q,a],
    [a,q,a,a,a,q,a,a],
    [a,a,q,q,a,a,q,a]]


    character_R = [
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,q,q,a,a,a],
    [a,q,q,a,a,a,a,a],
    [a,q,a,q,a,a,a,a],
    [a,q,a,a,q,q,a,a]]


    character_S = [
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,q,q,a,a],
    [a,q,a,a,a,a,q,a],
    [a,q,a,a,a,a,a,a],
    [a,q,q,q,q,a,a,a],
    [a,a,a,a,a,q,a,a],
    [a,q,a,a,a,a,q,a],
    [a,a,q,q,q,q,a,a]]


    character_T = [
    [a,a,a,a,a,a,a,a],
    [a,q,q,q,q,q,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a]]


    character_U = [
    [a,a,a,a,a,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,a,q,q,q,a,a,a]]


    character_V = [
    [a,a,a,a,a,a,a,a],
    [q,a,a,a,a,a,q,a],
    [a,q,a,a,a,a,q,a],
    [a,q,a,a,a,q,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,q,a,q,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a]]


    character_W = [
    [a,a,a,a,a,a,a,a],
    [q,a,a,a,a,a,q,a],
    [q,a,a,a,a,a,q,a],
    [q,a,a,a,a,a,q,a],
    [q,a,a,a,a,a,q,a],
    [q,a,a,q,a,a,q,a],
    [a,q,a,q,a,q,a,a],
    [a,a,q,a,q,a,a,a]]


    character_X = [
    [a,a,a,a,a,a,a,a],
    [q,a,a,a,a,a,q,a],
    [a,q,a,a,a,q,a,a],
    [a,a,q,a,q,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,q,a,q,a,a,a],
    [a,q,a,a,a,q,a,a],
    [q,a,a,a,a,a,q,a]]


    character_Y = [
    [a,a,a,a,a,a,a,a],
    [a,q,a,a,a,a,q,a],
    [a,q,a,a,a,a,q,a],
    [a,a,q,a,a,a,q,a],
    [a,a,a,q,q,q,a,a],
    [a,a,a,a,a,a,q,a],
    [a,a,a,a,a,a,q,a],
    [a,a,q,q,q,q,a,a]]


    character_Z = [
    [a,a,a,a,a,a,a,a],
    [a,q,q,q,q,q,a,a],
    [a,a,a,a,a,q,a,a],
    [a,a,a,a,q,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,q,q,q,q,a,a]]


    character_plus = [
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [q,q,q,q,q,q,q,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,a,a,a,a,a]]


    character_a = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,a,a,a,a],
    [a,q,a,a,q,a,a,a],
    [a,q,a,a,q,a,a,a],
    [a,q,a,a,q,a,q,a],
    [a,a,q,q,a,q,a,a]]


    character_b = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,a,q,q,a,a,a]]


    character_c = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,a,q,q,q,a,a,a]]


    character_d = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,q,a,a,a],
    [a,a,a,a,q,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,q,a,a,q,a,a,a],
    [a,q,a,a,q,a,a,a],
    [a,a,q,q,a,q,a,a]]


    character_e = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,a,a,a,a],
    [a,q,a,a,q,a,a,a],
    [a,q,q,q,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,a,q,q,q,a,a,a]]


    character_f = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,q,a,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,q,q,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,q,a,a,a,a,a,a]]


    character_g = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,a,a,a,a],
    [a,q,a,a,q,a,a,a],
    [a,a,q,q,a,a,a,a],
    [a,a,a,a,q,a,a,a],
    [a,a,a,a,q,a,a,a],
    [a,a,q,q,a,a,a,a]]


    character_h = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,q,q,a,a,a],
    [a,q,q,a,q,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a]]


    character_i = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,a,q,q,a,a,a,a]]


    character_j = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,q,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,q,a,a],
    [a,a,a,a,a,q,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,q,q,q,a,a,a]]


    character_k = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,q,a,q,a,a,a],
    [a,a,q,q,a,a,a,a],
    [a,a,q,a,q,a,a,a],
    [a,a,q,a,a,q,a,a]]


    character_l = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,a,q,q,a,a,a]]


    character_m = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,q,a,q,a,a,a],
    [a,q,a,q,a,q,a,a],
    [a,q,a,q,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a]]


    character_n = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,q,a,q,q,a,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,q,a,a,q,a,a]]


    character_o = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,q,a,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,a,q,q,a,a,a]]


    character_p = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,q,a,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,q,q,q,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,q,a,a,a,a,a]]


    character_q = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,q,a,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,a,q,q,q,a,a],
    [a,a,a,a,a,q,a,a],
    [a,a,a,a,a,q,q,a]]


    character_r = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,q,a,a,q,a,a,a],
    [a,a,q,q,a,q,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,q,a,a,a,a,a]]


    character_s = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,q,q,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,a,q,q,a,a,a],
    [a,a,a,a,a,q,a,a],
    [a,a,q,q,q,a,a,a]]


    character_t = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,q,q,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,a,q,q,q,a,a,a]]


    character_u = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,q,a,q,a,a,q,a],
    [a,a,a,q,a,a,q,a],
    [a,a,a,q,a,a,q,a],
    [a,a,a,a,q,q,a,a]]


    character_v = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,a,q,a,q,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a]]


    character_w = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,q,a,q,a,a],
    [a,q,a,q,a,q,a,a],
    [a,a,q,a,q,a,a,a]]


    character_x = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,a,q,a,q,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,q,a,q,a,a,a],
    [a,q,a,a,a,q,a,a]]


    character_y = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,q,a,a,q,a,a,a],
    [a,q,a,a,q,a,a,a],
    [a,a,q,q,a,a,a,a],
    [a,a,a,a,q,a,a,a],
    [a,q,q,q,a,a,a,a]]

    character_z = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,q,q,a,a],
    [a,a,a,a,a,q,a,a],
    [a,a,a,a,q,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,q,q,q,q,a,a]]


    character_arrow_left = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [q,a,q,q,q,q,q,a],
    [a,q,a,a,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,a,q,a,a,a,a]]


    character_arrow_right = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,q,a,a,a],
    [a,a,a,a,a,q,a,a],
    [a,a,a,a,a,a,q,a],
    [q,q,q,q,q,q,a,q],
    [a,a,a,a,a,a,q,a],
    [a,a,a,a,a,q,a,a],
    [a,a,a,a,q,a,a,a]]


    character_arrow_down = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [q,a,a,q,a,a,q,a],
    [a,q,a,q,a,q,a,a],
    [a,a,q,a,q,a,a,a],
    [a,a,a,q,a,a,a,a]]


    character_arrow_up = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,q,a,q,a,a,a],
    [a,q,a,q,a,q,a,a],
    [q,a,a,q,a,a,q,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a]]


    character_exclaim = [
    [a,a,a,q,a,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,q,q,q,a,a,a]]


    character_- = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,q,q,q,q,q,q,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a]]


    character_ = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,q,q,q,q,q,q,a],
    [a,a,a,a,a,a,a,a]]


    character_stop = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,a,a,q,a,a,a,a]]


    character_divide = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,q,a,a,a],
    [a,a,a,q,q,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,q,q,q,q,q,q,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,q,a,a,a],
    [a,a,a,q,q,a,a,a]]


    character_ = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a]]


    character_ = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,q,a,a,a],
    [a,a,q,q,q,q,a,a],
    [a,a,a,q,q,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a]]


    character_pound = [
    [a,a,a,a,q,q,a,a],
    [a,a,a,q,a,a,q,a],
    [a,a,q,a,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,q,q,a,a,a,a,a],
    [q,a,q,a,a,a,a,a],
    [a,q,a,q,q,q,q,a]]


    character_1 = [
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,a,a,a,a],
    [a,q,a,q,q,a,a,a],
    [a,a,a,q,q,a,a,a],
    [a,a,a,q,q,a,a,a],
    [a,a,a,q,q,a,a,a],
    [a,a,a,q,q,a,a,a],
    [a,q,q,q,q,q,a,a]]


    character_2 = [
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,a,a,a,q,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,q,q,q,q,a,a]]


    character_3 = [
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,a,a,a,q,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,a,q,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,a,q,q,q,a,a,a]]


    character_4 = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,w,w,a,a,a],
    [a,a,w,a,w,a,a,a],
    [a,w,a,a,w,a,a,a],
    [a,w,w,w,w,w,a,a],
    [a,a,a,a,w,a,a,a],
    [a,a,a,a,w,a,a,a],
    [a,a,a,a,w,a,a,a]]


    character_5 = [
    [a,a,a,a,a,a,a,a],
    [a,w,w,w,w,w,a,a],
    [a,w,a,a,a,a,a,a],
    [a,w,a,w,w,a,a,a],
    [a,w,w,a,a,w,a,a],
    [a,a,a,a,a,w,a,a],
    [a,w,a,a,a,w,a,a],
    [a,a,w,w,w,a,a,a]]


    character_6 = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,w,w,a,a,a],
    [a,a,w,a,a,a,a,a],
    [a,w,a,a,a,a,a,a],
    [a,w,a,w,w,a,a,a],
    [a,w,w,a,a,w,a,a],
    [a,a,w,a,a,w,a,a],
    [a,a,a,w,w,a,a,a]]


    character_7 = [
    [a,a,a,a,a,a,a,a],
    [a,w,w,w,w,a,a,a],
    [a,a,a,a,a,w,a,a],
    [a,a,a,a,a,w,a,a],
    [a,a,a,a,w,a,a,a],
    [a,a,a,w,a,a,a,a],
    [a,a,w,a,a,a,a,a],
    [a,w,a,a,a,a,a,a]]


    character_8 = [
    [a,a,a,a,a,a,a,a],
    [a,a,w,w,w,a,a,a],
    [a,w,a,a,a,w,a,a],
    [a,a,w,w,w,a,a,a],
    [a,w,a,a,a,w,a,a],
    [a,w,a,a,a,w,a,a],
    [a,w,a,a,a,w,a,a],
    [a,a,w,w,w,a,a,a]]


    character_9 = [
    [a,a,a,a,a,a,a,a],
    [a,a,w,w,w,a,a,a],
    [a,w,a,a,a,w,a,a],
    [a,w,a,a,w,w,a,a],
    [a,a,w,w,a,w,a,a],
    [a,a,a,a,a,w,a,a],
    [a,a,a,a,w,a,a,a],
    [a,a,a,w,a,a,a,a]]

    character_0 = [
    [a,a,a,a,a,a,a,a],
    [a,a,w,w,w,a,w,a],
    [a,w,a,a,a,w,a,a],
    [a,w,a,a,w,w,a,a],
    [a,w,a,w,a,w,a,a],
    [a,a,w,a,a,w,a,a],
    [a,w,a,w,w,a,a,a],
    [a,a,a,a,a,a,a,a]]


    character_0 = [
    [a,a,a,a,a,a,a,a],
    [a,a,w,w,w,a,w,a],
    [a,w,a,a,a,w,a,a],
    [a,w,a,a,w,w,a,a],
    [a,w,a,w,a,w,a,a],
    [a,a,w,a,a,w,a,a],
    [a,w,a,w,w,a,a,a],
    [a,a,a,a,a,a,a,a]]


    character_ = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a]]

