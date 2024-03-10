import matplotlib.pyplot as plt
import cv2

class ShowImages:
    """
    Classe para exibir imagens de forma conveniente.

    Esta classe fornece métodos para exibir uma única imagem,
    várias imagens em uma grade e várias imagens em tons de cinza.

    Métodos:
    - showSingleImage: exibe uma única imagem.
    - showSingleImageGray: exibe uma única imagem em tons de cinza.
    - showMultipleImages: exibe várias imagens em uma grade.
    - showMultipleImagesGray: exibe várias imagens em tons de cinza em uma grade.
    """
    @staticmethod
    def showSingleImage(img, title, size):
        """
        Função que exibe uma única imagem.

        img: Imagem que será exibida na tela.
        title: Título da imagem.
        size: Tamanho da figura (largura, altura).
        """
        fig, axis = plt.subplots(figsize=size)
        axis.imshow(img)
        axis.set_title(title, fontdict={'fontsize': 22, 'fontweight': 'medium'})
        plt.show()

    @staticmethod
    def showSingleImageGray(img, title, size):
        """
        Função que exibe uma única imagem em tons de cinza.

        img: Imagem que será exibida na tela.
        title: Título da imagem.
        size: Tamanho da figura (largura, altura).
        """
        fig, axis = plt.subplots(figsize=size)
        axis.imshow(img, 'gray')
        axis.set_title(title, fontdict={'fontsize': 22, 'fontweight': 'medium'})
        plt.show()

    @staticmethod
    def showMultipleImages(imgsArray, titlesArray, size, x, y):
        """
        Função que exibe várias imagens.

        imgsArray: Vetor de imagens que serão exibidas na tela.
        title: Vetor de títulos das imagens.
        size: Tamanho da figura (largura, altura).
        x: Número de imagens por linha.
        y: Número de imagens por coluna.
        """
        if(x < 1 or y < 1):
            print("ERRO: X e Y não podem ser zero ou abaixo de zero!")
            return
        elif(x == 1 and y == 1):
            ShowImages.showSingleImage(imgsArray[0], titlesArray[0], size)
        elif(x == 1):
            fig, axis = plt.subplots(y, figsize=size)
            yId = 0
            for img, title in zip(imgsArray, titlesArray):
                axis[yId].imshow(img)
                axis[yId].set_anchor('NW')
                axis[yId].set_title(title, fontdict={'fontsize': 18, 'fontweight': 'medium'}, pad=10)
                yId += 1
        elif(y == 1):
            fig, axis = plt.subplots(1, x, figsize=size)
            fig.suptitle(titlesArray)
            xId = 0
            for img, title in zip(imgsArray, titlesArray):
                axis[xId].imshow(img)
                axis[xId].set_anchor('NW')
                axis[xId].set_title(title, fontdict={'fontsize': 18, 'fontweight': 'medium'}, pad=10)
                xId += 1
        else:
            fig, axis = plt.subplots(y, x, figsize=size)
            titleId = 0
            for i in range(y):
                for j in range(x):
                    axis[i, j].set_title(titlesArray[titleId], fontdict={'fontsize': 18, 'fontweight': 'medium'}, pad=10)
                    axis[i, j].set_anchor('NW')
                    axis[i, j].imshow(imgsArray[titleId])
                    if(len(titlesArray[titleId]) == 0):
                        axis[i, j].axis('off')
                    titleId += 1
        plt.show()
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    @staticmethod
    def showMultipleImagesGray(imgsArray, titlesArray, size, x, y):
        """
        Função que exibe várias imagens em tons de cinza.

        imgsArray: Vetor de imagens que serão exibidas na tela.
        title: Vetor de títulos das imagens.
        size: Tamanho da figura (largura, altura).
        x: Número de imagens por linha.
        y: Número de imagens por coluna.
        """
        if(x < 1 or y < 1):
            print("ERRO: X e Y não podem ser zero ou abaixo de zero!")
            return
        elif(x == 1 and y == 1):
            ShowImages.showSingleImageGray(imgsArray[0], titlesArray[0], size)
        elif(x == 1):
            fig, axis = plt.subplots(y, figsize=size)
            yId = 0
            for img, title in zip(imgsArray, titlesArray):
                axis[yId].imshow(img, 'gray')
                axis[yId].set_anchor('NW')
                axis[yId].set_title(title, fontdict={'fontsize': 18, 'fontweight': 'medium'}, pad=10)
                yId += 1
        elif(y == 1):
            fig, axis = plt.subplots(1, x, figsize=size)
            fig.suptitle(titlesArray)
            xId = 0
            for img, title in zip(imgsArray, titlesArray):
                axis[xId].imshow(img, 'gray')
                axis[xId].set_anchor('NW')
                axis[xId].set_title(title, fontdict={'fontsize': 18, 'fontweight': 'medium'}, pad=10)
                xId += 1
        else:
            fig, axis = plt.subplots(y, x, figsize=size)
            titleId = 0
            for i in range(y):
                for j in range(x):
                    axis[i, j].set_title(titlesArray[titleId], fontdict={'fontsize': 18, 'fontweight': 'medium'}, pad=10)
                    axis[i, j].set_anchor('NW')
                    axis[i, j].imshow(imgsArray[titleId], 'gray')
                    if(len(titlesArray[titleId]) == 0):
                        axis[i, j].axis('off')
                    titleId += 1
        plt.show()
        cv2.waitKey(0)
        cv2.destroyAllWindows()