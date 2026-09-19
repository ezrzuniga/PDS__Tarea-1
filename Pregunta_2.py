import argparse
import numpy as np
import matplotlib.pyplot as plt





def main():
    parser = argparse.ArgumentParser(description="Señal senoidal y su alias bajo muestreo.")
    parser.add_argument("--F", type=float, required=True, help="Frecuencia natural (Hz)")
    parser.add_argument("--Fs", type=float, required=True, help="Frecuencia de muestreo (Hz)")
    parser.add_argument("--ciclos", type=float, default=3, help="Ciclos de la señal original a mostrar")
    args = parser.parse_args()

    F, Fs, ciclos = args.F, args.Fs, args.ciclos
    print("F: ",F)
    print("Fs: ",Fs)
    print("ciclos: ",ciclos)


    # Definir los tamaños del eje X e Y
    x = np.linspace(-10, 10, 400)
    # Establecemos la función seno al eje Y
    y = np.sin(x)
    
    # Crear el gráfico
    plt.figure(figsize = (10, 3))
    # Creamos la gráfica del seno con color rojo y tamaño de línea 3
    plt.plot(x, y, color = "red", linewidth = 3)
    # Establecemos el título del gráfico
    plt.title("Gráfica del seno")
    # Establecemos el nombre del eje X
    plt.xlabel("x")
    # Establecemos el nombre del eje Y
    plt.ylabel("sen(x)")
    # Ocultamos la rejilla
    plt.grid(False)
    # Establecemos el color y grosor de la línea divisora del eje X
    plt.axhline(0, color = "gray", lw = 1)
    # Establecemos el color y grosor de la línea divisora del eje Y
    plt.axvline(0, color = "gray", lw = 1)
    # Mostramos el gráfico del seno




    # Definir los tamaños del eje X e Y
    x2 = np.linspace(-10, 10, 800)
    # Establecemos la función seno al eje Y
    y2 = np.sin(x2)

    # Creamos la gráfica del seno con color azul y tamaño de línea 3 (mismo figure/axes que la anterior)
    plt.plot(x2, y2, color = "blue", linewidth = 3)





    plt.show()


if __name__ == "__main__":
    main()
