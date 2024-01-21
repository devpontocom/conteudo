from collections import Counter

texto = "exemplo de texto para contar palavras contar palavras é útil"
palavras = texto.split()
contador = Counter(palavras)

print(contador)