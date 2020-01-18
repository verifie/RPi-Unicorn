# characters

# ---------------------------------------------------------------------------------

# Define characters in typeface definitions.
def callCharacters():

    print("Function : callCharacters")

    self.typeface_characters = [
        'self.character_smiley',
        'self.character_smiley_cheeky',
        'self.character_poppy',
        'self.character_A',
        'self.character_B',
        'self.character_C',
        'self.character_D',
        'self.character_E',
        'self.character_G',
        'self.character_H',
        'self.character_I',
        'self.character_J',
        'self.character_K',
        'self.character_L',
        'self.character_M',
        'self.character_N',
        'self.character_O',
        'self.character_P',
        'self.character_Q',
        'self.character_R',
        'self.character_S',
        'self.character_T',
        'self.character_U',
        'self.character_V',
        'self.character_W',
        'self.character_Y',
        'self.character_Z',
        'self.character_a',
        'self.character_b',
        'self.character_c',
        'self.character_d',
        'self.character_e',
        'self.character_f',
        'self.character_g',
        'self.character_h',
        'self.character_i',
        'self.character_j',
        'self.character_k',
        'self.character_l',
        'self.character_m',
        'self.character_n',
        'self.character_o',
        'self.character_p',
        'self.character_q',
        'self.character_r',
        'self.character_s',
        'self.character_t',
        'self.character_u',
        'self.character_v',
        'self.character_w',
        'self.character_x',
        'self.character_y',
        'self.character_z',
        'self.character_0',
        'self.character_1',
        'self.character_2',
        'self.character_3',
        'self.character_4',
        'self.character_5',
        'self.character_6',
        'self.character_7',
        'self.character_8',
        'self.character_9',
        'self.character_arrow_up',
        'self.character_arrow_down',
        'self.character_arrow_left',
        'self.character_arrow_right',
        'self.character_exclaim',
        'self.character_add',
        'self.character_divide',
        'self.character_subtract',
        'self.character_multiply',
        'self.character_space',
        'self.character_dash',
        'self.character_dot',
        'self.character_pound']


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


    self.self.character_poppy = [
    [a,a,a,r,r,a,a,g],
    [a,a,r,r,r,g,g,g],
    [a,a,r,r,r,r,g,a],
    [r,r,r,a,a,r,r,r],
    [r,r,r,a,r,r,r,a],
    [a,r,r,r,r,r,a,a],
    [a,a,r,h,a,a,a,a],
    [a,a,a,h,a,a,a,a]]


    self.character_smiley_cheeky = [
    [a,a,b,b,b,b,b,a],
    [a,y,y,y,y,y,y,a],
    [y,y,a,n,y,a,n,y],
    [y,y,y,y,y,y,y,y],
    [y,y,y,y,y,y,y,y],
    [y,y,a,r,r,r,a,y],
    [a,y,y,r,r,r,y,a],
    [a,a,y,y,r,y,a,a]]


    self.character_smiley = [
    [a,a,a,a,a,a,a,a],
    [a,w,w,a,a,w,w,a],
    [a,w,n,a,a,n,w,a],
    [a,a,a,a,a,a,a,a],
    [a,w,a,a,a,a,w,a],
    [a,w,a,a,a,a,w,a],
    [a,a,w,w,w,w,a,a],
    [a,a,a,a,a,a,a,a]]


    self.character_A = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,q,a,q,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,q,q,q,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [q,q,q,a,q,q,q,a]]


    self.character_B = [
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,q,q,q,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,q,q,q,a,a,a]]


    self.character_C = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,q,q,a,a],
    [a,a,q,a,a,a,q,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,a,q,a,a,a,q,a],
    [a,a,a,q,q,q,a,a]]


    self.character_D = [
    [a,a,a,a,a,a,a,a],
    [a,q,q,q,a,a,a,a],
    [a,q,a,a,q,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,q,a,a,a],
    [a,q,q,q,a,a,a,a]]


    self.character_E = [
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,q,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,q,q,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,a,q,q,q,q,a,a]]


    self.character_F = [
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,q,q,q,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,q,q,q,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a]]


    self.character_G = [
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,q,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,q,q,q,a],
    [a,q,a,a,a,q,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,q,q,q,a,a,a]]


    self.character_H = [
    [a,a,a,a,a,a,a,a],
    [q,q,q,a,q,q,q,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,q,q,q,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [q,q,q,a,q,q,q,a]]


    self.character_I = [
    [a,a,a,a,a,a,a,a],
    [a,q,q,q,q,q,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,q,q,q,q,q,a,a]]


    self.character_J = [
    [a,a,a,a,a,a,a,a],
    [a,q,q,q,q,q,q,a],
    [a,a,a,a,q,a,a,a],
    [a,a,a,a,q,a,a,a],
    [a,a,a,a,q,a,a,a],
    [a,q,a,a,q,a,a,a],
    [a,q,a,a,q,a,a,a],
    [a,a,q,q,a,a,a,a]]


    self.character_K = [
    [a,a,a,a,a,a,a,a],
    [a,q,a,a,a,a,q,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,q,a,a,a],
    [a,q,q,q,a,a,a,a],
    [a,q,a,a,q,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,a,q,a]]


    self.character_L = [
    [a,a,a,a,a,a,a,a],
    [q,q,q,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,q,a],
    [a,q,q,q,q,q,q,a]]


    self.character_M = [
    [a,a,a,a,a,a,a,a],
    [q,q,a,a,a,q,q,a],
    [q,a,q,a,q,a,q,a],
    [q,a,q,a,q,a,q,a],
    [q,a,a,q,a,a,q,a],
    [q,a,a,a,a,a,q,a],
    [q,a,a,a,a,a,q,a],
    [q,a,a,a,a,a,q,a]]


    self.character_N = [
    [a,a,a,a,a,a,a,a],
    [q,q,a,a,a,a,q,a],
    [q,a,q,a,a,a,q,a],
    [q,a,a,q,a,a,q,a],
    [q,a,a,a,q,a,q,a],
    [q,a,a,a,q,a,q,a],
    [q,a,a,a,a,q,q,a],
    [q,a,a,a,a,a,q,a]]


    self.character_O = [
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,q,a,a,a,q,a,a],
    [q,a,a,a,a,a,q,a],
    [q,a,a,a,a,a,q,a],
    [a,q,a,a,a,a,q,a],
    [a,q,q,a,a,q,a,a],
    [a,a,a,q,q,a,a,a]]


    self.character_P = [
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,q,q,q,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a]]


    self.character_Q = [
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,q,a,a,a,q,a,a],
    [q,a,a,a,a,a,q,a],
    [q,a,a,q,a,a,q,a],
    [q,a,a,a,q,a,q,a],
    [a,q,a,a,a,q,a,a],
    [a,a,q,q,a,a,q,a]]


    self.character_R = [
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,q,q,a,a,a],
    [a,q,q,a,a,a,a,a],
    [a,q,a,q,a,a,a,a],
    [a,q,a,a,q,q,a,a]]


    self.character_S = [
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,q,q,a,a],
    [a,q,a,a,a,a,q,a],
    [a,q,a,a,a,a,a,a],
    [a,q,q,q,q,a,a,a],
    [a,a,a,a,a,q,a,a],
    [a,q,a,a,a,a,q,a],
    [a,a,q,q,q,q,a,a]]


    self.character_T = [
    [a,a,a,a,a,a,a,a],
    [a,q,q,q,q,q,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a]]


    self.character_U = [
    [a,a,a,a,a,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,a,q,q,q,a,a,a]]


    self.character_V = [
    [a,a,a,a,a,a,a,a],
    [q,a,a,a,a,a,q,a],
    [a,q,a,a,a,a,q,a],
    [a,q,a,a,a,q,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,q,a,q,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a]]


    self.character_W = [
    [a,a,a,a,a,a,a,a],
    [q,a,a,a,a,a,q,a],
    [q,a,a,a,a,a,q,a],
    [q,a,a,a,a,a,q,a],
    [q,a,a,a,a,a,q,a],
    [q,a,a,q,a,a,q,a],
    [a,q,a,q,a,q,a,a],
    [a,a,q,a,q,a,a,a]]


    self.character_X = [
    [a,a,a,a,a,a,a,a],
    [q,a,a,a,a,a,q,a],
    [a,q,a,a,a,q,a,a],
    [a,a,q,a,q,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,q,a,q,a,a,a],
    [a,q,a,a,a,q,a,a],
    [q,a,a,a,a,a,q,a]]


    self.character_Y = [
    [a,a,a,a,a,a,a,a],
    [a,q,a,a,a,a,q,a],
    [a,q,a,a,a,a,q,a],
    [a,a,q,a,a,a,q,a],
    [a,a,a,q,q,q,a,a],
    [a,a,a,a,a,a,q,a],
    [a,a,a,a,a,a,q,a],
    [a,a,q,q,q,q,a,a]]


    self.character_Z = [
    [a,a,a,a,a,a,a,a],
    [a,q,q,q,q,q,a,a],
    [a,a,a,a,a,q,a,a],
    [a,a,a,a,q,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,q,q,q,q,a,a]]


    self.character_plus = [
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [q,q,q,q,q,q,q,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,a,a,a,a,a]]


    self.character_a = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,a,a,a,a],
    [a,q,a,a,q,a,a,a],
    [a,q,a,a,q,a,a,a],
    [a,q,a,a,q,a,q,a],
    [a,a,q,q,a,q,a,a]]


    self.character_b = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,a,q,q,a,a,a]]


    self.character_c = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,a,q,q,q,a,a,a]]


    self.character_d = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,q,a,a,a],
    [a,a,a,a,q,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,q,a,a,q,a,a,a],
    [a,q,a,a,q,a,a,a],
    [a,a,q,q,a,q,a,a]]


    self.character_e = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,a,a,a,a],
    [a,q,a,a,q,a,a,a],
    [a,q,q,q,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,a,q,q,q,a,a,a]]


    self.character_f = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,q,a,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,q,q,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,q,a,a,a,a,a,a]]


    self.character_g = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,a,a,a,a],
    [a,q,a,a,q,a,a,a],
    [a,a,q,q,a,a,a,a],
    [a,a,a,a,q,a,a,a],
    [a,a,a,a,q,a,a,a],
    [a,a,q,q,a,a,a,a]]


    self.character_h = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,q,q,a,a,a],
    [a,q,q,a,q,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a]]


    self.character_i = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,a,q,q,a,a,a,a]]


    self.character_j = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,q,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,q,a,a],
    [a,a,a,a,a,q,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,q,q,q,a,a,a]]


    self.character_k = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,q,a,q,a,a,a],
    [a,a,q,q,a,a,a,a],
    [a,a,q,a,q,a,a,a],
    [a,a,q,a,a,q,a,a]]


    self.character_l = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,a,q,q,a,a,a]]


    self.character_m = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,q,a,q,a,a,a],
    [a,q,a,q,a,q,a,a],
    [a,q,a,q,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a]]


    self.character_n = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,q,a,q,q,a,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,q,a,a,q,a,a]]


    self.character_o = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,q,a,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,a,q,q,a,a,a]]


    self.character_p = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,q,a,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,q,q,q,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,q,a,a,a,a,a]]


    self.character_q = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,q,a,a,a],
    [a,a,q,a,a,q,a,a],
    [a,a,a,q,q,q,a,a],
    [a,a,a,a,a,q,a,a],
    [a,a,a,a,a,q,q,a]]


    self.character_r = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,q,a,a,q,a,a,a],
    [a,a,q,q,a,q,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,q,a,a,a,a,a]]


    self.character_s = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,q,q,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,a,q,q,a,a,a],
    [a,a,a,a,a,q,a,a],
    [a,a,q,q,q,a,a,a]]


    self.character_t = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,q,q,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,a,q,q,q,a,a,a]]


    self.character_u = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,q,a,q,a,a,q,a],
    [a,a,a,q,a,a,q,a],
    [a,a,a,q,a,a,q,a],
    [a,a,a,a,q,q,a,a]]


    self.character_v = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,a,q,a,q,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a]]


    self.character_w = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,a,a,q,a,a],
    [a,q,a,q,a,q,a,a],
    [a,q,a,q,a,q,a,a],
    [a,a,q,a,q,a,a,a]]


    self.character_x = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,a,q,a,q,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,q,a,q,a,a,a],
    [a,q,a,a,a,q,a,a]]


    self.character_y = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,q,a,a,q,a,a,a],
    [a,q,a,a,q,a,a,a],
    [a,a,q,q,a,a,a,a],
    [a,a,a,a,q,a,a,a],
    [a,q,q,q,a,a,a,a]]

    self.character_z = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,q,q,a,a],
    [a,a,a,a,a,q,a,a],
    [a,a,a,a,q,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,q,q,q,q,a,a]]


    self.character_arrow_left = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [q,a,q,q,q,q,q,a],
    [a,q,a,a,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,a,q,a,a,a,a]]


    self.character_arrow_right = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,q,a,a,a],
    [a,a,a,a,a,q,a,a],
    [a,a,a,a,a,a,q,a],
    [q,q,q,q,q,q,a,q],
    [a,a,a,a,a,a,q,a],
    [a,a,a,a,a,q,a,a],
    [a,a,a,a,q,a,a,a]]


    self.character_arrow_down = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [q,a,a,q,a,a,q,a],
    [a,q,a,q,a,q,a,a],
    [a,a,q,a,q,a,a,a],
    [a,a,a,q,a,a,a,a]]


    self.character_arrow_up = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,q,a,q,a,a,a],
    [a,q,a,q,a,q,a,a],
    [q,a,a,q,a,a,q,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,q,a,a,a,a]]


    self.character_exclaim = [
    [a,a,a,q,a,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,q,q,q,a,a,a]]


    self.character_dash = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,q,q,q,q,q,q,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a]]


    self.character__ = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,q,q,q,q,q,q,a],
    [a,a,a,a,a,a,a,a]]


    self.character_stop = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,a,a,q,a,a,a,a]]


    self.character_divide = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,q,a,a,a],
    [a,a,a,q,q,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,q,q,q,q,q,q,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,q,a,a,a],
    [a,a,a,q,q,a,a,a]]


    self.character_space = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a]]


    self.character_dot = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,q,q,a,a,a],
    [a,a,q,q,q,q,a,a],
    [a,a,a,q,q,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a]]


    self.character_pound = [
    [a,a,a,a,q,q,a,a],
    [a,a,a,q,a,a,q,a],
    [a,a,q,a,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,q,q,a,a,a,a,a],
    [q,a,q,a,a,a,a,a],
    [a,q,a,q,q,q,q,a]]


    self.character_1 = [
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,a,a,a,a],
    [a,q,a,q,q,a,a,a],
    [a,a,a,q,q,a,a,a],
    [a,a,a,q,q,a,a,a],
    [a,a,a,q,q,a,a,a],
    [a,a,a,q,q,a,a,a],
    [a,q,q,q,q,q,a,a]]


    self.character_2 = [
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,a,a,a,q,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,q,a,a,a,a,a],
    [a,q,a,a,a,a,a,a],
    [a,q,q,q,q,q,a,a]]


    self.character_3 = [
    [a,a,a,a,a,a,a,a],
    [a,a,q,q,q,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,a,a,a,q,a,a,a],
    [a,a,a,q,a,a,a,a],
    [a,a,a,a,q,a,a,a],
    [a,q,a,a,a,q,a,a],
    [a,a,q,q,q,a,a,a]]


    self.character_4 = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,w,w,a,a,a],
    [a,a,w,a,w,a,a,a],
    [a,w,a,a,w,a,a,a],
    [a,w,w,w,w,w,a,a],
    [a,a,a,a,w,a,a,a],
    [a,a,a,a,w,a,a,a],
    [a,a,a,a,w,a,a,a]]


    self.character_5 = [
    [a,a,a,a,a,a,a,a],
    [a,w,w,w,w,w,a,a],
    [a,w,a,a,a,a,a,a],
    [a,w,a,w,w,a,a,a],
    [a,w,w,a,a,w,a,a],
    [a,a,a,a,a,w,a,a],
    [a,w,a,a,a,w,a,a],
    [a,a,w,w,w,a,a,a]]


    self.character_6 = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,w,w,a,a,a],
    [a,a,w,a,a,a,a,a],
    [a,w,a,a,a,a,a,a],
    [a,w,a,w,w,a,a,a],
    [a,w,w,a,a,w,a,a],
    [a,a,w,a,a,w,a,a],
    [a,a,a,w,w,a,a,a]]


    self.character_7 = [
    [a,a,a,a,a,a,a,a],
    [a,w,w,w,w,a,a,a],
    [a,a,a,a,a,w,a,a],
    [a,a,a,a,a,w,a,a],
    [a,a,a,a,w,a,a,a],
    [a,a,a,w,a,a,a,a],
    [a,a,w,a,a,a,a,a],
    [a,w,a,a,a,a,a,a]]


    self.character_8 = [
    [a,a,a,a,a,a,a,a],
    [a,a,w,w,w,a,a,a],
    [a,w,a,a,a,w,a,a],
    [a,a,w,w,w,a,a,a],
    [a,w,a,a,a,w,a,a],
    [a,w,a,a,a,w,a,a],
    [a,w,a,a,a,w,a,a],
    [a,a,w,w,w,a,a,a]]


    self.character_9 = [
    [a,a,a,a,a,a,a,a],
    [a,a,w,w,w,a,a,a],
    [a,w,a,a,a,w,a,a],
    [a,w,a,a,w,w,a,a],
    [a,a,w,w,a,w,a,a],
    [a,a,a,a,a,w,a,a],
    [a,a,a,a,w,a,a,a],
    [a,a,a,w,a,a,a,a]]

    self.character_0 = [
    [a,a,a,a,a,a,a,a],
    [a,a,w,w,w,a,w,a],
    [a,w,a,a,a,w,a,a],
    [a,w,a,a,w,w,a,a],
    [a,w,a,w,a,w,a,a],
    [a,a,w,a,a,w,a,a],
    [a,w,a,w,w,a,a,a],
    [a,a,a,a,a,a,a,a]]


    self.character_0 = [
    [a,a,a,a,a,a,a,a],
    [a,a,w,w,w,a,w,a],
    [a,w,a,a,a,w,a,a],
    [a,w,a,a,w,w,a,a],
    [a,w,a,w,a,w,a,a],
    [a,a,w,a,a,w,a,a],
    [a,w,a,w,w,a,a,a],
    [a,a,a,a,a,a,a,a]]


    self.character_ = [
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a],
    [a,a,a,a,a,a,a,a]]

