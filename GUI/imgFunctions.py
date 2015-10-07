from PIL import Image, ImageFilter

#from numpy import *


"""
def gaussian_grid(size = 5):


    Create a square grid of integers of gaussian shape

    e.g. gaussian_grid() returns

    array([[ 1,  4,  7,  4,  1],

           [ 4, 20, 33, 20,  4],

           [ 7, 33, 55, 33,  7],

           [ 4, 20, 33, 20,  4],

           [ 1,  4,  7,  4,  1]])


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





im = Image.open('p2.jpg')

im1 = im.filter(GAUSSIAN)

im1.show()
"""

img = Image.open('p2.jpg')
img = img.filter(ImageFilter.FIND_EDGES)
w,h = img.size
pim = img.load()
pstack = []
limit = (50,50,50)

for j in range (0,h):
    for i in range (0,l):
        if pim[i,j] >= limit:


