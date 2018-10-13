from PIL import Image
import numpy as np
import time
import pdb

def print_elapsed_time(start_time, end_time):
    print("Elapsed time: " + str("{0:.2f}".format(end_time - start_time)))

def get_gray(r, g, b):
    return int((r * 0.299) + (g * 0.587) + (b * 0.114))

def sobel(input_img):
    width, height = input_img.size
    input_pixels = input_img.load()

    output_img = Image.new(input_img.mode, input_img.size)
    output_pixels = output_img.load()

    grayscaled = [[get_gray(input_pixels[i, j][0], input_pixels[i, j][1], input_pixels[i, j][2]) for j in range(height)] for i in range(width)]

    for x in range(1, width-1):
        for y in range(1, height-1):
            hor = int(-1*grayscaled[x-1][y-1] + -2*grayscaled[x][y-1] + -1*grayscaled[x+1][y-1] +
                    1*grayscaled[x-1][y+1] + 2*grayscaled[x][y+1] + 1*grayscaled[x+1][y+1])
            ver = int(-1*grayscaled[x-1][y-1] + -2*grayscaled[x-1][y] + -1*grayscaled[x-1][y+1] +
                    1*grayscaled[x+1][y-1] + 2*grayscaled[x+1][y] + 1*grayscaled[x+1][y+1])
            c = int(np.sqrt(hor*hor + ver*ver))

            output_pixels[x, y] = (c, c, c)
    return output_img