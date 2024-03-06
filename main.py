import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Testando template matching básico
'''
Trabalho inicial - 
1) Peguei uma imagem maior, cortei ela, e gerei a imagem menor.
2) Testei todos os métodos de Template matching.
3) Plotei a imagem com a área do matching na tela.
'''

img = cv.imread('testeImgs/testeMaior.jpg', 0)
assert img is not None, "file could not be read, check with os.path.exists()"
img2 = img.copy()
template = cv.imread('testeImgs/testeMenor.jpg', 0)
assert template is not None, "file could not be read, check with os.path.exists()"
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)

    # Apply template Matching
    res = cv.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # Draw rectangle on the original image
    cv.rectangle(img, top_left, bottom_right, 255, 2)

    # Plot the entire original image with rectangle
    plt.imshow(img, cmap='gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)

    plt.show()
