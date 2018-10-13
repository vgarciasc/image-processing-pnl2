from PIL import Image
from math import *

def linear_interpolate(image, x, y):
    u = floor(x)
    v = floor(y)

    dist_u = x - u
    dist_v = y - v

    r = (1 - dist_u)*(1 - dist_v)*image[u, v][0] + (dist_u)*(1 - dist_v)*image[u + 1, v][0] + (1 - dist_u)*(dist_v)*image[u, v + 1][0] + (dist_u)*(dist_v)*image[u + 1, v + 1][0]
    g = (1 - dist_u)*(1 - dist_v)*image[u, v][1] + (dist_u)*(1 - dist_v)*image[u + 1, v][1] + (1 - dist_u)*(dist_v)*image[u, v + 1][1] + (dist_u)*(dist_v)*image[u + 1, v + 1][1]
    b = (1 - dist_u)*(1 - dist_v)*image[u, v][2] + (dist_u)*(1 - dist_v)*image[u + 1, v][2] + (1 - dist_u)*(dist_v)*image[u, v + 1][2] + (dist_u)*(dist_v)*image[u + 1, v + 1][2]

    return (int(r), int(g), int(b))

def twirl(input_img, xc, yc, rmax, theta):
    width, height = input_img.size
    input_pixels = input_img.load()

    output_img = Image.new(input_img.mode, input_img.size)
    output_pixels = output_img.load()

    theta = radians(theta)

    for x_linha in range(0, width):
        for y_linha in range(0, height):
            dx = x_linha - xc
            dy = y_linha - yc
            r = sqrt(dx*dx + dy*dy)
            beta = atan2(dy, dx) + theta*(rmax - r)/rmax

            x = xc + r * cos(beta)
            y = yc + r * sin(beta)
            
            if r >= rmax:
                output_pixels[x_linha, y_linha] = input_pixels[x_linha, y_linha]
            elif x > 1 and x < width - 1 and y > 1 and y < height - 1:
                output_pixels[x_linha, y_linha] = linear_interpolate(input_pixels, x, y)
            else:
                output_pixels[x_linha, y_linha] = (0, 0, 0)
    return output_img