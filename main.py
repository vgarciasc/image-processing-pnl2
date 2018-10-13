from PIL import Image
import numpy as np
import time
import pdb

def print_elapsed_time(start_time, end_time):
    print("Elapsed time: " + str("{0:.2f}".format(end_time - start_time)))

def get_gray(r, g, b):
    return int((r * 0.299) + (g * 0.587) + (b * 0.114))

im = Image.open("pictures/dogs_contrast_blurred.jpg")
width, height = im.size

start_time = time.time()

pixels_old = im.load()

out = Image.new(im.mode, im.size)
pixels_new = out.load()

# grayscaled = np.zeros((width, height), np.int8)
grayscaled = [[get_gray(pixels_old[i, j][0], pixels_old[i, j][1], pixels_old[i, j][2]) for j in range(height)] for i in range(width)]
gaussian_blurred = grayscaled.copy()

print("> Finished grayscaling")

# for x in range(2, width-2):
#     for y in range(2, height-2):
#         c = int(1*grayscaled[x-2][y-2] + 4*grayscaled[x-1][y-2] + 6*grayscaled[x][y-2] + 4*grayscaled[x+1][y-2] + 1*grayscaled[x+2][y-2] +
#             4*grayscaled[x-2][y-1] + 16*grayscaled[x-1][y-1] + 24*grayscaled[x][y-1] + 16*grayscaled[x+1][y-1] + 4*grayscaled[x+2][y-1] +
#             6*grayscaled[x-2][y] + 24*grayscaled[x-1][y] + 36*grayscaled[x][y] + 24*grayscaled[x+1][y] + 6*grayscaled[x+2][y] +
#             4*grayscaled[x-2][y+1] + 16*grayscaled[x-1][y+1] + 24*grayscaled[x][y+1] + 16*grayscaled[x+1][y+1] + 4*grayscaled[x+2][y+1] +
#             1*grayscaled[x-2][y+2] + 4*grayscaled[x-1][y+2] + 6*grayscaled[x][y+2] + 4*grayscaled[x+1][y+2] + 1*grayscaled[x+2][y+2])
#         gaussian_blurred[x][y] = c//256

# print("> Finished gaussian blurring")

for x in range(1, width-1):
    for y in range(1, height-1):
        hor = int(-1*gaussian_blurred[x-1][y-1] + -2*gaussian_blurred[x][y-1] + -1*gaussian_blurred[x+1][y-1] +
                1*gaussian_blurred[x-1][y+1] + 2*gaussian_blurred[x][y+1] + 1*gaussian_blurred[x+1][y+1])
        ver = int(-1*gaussian_blurred[x-1][y-1] + -2*gaussian_blurred[x-1][y] + -1*gaussian_blurred[x-1][y+1] +
                1*gaussian_blurred[x+1][y-1] + 2*gaussian_blurred[x+1][y] + 1*gaussian_blurred[x+1][y+1])
        c = int(np.sqrt(hor*hor + ver*ver))

        pixels_new[x, y] = (c, c, c)

end_time = time.time()
print_elapsed_time(start_time, end_time)

out.save("pictures/dogs_contrast_blurred_sobel_1.jpg")
