from PIL import Image, ImageDraw, ImageFont
import glob

gl = glob.glob('Icons/*.jpg')

for j in gl:
    image = Image.open(j)
    font = ImageFont.truetype('LiberationSans-BoldItalic.ttf', 65)
    image_editable = ImageDraw.Draw(image)
    name = j[6:]
    image_editable.text((5, 270), f"{'-'.join(x.capitalize() for x in name.split('-'))}"[:-4], (237, 230, 211), font)
    image.save(f"IconsEdited/{name}")
