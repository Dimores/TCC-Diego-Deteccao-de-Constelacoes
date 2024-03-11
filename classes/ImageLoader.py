import glob
import cv2

class ImageLoader:
    """
    Classe para carregar imagens de forma conveniente.

    Esta classe fornece métodos para carregar uma única imagem,
    várias imagens, podendo ser em tom de cinza ou não.

    Métodos:
    - loadImage: carrega uma única imagem.
    - loadImageGray: carrega uma única imagem em tons de cinza.
    - loadMultipleImages: carrega várias imagens.
    - loadMultipleImagesGray: carrega várias imagens em tons de cinza.
    """
    @staticmethod
    def loadImage(imgName):
        """
        Função que carrega uma única imagem.

        imgName: Nome da imagem que será carregada.
        """
        img = cv2.imread("testeImgs/" + imgName + ".jpg")
        return img
    
    @staticmethod
    def loadImageGray(imgName):
        """
        Função que carrega uma única imagem em tons de cinza.

        imgName: Nome da imagem que será carregada.
        """
        imgGray = cv2.imread("testeImgs/" + imgName + ".jpg", 0)
        return imgGray
    
    @staticmethod
    def loadMultipleImages(imgVectorName):
        """
        Função que carrega um vetor de imagens.

        imgVectorName: Lista de nomes dos arquivos das imagens que serão carregadas.
        """
        # Lista para armazenar as imagens carregadas
        images = []

        # Iterar sobre os nomes dos arquivos
        for img_name in imgVectorName:
            # Carregar a imagem
            img = ImageLoader.loadImage(img_name)
            # Verificar se a imagem foi carregada com sucesso
            if img is not None:
                # Adicionar a imagem carregada à lista de imagens
                images.append(img)
            else:
                print("Erro ao carregar:", img_name)

        return images
    
    @staticmethod
    def loadMultipleImagesGray(imgVectorName):
        """
        Função que carrega um vetor de imagens em tons de cinza.

        imgVectorName: Lista de nomes dos arquivos das imagens que serão carregadas.
        """
        # Lista para armazenar as imagens carregadas
        imagesGray = []

        # Iterar sobre os nomes dos arquivos
        for img_name in imgVectorName:
            # Carregar a imagem
            imgGray = ImageLoader.loadImageGray(img_name)
            # Verificar se a imagem foi carregada com sucesso
            if imgGray is not None:
                # Adicionar a imagem carregada à lista de imagens
                imagesGray.append(imgGray)
            else:
                print("Erro ao carregar:", img_name)

        return imagesGray