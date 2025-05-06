
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")


def crear_album(figus_total):
    return np.zeros(figus_total)

def album_incompleto(album):
    return 0 in album

def comprar_figu(figus_total):
    return random.randint(0, figus_total - 1)

def cuantas_figus(figus_total):
    compras = 0
    album = crear_album(figus_total)
    while album_incompleto(album):
        figu = comprar_figu(figus_total)
        album[figu] = 1
        compras += 1
    return compras

def experimento_figus(n_repeticiones, figus_total):
    resultados = [cuantas_figus(figus_total) for _ in range(n_repeticiones)]
    promedio = np.mean(resultados)
    print(f"En promedio, se necesitan {promedio:.2f} figuritas individuales para llenar un álbum de {figus_total} figuritas (basado en {n_repeticiones} simulaciones).")
    return resultados


def comprar_paquete(figus_total, figus_paquete):
    return [random.randint(0, figus_total - 1) for _ in range(figus_paquete)]

def cuantos_paquetes(figus_total, figus_paquete):
    compras = 0
    album = crear_album(figus_total)
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        for figu in paquete:
            album[figu] = 1
        compras += 1
    return compras

def experimento_paquetes(n_repeticiones, figus_total, figus_paquete):
    resultados = [cuantos_paquetes(figus_total, figus_paquete) for _ in range(n_repeticiones)]
    promedio = np.mean(resultados)
    print(f"En promedio, se necesitan {promedio:.2f} paquetes de {figus_paquete} figuritas para llenar un álbum de {figus_total} figuritas (basado en {n_repeticiones} simulaciones).")
    return resultados


if __name__ == "__main__":
    # Parametros
    figus_total = 670
    figus_paquete = 5
    n_repeticiones = 1000

    # Experimento con paquetes
    resultados = experimento_paquetes(n_repeticiones, figus_total, figus_paquete)

    # Histograma de resultados
    plt.figure(figsize=(10, 6))
    sns.histplot(resultados, bins=30, kde=True)
    plt.title(f"Distribución de paquetes necesarios para llenar un álbum de {figus_total} figuritas")
    plt.xlabel("Cantidad de paquetes comprados")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.savefig("histograma_paquetes.png")
    plt.show()
