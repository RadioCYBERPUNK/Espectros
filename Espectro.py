# OpenCV (Open Source Computer Vision Library) é uma biblioteca de código aberto
# amplamente utilizada para processamento de imagens e visão computacional.
import cv2
# NumPy é uma biblioteca fundamental em Python para computação numérica.
import numpy as np
# Matplotlib é uma biblioteca de plotagem em Python que permite criar gráficos, visualizações e figuras.
import matplotlib.pyplot as plt

# Imagens para comparação de espectro
imagem1 = cv2.imread('C:\\Users\\saturno\\Documents\\a.jpg', 0)
# Imagens igual para fim de analise de resultados
imagem2 = cv2.imread('C:\\Users\\saturno\\Documents\\a.jpg', 0)
# Imagens diferente para fim de analise de resultados
imagem3 = cv2.imread('C:\\Users\\saturno\\Documents\\a2.jpg', 0)

# Redimensione a segunda imagem para ter o mesmo tamanho da primeira
# para evitar erro de compilação "boas praticas"
imagem2 = cv2.resize(imagem2, (imagem1.shape[1], imagem1.shape[0]))
imagem3 = cv2.resize(imagem3, (imagem1.shape[1], imagem1.shape[0]))

# Calcule o espectro de Fourier para ambas as imagens
# O cálculo de Fourier aplicado às imagens é uma técnica que descompõe uma imagem em
# suas componentes de frequência, representando-as como espectros. Isso permite analisar a
# distribuição de frequências e identificar diferenças entre imagens. O resultado revela
# informações valiosas sobre texturas e padrões, sendo útil em análises forenses e
# processamento de imagens.
espectro1 = np.fft.fftshift(np.fft.fft2(imagem1))
espectro2 = np.fft.fftshift(np.fft.fft2(imagem2))
espectro3 = np.fft.fftshift(np.fft.fft2(imagem3))

# Calcule a diferença entre os espectros 3 e 2
diferenca_espectros_3_2 = np.abs(espectro3 - espectro2)

# Exibe as imagens e os espectros
plt.figure(figsize=(12, 10))

# Subplot 1: Imagem 1
plt.subplot(331)
plt.imshow(imagem1, cmap='gray')
plt.title('Imagem 1')
plt.axis('off')

# Subplot 2: Imagem 2
plt.subplot(332)
plt.imshow(imagem2, cmap='gray')
plt.title('Imagem 2')
plt.axis('off')

# Subplot 3: Imagem 3
plt.subplot(333)
plt.imshow(imagem3, cmap='gray')
plt.title('Imagem 3')
plt.axis('off')

# Subplot 4: Espectro da Imagem 1
plt.subplot(334)
plt.imshow(np.log(np.abs(espectro1) + 1), cmap='gray')
plt.title('Espectro da Imagem 1')
plt.axis('off')

# Subplot 5: Espectro da Imagem 2 (igual)
plt.subplot(335)
plt.imshow(np.log(np.abs(espectro2) + 1), cmap='gray')
plt.title('Espectro da Imagem 2 (igual)')
plt.axis('off')

# Subplot 6: Espectro da Imagem 3 (Diferente)
plt.subplot(336)
plt.imshow(np.log(np.abs(espectro3) + 1), cmap='gray')
plt.title('Espectro da Imagem 3')
plt.axis('off')

plt.tight_layout()
plt.show()
