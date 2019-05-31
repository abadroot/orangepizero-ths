from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageFont, ImageDraw

device = ssd1306(port=0, address=0x3C)  # rev.1 users set port=0
with canvas(device) as draw:
    draw.point((5,9),fill=255)
    draw.point((6,9),fill=255)
    draw.point((7,9),fill=255)
    draw.point((8,9),fill=255)
    draw.point((9,9),fill=255)
