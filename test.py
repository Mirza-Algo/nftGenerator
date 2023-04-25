from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
img = Image.open("./images/0_bg/face_1.png")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('f.ttf', size=100)

width,height= draw.textsize("Sample Text asoincoiud wiuovniurnvure iufnv vuirn rnvuv ernvuineruv iuernv", font=font)
#draw.text((100-width/2, 100),"Sample Text",(255,255,255),font=font)
draw.multiline_text((100, 100),"Sample Text asoincoiud wiuovniurnvure iufnv vuirn rnvuv ernvuineruv iuernv",(255,255,255),font=font, align='center')
img.save('sample-out.png')