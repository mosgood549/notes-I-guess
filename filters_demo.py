from PIL import Image

#img = Image.open("beach.jpg")
#
#img.show() #original image
#
#pixmap = img.load()
#
#r, g, b = pixmap[100,100]

#pixmap[100,100] = (255,255,255)

#k-mart
#for i in range(img.size[0]):
#    for j in range(img.size[1]):
#        r, g, b = pixmap[i,j]
#        r += 100
#        g -= 50
#        b -= 50
#        
#        pixmap[i,j] = (r,g,b)
#        

def violet_haze(image):
    img = Image.open(image)
    img.show() 
    pixmap = img.load()
    
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixmap[i,j]
            r += 100
            g -= 50
            b += 500
        
            pixmap[i,j] = (r,g,b)
    for i in range(img.size[0]):
        for j in range(0,img.size[1],20):
            r, g, b = pixmap[i,j]
            r += 10*5
            g += 10*2
            b += 10
        
            pixmap[i,j] = (b,g,b)
    img.show()
    img.save("violet_filter.jpg")
    

        
def main():
    violet_haze("beach.jpg")
    
    
if __name__ == "__main__":
    main()