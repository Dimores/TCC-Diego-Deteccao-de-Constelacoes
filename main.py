import cv2
import numpy as np
from matplotlib import pyplot as plt
from classes import *

# Testando template matching básico
'''
Primeiro trabalho - 
1) Peguei uma imagem maior, cortei ela, e gerei a imagem menor.
2) Testei todos os métodos de Template matching.
3) Plotei a imagem com a área do matching na tela.
------------------
Segundo trabalho - 
1) Pegar a imagem do Github.
2) Pegar uma imagem maior que a do Github, da mesma região.
3) Testar
'''
def main():
    img = ImageLoader.loadImageGray("testeMaior")
    assert img is not None, "file could not be read, check with os.path.exists()"
    img2 = img.copy()
    template = ImageLoader.loadImageGray("testeMenor")
    assert template is not None, "file could not be read, check with os.path.exists()"

    # img = ImageLoader.loadImageGray("andromedaMeu")
    # assert img is not None, "file could not be read, check with os.path.exists()"
    # img2 = img.copy()
    # template = ImageLoader.loadImageGray("andromedaGit")
    # assert template is not None, "file could not be read, check with os.path.exists()"

    w, h = template.shape[::-1]

    # All the 6 methods for comparison in a list
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
                'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    for meth in methods:
        img = img2.copy()
        method = eval(meth)

        # Apply template Matching
        res = cv2.matchTemplate(img, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        # Draw rectangle on the original image
        cv2.rectangle(img, top_left, bottom_right, 255, 2)

        # Plot the entire original image with rectangle
        plt.imshow(img, cmap='gray')
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.suptitle(meth)

        plt.show()

if __name__ == "__main__":
    main()