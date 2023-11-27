# código de geração do gráfico 
import pandas as pd  # Importa a biblioteca Pandas para lidar com os dados
import matplotlib.pyplot as plt  # Importa a biblioteca Matplotlib para criação de gráficos

# Carregar os dados do arquivo CSV
data = pd.read_csv('gasolina.csv')  # Lê o arquivo CSV e armazena os dados em um DataFrame do Pandas

# Criar o gráfico de linha
plt.figure(figsize=(8, 6))  # Define o tamanho do gráfico
plt.plot(data['dia'], data['venda'], marker='o', linestyle='-')  # Cria o gráfico de linha com os dias no eixo x e vendas no eixo y
plt.xlabel('Dia')  # Adiciona um rótulo ao eixo x
plt.ylabel('Preço de Venda')  # Adiciona um rótulo ao eixo y
plt.title('Preço Médio de Venda de Gasolina - Julho de 2021-Atualizado')  # Adiciona um título ao gráfico
plt.grid(True)  # Adiciona grades ao gráfico

# Salvar o gráfico como gasolina.png
plt.savefig('gasolina.png')  # Salva o gráfico como um arquivo de imagem

# Mostrar o gráfico
plt.show()  # Exibe o gráfico na interface gráfica