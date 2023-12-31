import random
import string

def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

# Exemplo de uso: gerar senha com comprimento 12
senha_gerada = gerar_senha(12)
print("Senha gerada:", senha_gerada)
