from PIL import Image
img = Image.open('/home/coca/Desktop/teste.jpg')
out = Image.new(img.mode,(297,318))
print (img.mode)
xOrigin = 60
xDestin = 173
yOrigin = 123
yDestin = 268
w,h = (297,318)
for i in range (xOrigin,xDestin):
    for j in range (yOrigin,yDestin):
        r,g,b = img.getpixel((i,j))
        if r > 250 and g < 250 and b < 250 :
            #print (r,g,b)
            #print (i,j)
            out.putpixel((i,j), (r,g,b))

out.save('pontosPossivelmenteVermelhos.jpg','JPEG')
