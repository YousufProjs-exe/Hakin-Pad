
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.direct_pins = (
    board.D0,
    board.D1,
    board.D2,
    board.D3,
    board.D4,
    board.D5,
    board.D6,
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.Q,
        KC.W,
        KC.E,
        KC.R,
        KC.A,
        KC.S,
        KC.D,
    ]
]

if __name__ == "__main__":
    keyboard.go()
    