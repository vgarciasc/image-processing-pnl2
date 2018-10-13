import time
import sys
from PIL import Image

import transformations

def print_elapsed_time(start_time, end_time):
    print("Elapsed time: " + str("{0:.2f}".format(end_time - start_time)))

def print_twirl_usage():
    print("=== TWIRL ===")
    print("  == Default parameters:")
    print("\t> python application.py --twirl <input_image_path> <output_image_path>")
    print("  == Specify parameters")
    print("\t> python application.py --twirl <input_image_path> <output_image_path> <x coordinate of center of twirl> <y coordinate of center of twirl> <maximum radius of twirl> <twirl degrees>")

if __name__ == "__main__":
    start_time = time.time()
    
    if len(sys.argv) > 1 and sys.argv[1] == '--twirl':
        if len(sys.argv) != 4 and len(sys.argv) != 8:
            print("Wrong number of arguments!")
            print_twirl_usage()
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
    else:
        print("Wrong usage! Valid calls:")
        print_twirl_usage()
        exit()

    outimg.save(out_path)
    
    end_time = time.time()
    print_elapsed_time(start_time, end_time)