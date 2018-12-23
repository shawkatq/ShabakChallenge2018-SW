#env 3.7 
from PIL import Image, ImageFont 
from pathlib import Path 
import textwrap 

def f(imgPath): 
    image = Image.open(imgPath) 
    red_band = image.split()[0] 
    xSize = image.size[0] 
    ySize = image.size[1] 
    newImage = Image.new("RGB", image.size) 
    imagePixels = newImage.load() 
    for i in range(xSize): 
        for j in range(ySize): 
            if bin(red_band.getpixel((i, j)))[-1] == '0':
                imagePixels[i, j] = (255, 255, 255) 
            else: 
                imagePixels[i, j] = (0,0,0) 
    newImgPath = str(Path(imgPath).parent.absolute()) 
    newImage.save(newImgPath + '/text.png')

f('clue.png')
