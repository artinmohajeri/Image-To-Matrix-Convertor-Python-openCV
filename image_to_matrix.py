import cv2
import numpy as np

image = cv2.imread('.imgs/palm.jpg', cv2.IMREAD_GRAYSCALE)
np.savetxt('matrix.txt', image, fmt='%d')