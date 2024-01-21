import matplotlib.pyplot as plt

# Dados
labels = 'Python', 'Java', 'C++', 'Ruby'
sizes = [215, 130, 245, 210]

# Criar gráfico
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Popularidade das Linguagens de Programação')
plt.show()