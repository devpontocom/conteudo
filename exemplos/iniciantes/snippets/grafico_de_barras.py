import matplotlib.pyplot as plt

# Define os dados do gráfico: vendas totais para cada mês
dados = [3, 6, 5, 8, 7]

# Define os rótulos para o eixo x do gráfico: os meses do ano
labels = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI']

# Configura o texto do eixo x e y do gráfico
plt.ylabel('Total de Vendas')
plt.xlabel('Mês')

# Cria um gráfico de barras usando os rótulos e os dados definidos
plt.bar(labels, dados)

# Exibe o gráfico criado
plt.show()