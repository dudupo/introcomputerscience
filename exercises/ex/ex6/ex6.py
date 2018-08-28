from ex6_helper import load_image, show , save


def otsu(image):
    mean = lambda X : sum(X) / len(X) if len(X) > 0 else 0
    cost = lambda X , Y : len(X) * len(Y) * (( mean(X) - mean(Y) ) **2)

    optimth , optimcost = 0 , 0
    for th in range(256):
        blackpixels = []
        whitepixels = []
        for row in image:
            for pixel in row :
                 if pixel >= th :
                     blackpixels.append( pixel )
                 else :
                     whitepixels.append( pixel )
        if optimcost < cost(blackpixels , whitepixels) :
            optimth , optimcost = th , cost(blackpixels , whitepixels)
    return optimth

def threshold_filter(image):
    th = otsu(image)

    newimage = []
    for row in image:
        newimage.append([])
        for pixel in row :
            newimage[-1].append( 255 if pixel >= th else 0  )

    #save(newimage , "./test321.jpg")
    show(newimage )


def apply_filter(image, _filter):
    newimage = []
    for j ,row in enumerate(image):
        newimage.append([])
        for i , pixel in enumerate(row) :
            newimage[-1].append(0)
            for yhist in range (-1 , 2) :
                for xhist in range(-1 , 2) :
                    x = min( max( 0 , i + xhist ) , len(row) - 1)
                    y = min( max( 0,  j + yhist ) , len(image) - 1)
                    newimage[-1][-1] += image[y][x] * _filter[1 + yhist][1 + xhist]
            newimage[-1][-1] = min( int (abs( newimage[-1][-1]  )) , 255)
    return newimage

def detect_edges(image):
    _filter = [[ -0.125 for i in range(3)] for j in range(3)]
    _filter[1][1] = 1
    return apply_filter(image , _filter)

def downsample_by_3(image):
    _filter = [[ float( 1 / 9  ) for _ in range(3)] for __ in range(3)]
    newimage = []
    meanimage = apply_filter(image , _filter)
    for j in range(1 ,  len(image) , 3) :
        newimage.append([])
        for i in range ( 1 , len(image[j]) , 3):
             newimage[-1].append( meanimage[j][i])
    return newimage

def downsample(image, max_diagonal_size):

    def diagonal(image):
        return  int((len(image) ** 2 + len(image[0])**2) ** 0.5)
    newimage = image
    while ( diagonal(newimage) > max_diagonal_size ):
        newimage = downsample_by_3( newimage )
    return  newimage

from math import pi
'''
def get_angle(image):
    for angle in range( 0 , pi / 2 , 1 / (2*pi)  ) :
        for distance in range(0 , len(image) / (2 ** 0.5) , 0.1 ):
            lines , newline = [] , True
            for pixel in pixels_on_line(image, angle, distance, top=True):
                if pixel == 0 :
                    if newline :
                        lines.append([])
                        newline = False
                    lines[-1].append( pixel )
                else:
                    newline = True
            weight = 0
            for line in lines:
                weight += len(line) ** 2
'''

import os
if __name__ == "__main__" :
    args = os.sys.argv

    show( downsample_by_3(load_image( args[1 ])))
