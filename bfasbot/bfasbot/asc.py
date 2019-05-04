import PIL
import PIL.Image
import PIL.ImageFont
import PIL.ImageOps
import PIL.ImageDraw
from io import *
import base64
# import magic

PIXEL_ON = 0  # PIL color to use for "on"
PIXEL_OFF = 255  # PIL color to use for "off"


from PIL import Image, ImageDraw
import numpy as np

def makeTrueColour(image):
   """
   Force image to TrueColour by 'slightly distorting' greys.
   Distortion means adding a tiny random amount of noise (0-N) to pixels that will not
   "burn out" (i.e. exceed 255) as a result, and also subtracting a similar tiny 
   random amount of noise from pixels  from pixels that will not underflow as a result.
   If N=1, this means less than 0.4% error - hopefully imperceptible.
   """

   N = 1
   w, h = image.size
   ni = np.array(image)

   # Mask of pixels that will not exceed 255 by adding N
   okpix = (ni <= (255 - N))
   # Make additive noise in those pixels
   noise = np.random.randint(0,N+1,size=(h,w,3),dtype=np.uint8) * okpix
   ni += noise

   # Mask of pixels big enough to subtract N
   okpix = (ni >= N)
   # Make subtractive noise in those pixels
   noise = np.random.randint(0,N+1,size=(h,w,3),dtype=np.uint8) * okpix
   ni -= noise

   return(Image.fromarray(ni))

def mains(image):
    image = Image.new(mode='RGB', size=(400, 400), color=(255,255,255))
    draw = ImageDraw.Draw(image)
    draw.line(xy=((100, 100), (300, 300)), fill=(0,0,0), width=5)

    tc = makeTrueColour(image)
    tc.save('imgs.jpg',subsample=0,quality=95)  

# This just counts the unique colours in "tc" - you don't need it
    T = np.array(tc)   
    print(len(np.unique(T.reshape(-1, T.shape[2]), axis=0)) )
  
def main(path):
    image = text_image(path)
    image.show()
    image.save('img.png')


def text_image(text_path, font_path=None):
    """Convert text file to a grayscale image with black characters on a white background.

    arguments:
    text_path - the content of this file will be converted to an image
    font_path - path to a font file (for example impact.ttf)
    """
    grayscale = 'L'
    # parse the file into lines
    with open(text_path) as text_file:  # can throw FileNotFoundError
        lines = tuple(l.rstrip() for l in text_file.readlines())

    # choose a font (you can see more detail in my library on github)
    large_font = 20  # get better resolution with larger size
    font_path = font_path or "arial.ttf"  # Courier New. works in windows. linux may need more explicit path
    try:
        font = PIL.ImageFont.truetype(font_path, size=large_font)
    except IOError:
        font = PIL.ImageFont.load_default()
        print('Could not use chosen font. Using default.')

    # make the background image based on the combination of font and lines
    pt2px = lambda pt: int(round(pt * 96.0 / 72))  # convert points to pixels
    max_width_line = max(lines, key=lambda s: font.getsize(s)[0])
    # max height is adjusted down because it's too large visually for spacing
    test_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    max_height = pt2px(font.getsize(test_string)[1])
    max_width = pt2px(font.getsize(max_width_line)[0])
    height = max_height * len(lines)  # perfect or a little oversized
    width = int(round(max_width + 40))  # a little oversized
    image = PIL.Image.new(grayscale, (width, height), color=PIXEL_OFF)
    draw = PIL.ImageDraw.Draw(image)

    # draw each line of text
    vertical_position = 5
    horizontal_position = 5
    line_spacing = int(round(max_height * 0.8))  # reduced spacing seems better
    for line in lines:
        draw.text((horizontal_position, vertical_position),
                  line, fill=PIXEL_ON, font=font)
        vertical_position += line_spacing
    # crop the text
    c_box = PIL.ImageOps.invert(image).getbbox()
    image = image.crop(c_box)
    return image


def convert_byte_stream_to_jpg(asciiString):
        f = open('ascii_image.jpg', 'wb')
        f.write(base64.b64decode(asciiString.replace('\n', ' ').replace('\r', '').replace('\t', '').replace(' ', '')))
        f.close()
        return base64.b64decode(asciiString.replace('\n', ' ').replace('\r', '').replace('\t', '').replace(' ', ''))

def convert_ascii_to_byte_stream(asciiString):
        return base64.b64decode(self.strip_all_whitespace(asciiString))
    # def get_encoding_type(self):
    #     m = magic.MAGIC_MIME
    #     m.from_bytes(self.convert_ascii_to_byte_stream(), 'little')
    #     return m.file('./' + self.file)
  
  
  
if __name__ == '__main__':
    import sys
    import urllib.request
    if sys.argv[1].startswith('http://') or sys.argv[1].startswith('https://'):
        urllib.request.urlretrieve(sys.argv[1], "asciify.jpg")
        path = "asciify.jpg"
    else:
        path = sys.argv[1]
    main(path)