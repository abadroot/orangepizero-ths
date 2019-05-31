from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageFont, ImageDraw

device = ssd1306(port=0, address=0x3C)  # rev.1 users set port=0
with canvas(device) as draw:
    font = ImageFont.load_default()
    draw.text((0, 0), "Hello World", font=font, fill=255)
