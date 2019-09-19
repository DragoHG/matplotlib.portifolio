# diagrama de caixa

import matplotlib.pyplot as plt
import random

vetor = []

for i in range(10):
    num = random.randint(0,10000)
    vetor.append(num)

plt.boxplot(vetor)
plt.title("Boxplot")
plt.show()