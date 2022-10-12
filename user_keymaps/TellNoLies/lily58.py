from kb import KMKKeyboard

from kmk.extensions.layers import Layers
from kmk.keys import KC
from kmk.modules.modtap import ModTap
from kmk.modules.split import Split, SplitType
from kmk.modules.media_keys import MediaKeys

keyboard = KMKKeyboard()
media_keys = MediaKeys()
layers = Layers()
modtap = ModTap()
split = Split(Split_type=SplitType.UART)

keyboard.modules = [modtap, layers, media_keys, split]

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

LOWER = KC.MO(1)
RAISE = KC.MO(2)
ADJUST = KC.LT(3, KC.SPC)
GAMEA = KC.LT(4)
GAMEB = KC.MO(5)
UNDO = KC.LCTL(KC.Z)
CUT = KC.LCTL(KC.X)
COPY = KC.LCTL(KC.C)
PASTE = KC.LCTL(KC.V)
SAVE = KC.LCTL(KC.S)
WB = KC.LALT(KC.LEFT)
WF = KC.LALT(KC.RGHT)
REF = KC.F5


# Adding extensions

# TODO Comment one of these on each side
# Left is 0, Right is 1
split_side = 0
split_side = 1

layers_ext = Layers()

extensions = [layers_ext, split]

keyboard.keymap = [
    [  #COLEMAK
        KC.TAB,    KC.Q,    KC.W,    KC.F,    KC.P,    KC.G,                         KC.J,  KC.L,    KC.U,    KC.Y,    KC.SCLN, KC.BSLS,\
        KC.BSPC,   KC.A,    KC.R,    KC.S,    KC.T,    KC.D,                         KC.H,  KC.N,    KC.E,    KC.I,    KC.O,    KC.QUOT,\
        KC.LSFT,   KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                         KC.N,  KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.ENT,\
        KC.LCTL,   KC.LALT, KC.LGUI, KC.C,    KC.V,    KC.B, KC.ESC,       KC.MPLY,  KC.MPRV, KC.MNXT, KC.VOLD, KC.MUTE, KC.VOLU, KC.RGUI,\
                            KC.MEH, ADJUST,   LOWER,  KC.SPC,         KC.SPC, RAISE, KC.LT(4), ADJUST,
    ],
    [  #LOWER
        XXXXXXX, KC.PGUP, KC.HOME, KC.UP,   KC.END,  KC.INS,                      KC.LNUM, KC.KP_7, KC.KP_8, KC.KP_9, KC.PSLS, KC.PAST,\
        KC.DEL,  KC.PGDN, KC.LEFT, KC.DOWN, KC.RGHT, KC.MPRV,                     KC.MNXT, KC.KP_4, KC.KP_5, KC.KP_6, KC.PMNS, KC.PPLS,\
        KC.LSFT, UNDO,    CUT,     COPY,    PASTE,   KC.REF,                      KC.KP_0, KC.KP_1, KC.KP_2, KC.KP_3, KC.PEQL, KC.PENT,\
        KC.LCTL, XXXXXXX, XXXXXXX, SAVE,    KC.WB,   KC.WF,  KC.PSCR,    KC.LCAP, KC.RBRC,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,\
                            KC.TRNS,    KC.LGUI, LOWER,  ADJUST,    KC.SPC,   RAISE,  KC.RALT, KC.TRNS,
    ],
    [  #RAISE
        KC.TILD,  KC.EXLM, KC.AT, KC.HASH,  KC.DLR,   KC.PERC,                        KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, KC.PIPE,\
        KC.GRAVE, KC.NO,   KC.NO, KC.QUES,  KC.COLN,  KC.LPRN,                        KC.RPRN, KC.UNDS, KC.MINS, KC.PLUS, KC.EQL,  KC.QUOT,\
        KC.LCTL,  KC.NO,   KC.NO, KC.LT,    KC.GT,    KC.RCBR,                        KC.LCBR,  KC.EQL, KC.LCBR, KC.RCBR, KC.PIPE, KC.GRV,\
        UNDO,     CUT,     COPY,  PASTE,    SAVE,     KC.LBRC, KC.LPRN,     KC.RPRN,  KC.RBRC, KC.PLUS, KC.LBRC, KC.RBRC, KC.BSLS, KC.TILD,\
                            KC.TRNS,    KC.LGUI,  LOWER,  ADJUST,       KC.ENT, RAISE,  KC.RALT, KC.TRNS,
    ],
        [  #GAMEA
        KC.TAB,   KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                      KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   XXXXXXX,\
        KC.BSPC,  KC.Q,    KC.W,    KC.F,    KC.P,    KC.G,                       KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, KC.BSPC,\
        KC.LCTL,  KC.A,    KC.R,    KC.S,    KC.T,    KC.D,                       KC.MINS, KC.EQL,  KC.LCBR, KC.RCBR, KC.PIPE, KC.GRV,\
        KC.LSFT,  KC.Z,    KC.X,    KC.C,    KC.V,    KC.B, KC.ESC,    XXXXXXX,   KC.UNDS, KC.PLUS, KC.LBRC, KC.RBRC, KC.BSLS, KC.TILD,\
                            KC.TRNS,     LOWER,   KC.MO(4), KC.SPC,    KC.SPC, RAISE,  KC.RALT, XXXXXXX,
    ],
        [  #GAMEB
        KC.ESC,  KC.N6,   KC.N7,  KC.N8,    KC.N9,   KC.N0,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
        KC.BSPC, KC.J,    KC.L,   KC.U,     KC.Y,    KC.SCLN,                      XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
        KC.LSFT, KC.H,    KC.N,   KC.E,     KC.I,    KC.O,                         XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
        KC.LCTL, KC.N,    KC.M,   KC.COMM,  KC.DOT,  KC.SLSH, XXXXXXX,    XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
                                KC.TRNS, KC.LGUI,   KC.TRNS,  LOWER,     KC.ENT,   RAISE,  KC.RALT, XXXXXXX,
    ],
    [  #ADJUST
        KC.F1,  KC.F2,  KC.F3,  KC.F4,  KC.F5,  KC.F6,                        KC.F7,  KC.F8, KC.F9, KC.F10, KC.F11, KC.F12,\
        KC.F13, KC.F14, KC.F15, KC.F16, KC.F17, KC.F18,                       KC.F19, KC.F20, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,     XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
                            KC.TRNS, KC.LGUI,   KC.MO(5),  KC.SPC,     KC.ENT,   RAISE,  KC.RALT, XXXXXXX,
    ]
]

if __name__ == '__main__':
    keyboard.go()
