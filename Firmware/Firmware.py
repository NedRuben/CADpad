import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.rgb import RGB

# ----------------------------
# Keyboard instance
# ----------------------------
keyboard = KMKKeyboard()

# ----------------------------
# Macros module
# ----------------------------
macros = Macros()
keyboard.modules.append(macros)

# ----------------------------
# Key pins (order = physical order)
# ----------------------------
PINS = (
    board.GP3,  # Key 1
    board.GP4,  # Key 2
    board.GP2,  # Key 3
    board.GP1,  # Key 4
    board.GP0,  # Key 5
    board.GP7,  # Key 6
)

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,  # buttons to GND (internal pull-ups)
)

# ----------------------------
# Keymap (Map the keys yourself)
# ----------------------------
keyboard.keymap = [
    [
        KC.MUTE,
        KC.VOLDOWN,
        KC.VOLUP,
        KC.MACRO("Hello world!"),
        KC.ENTER,
        KC.ESCAPE,
    ]
]

# ----------------------------
# RGB (4x SK6812 Mini)
# ----------------------------
rgb = RGB(
    pixel_pin=board.GP6,
    num_pixels=4,
    val_limit=120,  # brightness limit
)
keyboard.extensions.append(rgb)

# ----------------------------
# Start KMK
# ----------------------------
if __name__ == '__main__':
    keyboard.go()
