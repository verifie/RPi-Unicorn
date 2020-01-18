# characters

# ---------------------------------------------------------------------------------

# Define characters in typeface definitions.
def callCharacters():

    print("Function : callCharacters")

    typeface_characters = [
        'character_smiley',
        'character_smiley_cheeky',
        'character_poppy',
        'character_A',
        'character_B',
        'character_C',
        'character_D',
        'character_E',
        'character_G',
        'character_H',
        'character_I',
        'character_J',
        'character_K',
        'character_L',
        'character_M',
        'character_N',
        'character_O',
        'character_P',
        'character_Q',
        'character_R',
        'character_S',
        'character_T',
        'character_U',
        'character_V',
        'character_W',
        'character_Y',
        'character_Z',
        'character_a',
        'character_b',
        'character_c',
        'character_d',
        'character_e',
        'character_f',
        'character_g',
        'character_h',
        'character_i',
        'character_j',
        'character_k',
        'character_l',
        'character_m',
        'character_n',
        'character_o',
        'character_p',
        'character_q',
        'character_r',
        'character_s',
        'character_t',
        'character_u',
        'character_v',
        'character_w',
        'character_x',
        'character_y',
        'character_z',
        'character_0',
        'character_1',
        'character_2',
        'character_3',
        'character_4',
        'character_5',
        'character_6',
        'character_7',
        'character_8',
        'character_9',
        'character_arrow_up',
        'character_arrow_down',
        'character_arrow_left',
        'character_arrow_right',
        'character_exclaim',
        'character_add',
        'character_divide',
        'character_subtract',
        'character_multiply',
        'character_space',
        'character_dash',
        'character_dot',
        'character_pound']


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

    # Define typeface 'characters.


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


    character_dash = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,q,q,q,q,q,q,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a]]


    character__ = [
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


    character_space = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a]]


    character_dot = [
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

