python application.py --twirl images/original/noise.jpg images/transformed/noise_twirl.jpg
python application.py --twirl images/original/human_face.jpg images/transformed/human_face_twirl.jpg 100 400 500 90
python application.py --twirl images/original/dogs.jpg images/transformed/dogs_twirl.jpg 0 200 300 100
python application.py --sobel images/original/dogs.jpg images/transformed/dogs_sobel.jpg
python application.py --sobel images/original/forest.jpg images/transformed/forest_sobel.jpg
python application.py --sobel images/original/human_face.jpg images/transformed/human_face_sobel.jpg
python application.py --sobel images/original/noise.jpg images/transformed/noise_sobel.jpg
python application.py --sobel images/original/dogs.jpg images/transformed/dogs_sobel_gauss_5.jpg 5 1.0
python application.py --sobel images/original/dogs.jpg images/transformed/dogs_sobel_gauss_11.jpg 11 5.0
python application.py --sobel images/original/forest.jpg images/transformed/forest_sobel_gauss_5.jpg 5 1.0
python application.py --sobel images/original/forest.jpg images/transformed/forest_sobel_gauss_11.jpg 11 5.0
python application.py --sobel images/original/human_face.jpg images/transformed/human_face_sobel_gauss_5.jpg 5 1.0
python application.py --sobel images/original/human_face.jpg images/transformed/human_face_sobel_gauss_11.jpg 11 5.0
python application.py --sobel images/original/noise.jpg images/transformed/noise_sobel_gauss_5.jpg 5 1.0
python application.py --sobel images/original/noise.jpg images/transformed/noise_sobel_gauss_11.jpg 11 5.0
python application.py --sobel images/original/dogs.jpg images/transformed/dogs_sobel_gauss_5_thresh_135.jpg 5 1.0 135
python application.py --sobel images/original/forest.jpg images/transformed/forest_sobel_gauss_5_thresh_80.jpg 5 1.0 80
python application.py --sobel images/original/human_face.jpg images/transformed/human_face_sobel_gauss_5_thresh_35.jpg 5 1.0 35
python application.py --sobel images/original/noise.jpg images/transformed/noise_sobel_gauss_11_thresh_40.jpg 11 5.0 40
python application.py --prewitt images/original/dogs.jpg images/transformed/dogs_prewitt.jpg
python application.py --prewitt images/original/forest.jpg images/transformed/forest_prewitt.jpg
python application.py --prewitt images/original/human_face.jpg images/transformed/human_face_prewitt.jpg
python application.py --prewitt images/original/noise.jpg images/transformed/noise_prewitt.jpg
python application.py --prewitt images/original/dogs.jpg images/transformed/dogs_prewitt_gauss_5_thresh_135.jpg 5 1.0 135
python application.py --prewitt images/original/forest.jpg images/transformed/forest_prewitt_gauss_5_thresh_80.jpg 5 1.0 80
python application.py --prewitt images/original/human_face.jpg images/transformed/human_face_prewitt_gauss_5_thresh_35.jpg 5 1.0 35
python application.py --prewitt images/original/noise.jpg images/transformed/noise_prewitt_gauss_11_thresh_40.jpg 11 5.0 40
