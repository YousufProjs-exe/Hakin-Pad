
import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306

keyboard = KMKKeyboard()

# Hakin Pad key matrix (7)
keyboard.col_pins = (
    board.D0,
    board.D1,
    board.D2,
    board.D3,
    board.SCL,
)

# (ms)
keyboard.row_pins = (
    board.D6,
    board.D7,
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

layers = Layers()
keyboard.modules.append(layers)

keyboard.keymap = [
    [
        KC.Q, KC.W, KC.E, KC.R, KC.T,
        KC.A, KC.S,
        KC.TRNS, KC.TRNS, KC.TRNS,
    ],
    [
        KC.F1, KC.F2, KC.F3, KC.F4, KC.F5,
        KC.F6, KC.F7,
        KC.TRNS, KC.TRNS, KC.TRNS,
    ],
]

encoder_handler = EncoderHandler()

encoder_handler.pins = (
    (board.D6, board.D7),
    (board.D10, board.D9),
)

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),),
    ((KC.MPRV, KC.MNXT),),
]

keyboard.modules.append(encoder_handler)
keyboard.extensions.append(MediaKeys())

i2c = busio.I2C(board.SCL, board.SDA)

display_driver = SSD1306(
    i2c=i2c,
    device_address=0x3C,
)

display = Display(
    display=display_driver,
    width=128,
    height=32,
    brightness=0.8,
    entries=[
        TextEntry(text="HAKIN PAD", x=0, y=0),
        TextEntry(text="MODE 0", x=0, y=12, layer=0),
        TextEntry(text="MODE 1", x=0, y=12, layer=1),
        TextEntry(text="YSH", x=0, y=24),
    ],
)

keyboard.extensions.append(display)

if __name__ == "__main__":
    keyboard.go()
