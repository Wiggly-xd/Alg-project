from PIL import Image
import time
def getCoordinate():
    coordinate=[]
    color=[]
    arrays=[]
    #img=Image.open(r"img_shp/test.bmp")
    t0 = time.time()
    img=Image.open(r"img_shp/1406_S1_2021.bmp")
    pixVal=list(img.getdata())
    width, height=0,0
    for i in pixVal:
        cordinate = width, height
        width=width+1
        if width==1346:
            width=0
            height=height+1
        if i!=(0, 255, 0) and i!=(197, 224, 245):
            color.append(i)
            coordinate.append(cordinate)
    t1 = time.time()
    total = t1-t0
    print(total/60)
    arrays.append(coordinate)
    arrays.append(color)
    return arrays
CoordinateColor=getCoordinate()
for x in CoordinateColor[0]:
    print(x)