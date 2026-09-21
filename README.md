# PDS Tarea 1
Tarea 1 del curso: Procesamiento Digital de Señales

## Pregunta 1 
- Resuelta en el documento

### Resultados
- Frecuencia de muestreo: 8 kHz; frecuencia de plegado: 4 kHz.
- Nota más alta grabable sin alias: Si₇ (n=38, ≈3951 Hz).
- El Mi♭₈ del pícolo (≈4978 Hz) aliasea a ≈3022 Hz, escuchándose como Fa♯₇.
- Se requiere un filtro anti-aliasing (pasa-bajas) antes del muestreo.

## Pregunta 2 
- Se necesita python instalado
- Instalación de dependencias: pip install matplotlib numpy
- Comando para ejecutar el script de manera generica: python3 Pregunta_2.py --F <frecuencia_Hz> --Fs <frecuencia_muestreo_Hz> --ciclos <num_ciclos>
- Ejemplo del enunciado: python3 Pregunta_2.py --F 0.714285714 --Fs 1 --ciclos 7

### Resultados
- Script parametrizable (F, Fs, ciclos) que grafica la señal original, su alias y las muestras comunes a ambas.

## Pregunta 3
- Resuelta en el documento
- Se necesita python instalado
- Instalación de dependencias: pip install matplotlib numpy
- Comando para ejecutar el script: python3 Pregunta_3.py

### Resultados
- $x(t)$ se descompone en tonos de 900, 1000 y 1100 Hz (Nyquist = 2200 Hz).
- Se elige $F_s=1000$ Hz (igual a la portadora) para eliminar su oscilación.
- Recuperación exacta: $m[n]=2x[n]-2$, verificado en Python con error ≈$10^{-16}$.
- Con fase de portadora desconocida $\phi$, el procedimiento falla si $\cos\phi=0$ (p. ej. $\phi=\pi/2$): pérdida total de información.

## Pregunta 4
- Resuelta en el documento

### Resultados
- Asignación directa (256 niveles): cuanto ≈23.53 mV.
- Punto fijo Q3.5: cuanto 31.25 mV (menor resolución por redondeo a potencia de 2).
- Suma de mediciones → Q4.4 (62.5 mV); producto → Q5.3 (125 mV).
- SQNR para señal de 3 V: 49.89 dB, 47.43 dB, 41.41 dB y 35.39 dB respectivamente.

## Pregunta 5
- Resuelta en el documento

### Resultados
- La velocidad aparente de 47 km/h es un alias espacial (video submuestreado 1:15 vs. patrón periódico de la demarcación vial, D=12 m).
- Cruzando con la evidencia de localización celular (torres a 2499.4 m, 60 s), se descartan los alias no plausibles.
- Velocidad estimada del sospechoso: ≈133 km/h ± 10 km/h.
