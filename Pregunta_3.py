import numpy as np
import matplotlib.pyplot as plt

# Parámetros del problema
F_portadora = 1000   # Hz
F_info = 100          # Hz
Fs = 1000             # Hz, elegida en la parte b)
ciclos = 3             # ciclos del tono de 100 Hz a mostrar

# Duración total: 3 ciclos del tono de información
T = ciclos / F_info

# --- Señales "continuas" (resolución fina, solo para graficar) ---
t_fino = np.linspace(0, T, 5000)
x_continua = (1 + 0.5 * np.cos(2 * np.pi * F_info * t_fino)) * np.cos(2 * np.pi * F_portadora * t_fino)
m_continua = np.cos(2 * np.pi * F_info * t_fino)

# --- Muestras reales tomadas a Fs ---
n = np.arange(0, np.floor(T * Fs) + 1)
t_muestras = n / Fs
x_muestras = (1 + 0.5 * np.cos(2 * np.pi * F_info * t_muestras)) * np.cos(2 * np.pi * F_portadora * t_muestras)

# --- Recuperación de m[n] a partir de x[n], según el procedimiento derivado ---
m_recuperado = 2 * (x_muestras - 1)          # m[n] = 2x[n] - 2
m_directo = np.cos(2 * np.pi * F_info * t_muestras)  # calculado directamente de m(t)

# --- Comparación numérica ---
error = m_recuperado - m_directo
print(f"{'n':>3} {'t (ms)':>8} {'m_recuperado':>14} {'m_directo':>12} {'error':>12}")
for i in range(len(n)):
    print(f"{int(n[i]):3d} {t_muestras[i]*1000:8.3f} {m_recuperado[i]:14.6f} {m_directo[i]:12.6f} {error[i]:12.2e}")
print(f"\nError máximo absoluto: {np.max(np.abs(error)):.2e}")

# --- Gráfica 1: x(t) y sus muestras ---
fig, axs = plt.subplots(2, 1, figsize=(9, 8))

axs[0].plot(t_fino * 1000, x_continua, 'b-', label="x(t)")
axs[0].plot(t_muestras * 1000, x_muestras, 'ro', label=f"x[n], Fs = {Fs} Hz")
axs[0].set_xlabel("t (ms)")
axs[0].set_ylabel("Amplitud")
axs[0].set_title("Señal modulada x(t) y sus muestras")
axs[0].legend()
axs[0].grid(True)

# --- Gráfica 2: m(t) y las muestras recuperadas ---
axs[1].plot(t_fino * 1000, m_continua, 'b-', label="m(t)")
axs[1].plot(t_muestras * 1000, m_recuperado, 'go', label="m[n] recuperado")
axs[1].set_xlabel("t (ms)")
axs[1].set_ylabel("Amplitud")
axs[1].set_title("Tono de información m(t) y muestras recuperadas")
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.savefig("pregunta3_resultado.png", dpi=150)
plt.show()