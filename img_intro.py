from PIL import Image

#img = Image.new("RGB", (300,200))
#img.show()

#img = Image.new("RGB",(100,100),(255,0,0))
#img.show()



def smiley():
    img = Image.new("RGB",(100,100),(255,0,0))
    pixelmap = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if i > 60 and i <70:
                if j < 20 and j> 15:
                    pixelmap[i,j] = (255,255,255)
                if j < 65 and j >55:
                    pixelmap[i,j] = (255,255,255)
            if i > 60 and i < 70:
                if j < 70 and j >60:
                    pixelmap[i,j] = (0,0,0)
                if j < 30 and j >20:
                    pixelmap[i,j] = (0,0,0)
            if i > 30 and i < 40:
                if j <20 and j> 15:
                    pixelmap[i,j] = (0,0,0)
                if j < 80 and j > 75:
                    pixelmap[i,j] = (0,0,0)
            if i >30 and i <35:
                if j > 15 and j <80:
                    pixelmap[i,j] = (0,0,0)
                    
    img.show()
    img.save("my_image.jpeg")
    

def main():
    smiley()
    
    
if __name__ == "__main__":
    main()