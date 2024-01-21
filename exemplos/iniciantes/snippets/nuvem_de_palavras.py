from wordcloud import WordCloud
import matplotlib.pyplot as plt

texto = "Python é uma linguagem de programação incrível. Python é popular e Python é usado em ciência de dados."

# Gerar a nuvem de palavras
nuvem_palavras = WordCloud(width = 800, height = 800, background_color ='white').generate(texto)

# Mostrar a imagem gerada
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(nuvem_palavras) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show()
