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
        print("  == Without Gaussian Blur:")
        print("\t> python application.py --sobel <input_image_path> <output_image_path>")
        print("  == With Gaussian Blur:")
        print("\t> python application.py --sobel <input_image_path> <output_image_path> <gaussian blur size> <gaussian blur sigma>")
        print("  == With Gaussian Blur and Deleting Below Threshold:")
        print("\t> python application.py --sobel <input_image_path> <output_image_path> <gaussian blur size> <gaussian blur sigma> <threshold>")
    elif method == "prewitt":
        print("=== PREWITT ===")
        print("  == Without Gaussian Blur:")
        print("\t> python application.py --prewitt <input_image_path> <output_image_path>")
        print("  == With Gaussian Blur:")
        print("\t> python application.py --prewitt <input_image_path> <output_image_path> <gaussian blur size> <gaussian blur sigma>")
        print("  == With Gaussian Blur and Deleting Below Threshold:")
        print("\t> python application.py --prewitt <input_image_path> <output_image_path> <gaussian blur size> <gaussian blur sigma> <threshold>")
    elif method == "gaussian_blur":
        print("=== GAUSSIAN BLUR ===")
        print("\t> python application.py --gaussian_blur <input_image_path> <output_image_path> <gaussian blur size> <gaussian blur sigma>")

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
        if len(sys.argv) != 4 and len(sys.argv) != 6 and len(sys.argv) != 7:
            print("Wrong number of arguments!")
            print_usage("sobel")
            exit()
        else:
            im = Image.open(str(sys.argv[2]))
            out_path = str(sys.argv[3])

            if len(sys.argv) == 4:
                outimg = edge_detection.sobel(im, with_gaussian_blur=False)
            elif len(sys.argv) == 6:
                gaussian_size = int(sys.argv[4])
                gaussian_sigma = float(sys.argv[5])
                outimg = edge_detection.sobel(im, with_gaussian_blur=True, gaussian_size = gaussian_size, gaussian_sigma = gaussian_sigma)
            elif len(sys.argv) == 7:
                gaussian_size = int(sys.argv[4])
                gaussian_sigma = float(sys.argv[5])
                threshold = int(sys.argv[6])
                outimg = edge_detection.sobel(im, with_gaussian_blur=True, gaussian_size = gaussian_size, gaussian_sigma = gaussian_sigma, threshold = threshold)
    elif len(sys.argv) > 1 and sys.argv[1] == '--prewitt':
        if len(sys.argv) != 4 and len(sys.argv) != 6 and len(sys.argv) != 7:
            print("Wrong number of arguments!")
            print_usage("prewitt")
            exit()
        else:
            im = Image.open(str(sys.argv[2]))
            out_path = str(sys.argv[3])

            if len(sys.argv) == 4:
                outimg = edge_detection.prewitt(im, with_gaussian_blur=False)
            elif len(sys.argv) == 6:
                gaussian_size = int(sys.argv[4])
                gaussian_sigma = float(sys.argv[5])
                outimg = edge_detection.prewitt(im, with_gaussian_blur=True, gaussian_size = gaussian_size, gaussian_sigma = gaussian_sigma)
            elif len(sys.argv) == 7:
                gaussian_size = int(sys.argv[4])
                gaussian_sigma = float(sys.argv[5])
                threshold = int(sys.argv[6])
                outimg = edge_detection.prewitt(im, with_gaussian_blur=True, gaussian_size = gaussian_size, gaussian_sigma = gaussian_sigma, threshold = threshold)
    elif len(sys.argv) > 1 and sys.argv[1] == '--gaussian_blur':
        if len(sys.argv) != 4:
            print("Wrong number of arguments!")
            print_usage("gaussian_blur")
            exit()
        else:
            im = Image.open(str(sys.argv[2]))
            width, height = im.size
            out_path = str(sys.argv[3])
            gaussian_size = int(sys.argv[4])
            gaussian_sigma = float(sys.argv[5])

            outimg = edge_detection.gaussian_blur(im, gaussian_size, gaussian_sigma)
    else:
        print("Wrong usage! Valid calls:")
        print_usage("twirl")
        print_usage("sobel")
        print_usage("prewitt")
        print_usage("gaussian_blur")
        exit()

    outimg.save(out_path)
    
    end_time = time.time()
    print_elapsed_time(start_time, end_time)