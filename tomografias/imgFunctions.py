from PIL import Image, ImageFilter
from numpy import *
import sys


def gaussian_grid(size = 4):


    #Create a square grid of integers of gaussian shape

    #e.g. gaussian_grid() returns

    #array([[ 1,  4,  7,  4,  1],

           #[ 4, 20, 33, 20,  4],

           #[ 7, 33, 55, 33,  7],

           #[ 4, 20, 33, 20,  4],

           #[ 1,  4,  7,  4,  1]])


    m = size/2

    n = m+1  # remember python is 'upto' n in the range below

    x, y = mgrid[-m:n,-m:n]

    # multiply by a factor to get 1 in the corner of the grid

    # ie for a 5x5 grid   fac*exp(-0.5*(2**2 + 2**2)) = 1

    fac = exp(m**2)

    g = fac*exp(-0.5*(x**2 + y**2))

    return g.round().astype(int)



class GAUSSIAN(ImageFilter.BuiltinFilter):

    name = "Gaussian"

    gg = gaussian_grid().flatten().tolist()

    filterargs = (5,5), sum(gg), 0, tuple(gg)


def findBorder(image):
    toBePainted = image.copy()
    img = image.filter(GAUSSIAN)
    img = img.filter(ImageFilter.FIND_EDGES)
    w,h = img.size
    pim = img.load()
    limit = (50,50,50)

    #for j in range (0,h):
        #for i in range (0,w):
            #if pim[i,j] != (0,0,0):
                #pim[i,j] = (255,255,255)
    #img.show()

    for j in range (0,h):
        for i in range (0,w):
            if pim[i,j] > limit:
                pixels = paintBorder(img,(i,j))
                break
        else:
            continue
        break
    pim = toBePainted.load()
    for pixel in pixels:
        pim[pixel[0],pixel[1]] = (255,0,0)

    return toBePainted

    

def paintBorder(image,initPixel):
    limit = (0,0,0)
    w,h = image.size
    pim = image.load()
    pstack = [initPixel]
    processedPixels = set()
    while len(pstack) > 0:
        x,y = pstack.pop()
        if (x,y) not in processedPixels and x not in (0,w) and y not in (0,h):
            processedPixels.add((x,y))
            if pim[x,y] > limit:
                #pim[x,y] = (255,0,0)
                pstack.append((x + 1, y))
                pstack.append((x - 1, y))
                pstack.append((x, y + 1))
                pstack.append((x, y - 1))
            else:
                #pim[x,y] = (255,0,0)
                pass
    return processedPixels

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)
    img = Image.open(sys.argv[1])
    img = findBorder(img)
    img.show()
