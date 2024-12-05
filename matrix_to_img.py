import cv2
import numpy as np

matrix = np.loadtxt('matrix.txt', dtype=np.uint8)

cv2.imwrite('output_image.jpg', matrix)