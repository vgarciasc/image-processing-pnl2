from PIL import Image
from math import *
import numpy as np
import pdb

def print_elapsed_time(start_time, end_time):
    print("Elapsed time: " + str("{0:.2f}".format(end_time - start_time)))

def get_gray(r, g, b):
    return int((r * 0.299) + (g * 0.587) + (b * 0.114))

def get_gaussian_mask(size, sigma):
    bx = np.arange(- size // 2 + 1.0, size // 2 + 1.0)
    kernel = np.exp(- (bx * bx) / (2.0 * (sigma * sigma)))
    kernel = kernel / np.sum(kernel)
    return kernel

def gaussian_blur(input_img, size, sigma):
    width, height = input_img.size
    input_pixels = input_img.load()

    output_img = Image.new(input_img.mode, input_img.size)
    output_pixels = output_img.load()

    gaussian_values = get_gaussian_mask(size, sigma)

    #Horizontal pass
    for x in range(0, width-1):
        for y in range(0, height-1):
            r = 0
            g = 0
            b = 0

            for i in range(0, len(gaussian_values)):
                x_pass = x - floor(len(gaussian_values)/2) + i
                if x_pass >= 0 and x_pass <= width - 1:
                    r += input_pixels[x_pass, y][0] * gaussian_values[i]
                    g += input_pixels[x_pass, y][1] * gaussian_values[i]
                    b += input_pixels[x_pass, y][2] * gaussian_values[i]
                
            output_pixels[x, y] = (int(r), int(g), int(b))

    #Vertical pass    
    for x in range(1, width-1):
        for y in range(0, height-1):
            r = 0
            g = 0
            b = 0

            for j in range(0, len(gaussian_values)):
                y_pass = y - floor(len(gaussian_values)/2) + j
                if y_pass >= 0 and y_pass <= height - 1:
                    r += output_pixels[x, y_pass][0] * gaussian_values[j]
                    g += output_pixels[x, y_pass][1] * gaussian_values[j]
                    b += output_pixels[x, y_pass][2] * gaussian_values[j]
                
            input_pixels[x, y] = (int(r), int(g), int(b))

    return input_img 

def prewitt(input_img, with_gaussian_blur=False, gaussian_size = 5, gaussian_sigma = 1.0, threshold = -1):
    if with_gaussian_blur:
        input_img = gaussian_blur(input_img, gaussian_size, gaussian_sigma)

    width, height = input_img.size
    input_pixels = input_img.load()

    output_img = Image.new(input_img.mode, input_img.size)
    output_pixels = output_img.load()

    grayscaled = [[get_gray(input_pixels[i, j][0], input_pixels[i, j][1], input_pixels[i, j][2]) for j in range(height)] for i in range(width)]

    for x in range(1, width-1):
        for y in range(1, height-1):
            mask_1 = int(1*grayscaled[x-1][y-1] + 1*grayscaled[x][y-1] + 1*grayscaled[x+1][y-1] +
                    0*grayscaled[x-1][y] + 0*grayscaled[x][y] + 0*grayscaled[x+1][y] +
                    -1*grayscaled[x-1][y+1] + -1*grayscaled[x][y+1] + -1*grayscaled[x+1][y+1])
            mask_2 = int(0*grayscaled[x-1][y-1] + 1*grayscaled[x][y-1] + 1*grayscaled[x+1][y-1] +
                    -1*grayscaled[x-1][y] + 0*grayscaled[x][y] + 1*grayscaled[x+1][y] +
                    -1*grayscaled[x-1][y+1] + -1*grayscaled[x][y+1] + 0*grayscaled[x+1][y+1])
            mask_3 = int(-1*grayscaled[x-1][y-1] + 0*grayscaled[x][y-1] + 1*grayscaled[x+1][y-1] +
                    -1*grayscaled[x-1][y] + 0*grayscaled[x][y] + 1*grayscaled[x+1][y] +
                    -1*grayscaled[x-1][y+1] + 0*grayscaled[x][y+1] + 1*grayscaled[x+1][y+1])
            mask_4 = int(-1*grayscaled[x-1][y-1] + -1*grayscaled[x][y-1] + 0*grayscaled[x+1][y-1] +
                    -1*grayscaled[x-1][y] + 0*grayscaled[x][y] + 1*grayscaled[x+1][y] +
                    0*grayscaled[x-1][y+1] + 1*grayscaled[x][y+1] + 1*grayscaled[x+1][y+1])
            mask_5 = int(-1*grayscaled[x-1][y-1] + -1*grayscaled[x][y-1] + -1*grayscaled[x+1][y-1] +
                    0*grayscaled[x-1][y] + 0*grayscaled[x][y] + 0*grayscaled[x+1][y] +
                    1*grayscaled[x-1][y+1] + 1*grayscaled[x][y+1] + 1*grayscaled[x+1][y+1])
            mask_6 = int(0*grayscaled[x-1][y-1] + -1*grayscaled[x][y-1] + -1*grayscaled[x+1][y-1] +
                    1*grayscaled[x-1][y] + 0*grayscaled[x][y] + -1*grayscaled[x+1][y] +
                    1*grayscaled[x-1][y+1] + 1*grayscaled[x][y+1] + 0*grayscaled[x+1][y+1])
            mask_7 = int(1*grayscaled[x-1][y-1] + 0*grayscaled[x][y-1] + -1*grayscaled[x+1][y-1] +
                    1*grayscaled[x-1][y] + 0*grayscaled[x][y] + -1*grayscaled[x+1][y] +
                    1*grayscaled[x-1][y+1] + 0*grayscaled[x][y+1] + -1*grayscaled[x+1][y+1])
            mask_8 = int(1*grayscaled[x-1][y-1] + 1*grayscaled[x][y-1] + 0*grayscaled[x+1][y-1] +
                    1*grayscaled[x-1][y] + 0*grayscaled[x][y] + -1*grayscaled[x+1][y] +
                    0*grayscaled[x-1][y+1] + -1*grayscaled[x][y+1] + -1*grayscaled[x+1][y+1])
            c = max([mask_1, mask_2, mask_3, mask_4, mask_5, mask_6, mask_7, mask_8])

            output_pixels[x, y] = (c, c, c)
    
    if threshold != -1:
        output_img = delete_below_threshold(output_img, threshold)

    return output_img

def sobel(input_img, with_gaussian_blur=False, gaussian_size = 5, gaussian_sigma = 1.0, threshold = -1):
    if with_gaussian_blur:
        input_img = gaussian_blur(input_img, gaussian_size, gaussian_sigma)

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
    
    if threshold != -1:
        output_img = delete_below_threshold(output_img, threshold)

    return output_img

def delete_below_threshold(input_img, threshold):
    width, height = input_img.size
    input_pixels = input_img.load()

    output_img = Image.new(input_img.mode, input_img.size)
    output_pixels = output_img.load()

    grayscaled = [[get_gray(input_pixels[i, j][0], input_pixels[i, j][1], input_pixels[i, j][2]) for j in range(height)] for i in range(width)]

    for x in range(1, width-1):
        for y in range(1, height-1):
            c = grayscaled[x][y]
            if c < threshold:
                output_pixels[x, y] = 0
            else:
                output_pixels[x, y] = (c, c, c)
    return output_img