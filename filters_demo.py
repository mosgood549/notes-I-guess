from PIL import Image

from random import randint

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

#def violet_haze(image):
#    img = Image.open(image)
#    img.show() 
#    pixmap = img.load()
#    
#    for i in range(img.size[0]):
#        for j in range(img.size[1]):
#            r, g, b = pixmap[i,j]
#            r += 100
#            g -= 50
#            b += 500
#        
#            pixmap[i,j] = (r,g,b)
#    for i in range(img.size[0]):
#        for j in range(0,img.size[1],20):
#            r, g, b = pixmap[i,j]
#            r += 10*5
#            g += 10*2
#            b += 10
#        
#            pixmap[i,j] = (b,g,b)
#    img.show()
#    img.save("violet_filter.jpg")
#
def pointillism(image):
    img = Image.open(image)
    img.show() 
    pixmap = img.load()

    
    for i in range(img.size[0]):
        for j in range(0,img.size[1]):
            r, g, b = pixmap[i,j]
            r += randint(100,150)
            g += randint(50,150)
            b += randint(50,200)
        
            pixmap[i,j] = (r,g,b)
    
    img.show()
    img.save("point_filter.jpg")
    
    





def mirror_half(img):
    pixmap = img.load()
    for i in range(img.size[0]//2):
        for j in range(img.size[1]):
            pixmap[i,j] = pixmap[img.size[0]-1-i,j]
def top_switch(img):
    pixmap = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]//2):
            pixmap[i,j] = pixmap[i,img.size[1]-1-j]
            

def mirror(img):
    pixmap = img.load()
    mirror_half(img)
    top_switch(img)
             
    img.show()        
    img.save("mirror.jpg")
    

        
def main():
    pointillism("mountains.jpg")

#    img = Image.open("lighthouse.jpg")
#    img.show()
#    mirror(img)
    
    
if __name__ == "__main__":
    main()