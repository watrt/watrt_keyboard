import board

from kmk.extensions.LED import LED
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        super().__init__()

        self.col_pins = (
            board.GP15,
            board.GP16,
            board.GP14,
            board.GP17,
            board.GP13,
            board.GP18,
            board.GP12,
            board.GP19,
            board.GP11,
            board.GP20
        )

        self.row_pins = (
            board.GP0,
            board.GP1,
            board.GP2,
            board.GP3,
            board.GP4,
            board.GP5,
            board.GP6
        )

        self.diode_orientation = DiodeOrientation.COLUMNS

        self.leds = LED(led_pin=[board.GP10, board.GP21, board.GP22])
        self.extensions.append(self.leds)
