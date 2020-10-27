from PIL import Image
import time
#img=Image.open(r"img_shp/test.bmp")
t0 = time.time()
img=Image.open(r"img_shp/1406_S1_2020.bmp")

        #plt.imshow(img)

print("true")
pixVal=list(img.getdata())
#x, y = (img > 1000).nonzero()
#vals=img[x, y];
width, height=0,0
cordinates=width,height
Mwidth, Mheight = img.size
outside=0
Skogsmark=0
Vatten=0
Myrmark=0
houses=0
avverkad=0
stop=0
minHeight=1000000000
maxHeight=0
maxWidth=0
minWidth=1000000000
for i in pixVal:
    #if i==(90, 90, 160):
    #    break
    cordinate = x, y = width, height
    if(i==(0, 255, 0)):
        outside=outside+1
    elif(i==(204, 232, 182)):
        Skogsmark=Skogsmark+1
    elif(i==(197, 224, 245)):
        Vatten=Vatten+1
    elif(i==(242, 213, 199)):
        Myrmark=Myrmark+1
    elif(i==(224, 160, 128)):
        houses=houses+1
    else:
        avverkad=avverkad+1
    width=width+1
    if width==1599:
        width=0
        height=height+1
    if i!=(0, 255, 0) and i!=(197, 224, 245):
        if height<minHeight:
            minHeight=height
        if height>maxHeight:
            maxHeight=height
        if width<minWidth:
            minWidth=width
        if width>maxWidth:
            maxWidth=width  
        #print(i)
        #print(cordinate)
        #stop+=1

size=Mwidth*Mheight
print("outside ",outside)
print("Skogsmark ",Skogsmark)
print("Vatten ",Vatten)
print("Myrmark ",Myrmark)
print("hus ",houses)
print("avverkad ",avverkad)
print("total size ",size)
print("Inte med ",size-outside-Skogsmark-Vatten-Myrmark-houses-avverkad)
print(maxWidth)
print(maxHeight)
print(minWidth)
print(minHeight)
print("Bred",maxWidth-minWidth)  
t1 = time.time()
total = t1-t0
print(total/60)
#6400000
#40000