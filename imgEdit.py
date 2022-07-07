from PIL import Image, ImageDraw, ImageFont
import glob

gl = glob.glob('Icons/*.jpg')

for jpg in gl:
    image = Image.open(jpg)
    font = ImageFont.truetype('LiberationSans-BoldItalic.ttf', 65)
    image_editable = ImageDraw.Draw(image)
    name = jpg[6:]
    image_editable.text((5, 270), f"{'-'.join(x.capitalize() for x in name.split('-'))}"[:-4], (237, 230, 211), font)
    image.save(f"IconsEdited/{name}")
