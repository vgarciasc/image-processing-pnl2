import time
import sys
from PIL import Image

import transformations
import edge_detection

def print_elapsed_time(start_time, end_time):
    print("Elapsed time: " + str("{0:.2f}".format(end_time - start_time)))

def print_usage(method):
    if method == "twirl":
        print("=== TWIRL ===")
        print("  == Default parameters:")
        print("\t> python application.py --twirl <input_image_path> <output_image_path>")
        print("  == Specify parameters")
        print("\t> python application.py --twirl <input_image_path> <output_image_path> <x coordinate of center of twirl> <y coordinate of center of twirl> <maximum radius of twirl> <twirl degrees>")
    elif method == "sobel":
        print("=== SOBEL ===")
        print("\t> python application.py --sobel <input_image_path> <output_image_path>")

if __name__ == "__main__":
    start_time = time.time()
    
    if len(sys.argv) > 1 and sys.argv[1] == '--twirl':
        if len(sys.argv) != 4 and len(sys.argv) != 8:
            print("Wrong number of arguments!")
            print_usage("twirl")
            exit()
        else:
            im = Image.open(str(sys.argv[2]))
            width, height = im.size
            out_path = str(sys.argv[3])

            if len(sys.argv) == 4:
                x_center = width / 2
                y_center = height / 2
                max_radius = (width + height) / 4
                degrees = 70
            elif len(sys.argv) == 8:
                x_center = int(sys.argv[4])
                y_center = int(sys.argv[5])
                max_radius = float(sys.argv[6])
                degrees = float(sys.argv[7])

            outimg = transformations.twirl(im, x_center, y_center, max_radius, degrees)
    elif len(sys.argv) > 1 and sys.argv[1] == '--sobel':
        if len(sys.argv) != 4:
            print("Wrong number of arguments!")
            print_usage("sobel")
            exit()
        else:
            im = Image.open(str(sys.argv[2]))
            width, height = im.size
            out_path = str(sys.argv[3])

            outimg = edge_detection.sobel(im)
    else:
        print("Wrong usage! Valid calls:")
        print_usage("twirl")
        print_usage("sobel")
        exit()

    outimg.save(out_path)
    
    end_time = time.time()
    print_elapsed_time(start_time, end_time)