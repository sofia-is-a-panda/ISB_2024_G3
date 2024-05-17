# LABORATORIO 7 - TRANSFORMADA WAVELET
## TABLA DE CONTENIDO

* [Introducción](#introducción)
* [Objetivos](#objetivos)
* [Filtrado de EMG](#filtrado-de-emg)
* [Filtrado de ECG](#filtrado-de-ecg)
* [Filtrado de EEG](#filtrado-de-eeg)
* [Discusiones](#discusiones)
* [Bibliografía](#bibliografía)

## Introducción

La transformada Wavelet...

## Objetivos
* Usar la transformada Wavelet para filtrar señales de EMG, ECG, EEG.
## Filtrado de EMG

Se siguió la metodología que presenta en el artículo: "Surface electromyography signal denoising via EEMD and improved wavelet thresholds", específicamente la sección 2.2 "Extract the useful component from the first IMF and Remove the noise" [1].

Se comienza aplicando la Transformada Discreta de Wavelet (Symlet 8 - Sym8) debido a que es la wavelet que presenta el mejor efecto de eliminación de ruido. Luego se procede a elegir el nivel de descomposición, esta se realizó de la siguiente manera:

WMA demostró ser efectivo al filtrar la mayoría de los artefactos fuera del rango de frecuencia de interés

A continuación presentamos los resultados obtenidos después de realizar el procedimiento mencionado en cual fue implementado en un [notebook](https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/df1e5a4322037259225f096a596b8ed1e24f184e/ISB/Laboratorios/Laboratorios%207/WAVELET_EEG%20(1).ipynb).. Recordar que realizamos el procedimiento las tomas de la señal:

Reposo: Tomamos una señal de 6 segundos mientras el voluntario estaba en reposo.
Tensión: El voluntario se encontraba inicialmente en reposo, luego realizó una fuerza de tensión por aproximadamente 8 segundos.
Oposición: El voluntario se encontraba inicialmente en reposo, luego realizó una fuerza de oposición respecto a otra persona por aproximadamente 4 segundos.

<div align="center"> <i>Fig. 1. Coeficientes de Wavelet para la señal EMG. </i></div>

## Filtrado de ECG


<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/4563ed79b720d716c675f407ee061e73e6505320/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab7/descomp_reposo.png" align="center"/>
<div align="center"> <i>Fig. 3. Diagrama de bloques de filtro FIR de quinto orden. Recuperado de [7]</i></div>
</p>


<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/4563ed79b720d716c675f407ee061e73e6505320/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab7/ecg_reposo.png" align="center"/>
<div align="center"> <i>Fig. 3. Diagrama de bloques de filtro FIR de quinto orden. Recuperado de [7]</i></div>
</p>


<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/4563ed79b720d716c675f407ee061e73e6505320/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab7/decomp_respiracion.png" align="center" />
<div align="center"> <i>Fig. 3. Diagrama de bloques de filtro FIR de quinto orden. Recuperado de [7]</i></div>
</p>

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/4563ed79b720d716c675f407ee061e73e6505320/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab7/ecg_respiracion.png" align="center" />
<div align="center"> <i>Fig. 3. Diagrama de bloques de filtro FIR de quinto orden. Recuperado de [7]</i></div>
</p>

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/4563ed79b720d716c675f407ee061e73e6505320/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab7/descomp_ejercicio.png" align="center" />
<div align="center"> <i>Fig. 3. Diagrama de bloques de filtro FIR de quinto orden. Recuperado de [7]</i></div>
</p>

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/4563ed79b720d716c675f407ee061e73e6505320/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab7/ecg_ejercicio.png" align="center" />
<div align="center"> <i>Fig. 3. Diagrama de bloques de filtro FIR de quinto orden. Recuperado de [7]</i></div>
</p>

## Filtrado de EEG
Nuestro trabajo siguió el enfoque propuesto en el artículo "Automated Classification and Removal of EEG Artifacts with SVM and Wavelet-ICA", específicamente en la sección B, que describe el Procedimiento para el Análisis Multirresolución con Wavelet, WMA. [3]

Comenzamos aplicando WMA a las señales EEG registradas con el fin de mantener solo las bandas de frecuencia de interés. Cada canal de la señal se descompuso utilizando la Transformada Discreta de Wavelet (DWT) en 8 niveles utilizando la wavelet madre db8. Durante este proceso, eliminamos los detalles en los niveles D1 y D2, que representan el rango de frecuencia de 32 a 128 Hz, y también la wavelet madre A8, que cubre el rango de frecuencia de 0 a 0.5 Hz. Esto nos permitió conservar los detalles relevantes de D8 a D3, que corresponden al rango de frecuencia de interés para las señales EEG, es decir, de 0.5 a 32 Hz. Estos detalles de la wavelet representan las bandas de frecuencia tradicionales de las señales EEG, como las bandas delta, theta, alpha y beta. [3]

A continuación presentamos los resultados obtenidos después de realizar el procedimiento mencionado con la ayuda de un código de Python, el cual pueden encontrar [aquí](https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/df1e5a4322037259225f096a596b8ed1e24f184e/ISB/Laboratorios/Laboratorios%207/WAVELET_EEG%20(1).ipynb). Recordar que realizamos el procedimiento para tres casos de tomas de señales distintas:

* Reposo: Tomamos una señal de 30 segundos mientras el voluntario estaba en reposo con los ojos cerrados.
* Ciclo de abrir y cerrar ojos: El voluntario realizó un ciclo de abrir y cerrar los ojos con una duración de 5 segundos cada acción.
* Resolviendo problemas matemáticos: El voluntario resolvió problemas matemáticos de baja dificultad que se le dictaron en voz alta. Todos los cálculos los realizó mentalmente.

<div align="center">
  
*Niveles de Wavelet para la señal EEG en reposo*

</div>

![reposo_niveles](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/5b147606-5616-4ed4-b3a1-380e2fc5f023)

<div align="center">
  
*Resultados de la señal EEG en reposo original y filtrada*

</div>

![REPOSO_RESULTADOS](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/9bf9e9dc-e97f-450b-bd89-a21fb550a9ae)

<div align="center">
  
*Niveles de Wavelet para la señal EEG en el ciclo de abrir y cerrar ojos*

</div>

![OJOS_NIVELES](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/a18493d5-70cc-492c-88a2-be785ad3d5e0)

<div align="center">
  
*Resultados de la señal EEG en el ciclo de abrir y cerrar ojos original y filtrada*

</div>


![OJOS_RESULTADOS](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/1ff3a2c1-afb6-4d8d-9d71-5c2768b02dcb)

<div align="center">
  
*Niveles de Wavelet para la señal EEG resolviendo problemas matemáticos*

</div>

![MAT_NIVELES](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/69b607f3-a285-4a0a-abd6-ada0a4919829)

<div align="center">
  
*Resultados de la señal EEG resolviendo problemas matemáticos original y filtrada*

</div>

![MAT_RESULTDOS](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/8448107a-1fbc-479c-9fd9-3cff8796674b)


## Discusiones

### EEG
Es importante destacar que las señales EEG suelen estar contaminadas por artefactos biológicos y ambientales en entornos prácticos. Los artefactos biológicos provienen de fuentes no cerebrales en el cuerpo humano, como la actividad cardíaca, ocular o muscular, mientras que los artefactos ambientales provienen de fuentes externas, como el movimiento de electrodos o la interferencia de dispositivos externos. Estos artefactos pueden distorsionar las señales EEG, dificultando el diagnóstico clínico o las aplicaciones de interfaz cerebro-computadora (BCI). [3]

Los métodos tradicionales para eliminar artefactos EEG, como los filtros lineales o las regresiones, pueden causar una pérdida significativa de la actividad cerebral observada debido a la superposición espectral entre la actividad neurológica y los artefactos de señal. Por el contrario, el análisis multirresolución con wavelets utilizando la DWT ha demostrado ser más efectivo para eliminar artefactos mientras se preservan las características esenciales de las señales EEG en los dominios de tiempo y frecuencia. [3]

En el caso de nuestro trabajo, el código reflejó fielmente este procedimiento. Utilizamos la biblioteca pywt de Python para aplicar la DWT y filtrar los coeficientes de la wavelet según lo descrito en el artículo. Hicimos uso de la wavelet madre db8 y ajustamos los parámetros según las especificaciones del estudio. La visualización de los resultados mostró claramente la señal EEG original, los niveles de wavelet y la señal filtrada.

El procedimiento demostró ser efectivo al filtrar la mayoría de los artefactos fuera del rango de frecuencia de interés, incluido el ruido de alta frecuencia (>32 Hz) y el movimiento de tendencia lineal a frecuencias extremadamente bajas (<0.5 Hz). Esto lo podemos evidenciar en los gráficos obtenidos donde la señal filtrada conservaba las características de interés mientras eliminaba los artefactos no deseados, lo que indica que el método implementado fue efectivo. Esto subraya la importancia crítica de un buen filtrado en el análisis de señales EEG. Un filtrado adecuado es fundamental para obtener resultados precisos y confiables en aplicaciones de monitoreo y diagnóstico médico basadas en señales EEG, ya que permite separar las señales de interés de las interferencias no deseadas.


## Bibliografía

[1] Z. Sun, X. Xi, C. Yuan, Y. Yang, and X. Hua, “Surface electromyography signal denoising via EEMD and improved wavelet thresholds,” Mathematical Biosciences and Engineering, vol. 17, no. 6, pp. 6945–6962, 2020, doi: https://doi.org/10.3934/mbe.2020359.

[2] Ali Abdrhman Ukasha, Mousa Hasan Omar, and Mabrouka Idrees Fadel, “Simulation for Design the Compressed ECG Signal Transmission System with Baseline Wander Noise,” May 2023, doi: https://doi.org/10.1109/iecres57315.2023.10209428.

[3] T. Olund, J. Duun-Henriksen, T. W. Kjaer, y H. B. D. Sorensen, “Automatic detection and classification of artifacts in single-channel EEG”, en 2014 36th Annual International Conference of the IEEE Engineering in Medicine and Biology Society, 2014, vol. 2014.

