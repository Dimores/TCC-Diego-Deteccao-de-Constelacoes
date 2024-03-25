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
    # ----Teste 1----
    # img = ImageLoader.loadImageGray("testeMaior")
    # assert img is not None, "file could not be read, check with os.path.exists()"
    # img2 = img.copy()
    # template = ImageLoader.loadImageGray("testeMenor")
    # assert template is not None, "file could not be read, check with os.path.exists()"

    # ----Teste 2----
    # img = ImageLoader.loadImageGray("andromedaMeu")
    # assert img is not None, "file could not be read, check with os.path.exists()"
    # img2 = img.copy()
    # template = ImageLoader.loadImageGray("andromedaGit")
    # assert template is not None, "file could not be read, check with os.path.exists()"

    # ----Teste 3----
    # img = ImageLoader.loadImageGray("leaoMeu")
    # assert img is not None, "file could not be read, check with os.path.exists()"
    # img2 = img.copy()
    # template = ImageLoader.loadImageGray("leaoGit")
    # assert template is not None, "file could not be read, check with os.path.exists()"

    # ----Teste 4----
    # img = ImageLoader.loadImageGray("fenixMeu")
    # assert img is not None, "file could not be read, check with os.path.exists()"
    # img2 = img.copy()
    # template = ImageLoader.loadImageGray("fenixGit")
    # assert template is not None, "file could not be read, check with os.path.exists()"

    # w, h = template.shape[::-1]

    # # All the 6 methods for comparison in a list
    # methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
    #             'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    # for meth in methods:
    #     img = img2.copy()
    #     method = eval(meth)

    #     # Apply template Matching
    #     res = cv2.matchTemplate(img, template, method)
    #     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    #     # Imprimir os valores min_val e max_val
    #     print(f"Metodo: {meth}")
    #     print(f"min_val: {min_val}")
    #     print(f"max_val: {max_val}")

    #     # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    #     if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    #         top_left = min_loc
    #     else:
    #         top_left = max_loc
    #     bottom_right = (top_left[0] + w, top_left[1] + h)

    #     # Draw rectangle on the original image
    #     cv2.rectangle(img, top_left, bottom_right, 255, 2)

    #     # Plot the entire original image with rectangle
    #     plt.imshow(img, cmap='gray')
    #     plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    #     plt.suptitle(meth)

    #     plt.show()

    # ----Primeiro teste----
    # Carregando as imagens
    img1 = ImageLoader.loadImageGray("livroMenor")
    img2 = ImageLoader.loadImageGray("livroMaior")
    
    # ----Segundo teste------
    # img1 = ImageLoader.loadImageGray("testeMenor")
    # img2 = ImageLoader.loadImageGray("testeMaior")    

    # ----Terceiro teste------
    # img1 = ImageLoader.loadImageGray("LeaoGit")
    # img2 = ImageLoader.loadImageGray("LeaoMeu")    

    # ----Quarto teste------
    # img1 = ImageLoader.loadImageGray("FenixGit")
    # img2 = ImageLoader.loadImageGray("FenixMeu")    

    # ----Quinto teste------
    # img1 = ImageLoader.loadImageGray("AndromedaGit")
    # img2 = ImageLoader.loadImageGray("AndromedaMeu")    

    # Criando um objeto sift
    sift = cv2.SIFT_create()

    # Detecção de pontos chaves e descritores
    keypoints_1, descriptors_1 = sift.detectAndCompute(img1, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(img2, None)

    # Desenhando os pontos chave
    imgPontosChave1 = cv2.drawKeypoints(img1, keypoints_1, img1)
    imgPontosChave2 = cv2.drawKeypoints(img2, keypoints_2, img2)

    # Objeto usado para encontrar correspondencias
    # Utiliza força bruta, distancia manhattan e verifica em ambas direções
    bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

    # Encontra as correspondências entre os descritores das 2 imagens
    matches = bf.match(descriptors_1,descriptors_2)

    # Ordena a lista de correspondencias com base distancia
    # Lambda extrai a distancia de cada correspondencia da lista
    # lambda arguments: expression
    matches = sorted(matches, key = lambda x:x.distance)

    print("Dados:")
    # Imprimir o número de correspondências
    print("\tNumero de correspondencias:", len(matches))
    # Imprimir o número de pontos chaves da primeira imagen
    print("\tNumero de pontos-chave da img menor:", len(keypoints_1))
    # Imprimir o número de pontos chaves da segunda imagen
    print("\tNumero de pontos-chave da img maior:", len(keypoints_2))
    
    # Desenha as primeiras 50 correspondencias
    matched_img = cv2.drawMatches(img1, keypoints_1, img2, keypoints_2, 
                                  matches[:50], img2, flags=2)

    # Mostrando os pontos chave na tela
    ShowImages.showMultipleImagesGray([imgPontosChave1, imgPontosChave2], 
                            ["Pontos chave 1", "Pontos chave 2"], (8,8), 2, 1)
    
    # Mostrando a imagem com as linhas de correspondência
    ShowImages.showSingleImageGray(matched_img, "Sift", (8,8))

if __name__ == "__main__":
    main()