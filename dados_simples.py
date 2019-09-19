import matplotlib.pyplot as plt

#vars
x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]
z = [200, 25, 400, 3300, 100]

#teste
x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]

titulo = 'Grafico de dispersão'
eixox = 'Eixo X'
eixoy = 'Eixo Y'

#legenda
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.plot(x, y, color='k', linestyle='--')
plt.scatter(x, y, label='Pontos de interesse', color='r', marker='h', s=z)

'''
plt.bar(x1, y1, label='Grupo 1')
plt.bar(x2, y2, label='Grupo 2')
'''
plt.legend()

#exibe dados
plt.show()

#salvar png para art. cientifico
#plt.savefig('art1.png', dpi=300)