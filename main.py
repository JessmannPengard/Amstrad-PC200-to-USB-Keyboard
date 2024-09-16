import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP0,board.GP1,board.GP2,board.GP3,board.GP4,board.GP5,board.GP6,board.GP7)
keyboard.row_pins = (board.GP9,board.GP10,board.GP11,board.GP12,board.GP13,board.GP14,board.GP15,board.GP16,board.GP17,board.GP18,board.GP19,board.GP20,board.GP21)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Mapa de teclas
keymap = [
    [
    KC.ESC, KC.F1, KC.GRAVE, KC.N1, KC.TAB, KC.CAPSLOCK, KC.LSHIFT, KC.LCTRL,					#1
    KC.F2, KC.N3, KC.N2, KC.W, KC.Q, KC.A, KC.Z, KC.NUBS,										#2
    KC.F3, KC.F4, KC.N4, KC.E, KC.LALT, KC.D, KC.X, KC.S,										#3
    KC.F5, KC.N5, KC.R, KC.T, KC.F, KC.G, KC.C, KC.V,											#4
    KC.F6, KC.N6, KC.N7, KC.Y, KC.U, KC.H, KC.B, KC.N,											#5
    KC.F7, KC.N8, KC.I, KC.K, KC.J, KC.M, KC.COMMA, KC.SPACE,									#6
    KC.F8, KC.N9, KC.N0, KC.O, KC.P, KC.L, KC.SCOLON, KC.DOT,									#7
    KC.F9, KC.MINUS, KC.EQUAL, KC.LBRACKET, KC.RBRACKET, KC.QUOTE, KC.SLASH, KC.RALT,			#8
    KC.F10, KC.F11, KC.NO, KC.ENTER, KC.BSLASH, KC.RSHIFT, KC.LEFT, KC.RCTRL,					#9
    KC.F12, KC.PSCREEN, KC.BACKSPACE, KC.INSERT, KC.DELETE, KC.UP, KC.DOWN, KC.NO,				#10
    KC.SCROLLLOCK, KC.PAUSE, KC.HOME, KC.PGUP, KC.END, KC.PGDOWN, KC.RIGHT, KC.KP_0,			#11
    KC.NUMLOCK, KC.KP_SLASH, KC.KP_7, KC.KP_8, KC.KP_4, KC.KP_5, KC.KP_1, KC.KP_2,				#12
    KC.KP_ASTERISK, KC.KP_MINUS, KC.KP_9, KC.KP_PLUS, KC.KP_6, KC.KP_3, KC.KP_ENTER, KC.KP_DOT	#13
    ]
]

keyboard.keymap = keymap

if __name__ == '__main__':
    keyboard.go()
