import argparse
import numpy as np
import matplotlib.pyplot as plt


def frecuencia_alias(F, Fs):
    #Devuelve la frecuencia equivalente de F dentro del rango [-Fs/2, Fs/2].
    return ((F + Fs / 2) % Fs) - Fs / 2


def main():
    parser = argparse.ArgumentParser(
        description="Señal senoidal y su alias bajo muestreo."
    )
    parser.add_argument("--F", type=float, required=True, help="Frecuencia natural de la señal analógica (Hz)")
    parser.add_argument("--Fs", type=float, required=True, help="Frecuencia de muestreo (Hz)")
    parser.add_argument("--ciclos", type=float, default=3, help="Ciclos de la señal original a mostrar")
    args = parser.parse_args()

    F, Fs, ciclos = args.F, args.Fs, args.ciclos

    if Fs <= 0:
        raise ValueError("Fs debe ser mayor que 0")
    if ciclos <= 0:
        raise ValueError("ciclos debe ser mayor que 0")

    F_alias = frecuencia_alias(F, Fs)
    hay_aliasing = not np.isclose(F_alias, F)

    print("F: ", F)
    print("Fs: ", Fs)
    print("ciclos: ", ciclos)
    print("F_alias: ", F_alias, "Hz" + (" (hay aliasing)" if hay_aliasing else " (sin aliasing)"))

    # Duración de la ventana de tiempo, en función de los ciclos de la señal original
    f_base = abs(F) if F != 0 else Fs
    duracion = ciclos / f_base

    # Eje de tiempo "continuo" (aproximado con alta resolución) para la señal analógica
    t_cont = np.linspace(0, duracion, 5000)
    x_t = np.sin(2 * np.pi * F * t_cont)

    # Instantes y muestras discretas tomadas a Fs
    t_n = np.arange(0, duracion, 1 / Fs)
    x_n = np.sin(2 * np.pi * F * t_n)

    # Gráfico
    plt.figure(figsize=(10, 5))
    plt.title("Tarea 1")

    plt.plot(t_cont, x_t, color="red", linewidth=1.5, label=f"x(t), F = {F:g} Hz")

    if hay_aliasing:
        x_alias_t = np.sin(2 * np.pi * F_alias * t_cont)
        plt.plot(t_cont, x_alias_t, color="black", linewidth=1.5,
                  label=f"x_alias(t), F_alias = {F_alias:g} Hz")

    plt.stem(t_n, x_n, linefmt="green", markerfmt="go", basefmt=" ")
    plt.plot([], [], "go", label=f"x[n], Fs = {Fs:g} Hz")  # entrada de leyenda para las muestras

    plt.xlabel("t (s)")
    plt.ylabel("Amplitud")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
