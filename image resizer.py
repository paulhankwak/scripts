import PIL
from PIL import Image
basewidth = 430
baseheight = 430
for x in range(0, 2+1):
    y = str(x)
    img = Image.open(y + '.png')
    if(img.size[0] <= img.size[1]):
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), PIL.Image.LANCZOS)
        img.save(y +'.png')
    if(img.size[0] > img.size[1]):
        img = Image.open(y + '.png')
        hpercent = (baseheight / float(img.size[1]))
        wsize = int((float(img.size[0]) * float(hpercent)))
        img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
        img.save(y +'.png')

print("done")
