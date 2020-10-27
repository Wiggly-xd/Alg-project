def getCoordinate():
    from PIL import Image
    import time
    #img=Image.open(r"img_shp/test.bmp")
    t0 = time.time()
    img=Image.open(r"img_shp/1406_S1_2020.bmp")
    pixVal=list(img.getdata())
    width, height=0,0
    for i in pixVal:
        cordinate = x, y = width, height
        width=width+1
        if width==1599:
            width=0
            height=height+1
        if i!=(0, 255, 0) and i!=(197, 224, 245):
            print(i)
            print(cordinate)
    t1 = time.time()
    total = t1-t0
    print(total/60)
getCoordinate()
