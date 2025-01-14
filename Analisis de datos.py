dias_semana = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
temperaturas = np.array([22, 24, 25, 27, 30, 32, 28, 25, 26, 27])


temperatura_media = np.mean(temperaturas)
temperatura_maxima = np.max(temperaturas)
temperatura_minima = np.min(temperaturas)

# Imprimir los resultados
(temperatura_media, temperatura_maxima, temperatura_minima)

# Graficar la temperatura promedio diaria 
plt.figure(figsize=(10, 6))

# Graficar las temperaturas
plt.plot(dias_semana, temperaturas, marker='o', linestyle='-', color='orange')

# Añadir etiquetas a los ejes
plt.xlabel('Días de la Semana')
plt.ylabel('Temperatura Promedio (°C)')

# Añadir titulo
plt.title('Temperatura Promedio Diaria en Función de los Días de la Semana')

# Mostrar el grafico
plt.grid(True)
plt.show()