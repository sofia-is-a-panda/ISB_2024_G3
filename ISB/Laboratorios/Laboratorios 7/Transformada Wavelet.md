# LABORATORIO 7 - TRANSFORMADA WAVELET
## TABLA DE CONTENIDO

* [Introducción](#introducción)
* [Objetivos](#objetivos)
* [Filtrado de EMG](#filtrado-de-emg)
* [Filtrado de ECG](#filtrado-de-ecg)
* [Filtrado de EEG](#filtrado-de-eeg)
* [Discusiones](#discusiones)
* [Conclusiones](#conclusiones)
* [Bibliografía](#bibliografía)

## Introducción

La transformada Wavelet...

## Objetivos
* Usar la transformada Wavelet para filtrar señales de EMG, ECG, EEG.
## Filtrado de EMG

## Filtrado de ECG

## Filtrado de EEG
Nuestro trabajo siguió el enfoque propuesto en el artículo "Automated Classification and Removal of EEG Artifacts with SVM and Wavelet-ICA", específicamente en la sección B, que describe el "Procedure for Wavelet Multiresolution Analysis".

Comenzamos aplicando WMA a las señales EEG registradas con el fin de mantener solo las bandas de frecuencia de interés. Cada canal de la señal se descompuso utilizando la Transformada Discreta de Wavelet (DWT) en 8 niveles utilizando la wavelet madre db8. Durante este proceso, eliminamos los detalles en los niveles D1 y D2, que representan el rango de frecuencia de 32 a 128 Hz, y también la wavelet madre A8, que cubre el rango de frecuencia de 0 a 0.5 Hz. Esto nos permitió conservar los detalles relevantes de D8 a D3, que corresponden al rango de frecuencia de interés para las señales EEG, es decir, de 0.5 a 32 Hz. Estos detalles de la wavelet representan las bandas de frecuencia tradicionales de las señales EEG, como las bandas delta, theta, alpha y beta.



## Discusiones

### EEG
Es importante destacar que las señales EEG suelen estar contaminadas por artefactos biológicos y ambientales en entornos prácticos. Los artefactos biológicos provienen de fuentes no cerebrales en el cuerpo humano, como la actividad cardíaca, ocular o muscular, mientras que los artefactos ambientales provienen de fuentes externas, como el movimiento de electrodos o la interferencia de dispositivos externos. Estos artefactos pueden distorsionar las señales EEG, dificultando el diagnóstico clínico o las aplicaciones de interfaz cerebro-computadora (BCI). [X]

Los métodos tradicionales para eliminar artefactos EEG, como los filtros lineales o las regresiones, pueden causar una pérdida significativa de la actividad cerebral observada debido a la superposición espectral entre la actividad neurológica y los artefactos de señal. Por el contrario, el análisis multirresolución con wavelets utilizando la DWT ha demostrado ser más efectivo para eliminar artefactos mientras se preservan las características esenciales de las señales EEG en los dominios de tiempo y frecuencia. [X]

En el caso de nuestro trabajo, el código reflejó fielmente este procedimiento. Utilizamos la biblioteca pywt de Python para aplicar la DWT y filtrar los coeficientes de la wavelet según lo descrito en el artículo. Hicimos uso de la wavelet madre db8 y ajustamos los parámetros según las especificaciones del estudio. La visualización de los resultados mostró claramente la señal EEG original, los niveles de wavelet y la señal filtrada.

El procedimiento demostró ser efectivo al filtrar la mayoría de los artefactos fuera del rango de frecuencia de interés, incluido el ruido de alta frecuencia (>32 Hz) y el movimiento de tendencia lineal a frecuencias extremadamente bajas (<0.5 Hz). Esto lo podemos evidenciar en los gráficos obtenidos donde la señal filtrada conservaba las características de interés mientras eliminaba los artefactos no deseados, lo que indica que el método implementado fue efectivo. Esto subraya la importancia crítica de un buen filtrado en el análisis de señales EEG. Un filtrado adecuado es fundamental para obtener resultados precisos y confiables en aplicaciones de monitoreo y diagnóstico médico basadas en señales EEG, ya que permite separar las señales de interés de las interferencias no deseadas.

## Conclusiones

## Bibliografía
