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

### ¿Cuáles son las limitaciones de la Transformada de Fourier?
La Transformada de Fourier es una herramienta muy poderosa en el análisis de una gran cantidad de señales, debido a que permite descomponer una señal continua o discreta, a través de la Transformada Continua o la Transformada en Tiempo Discreto de Fourier, en los distinos componentes frecuenciales que conforman la señal. En otras palabras, esta herramienta nos permite expandir el análisis de la señal a no únicamente el dominio del tiempo, sino también al dominio de la frecuencia [1].

Aunque la Transformada de Fourier sea una herramienta poderosa, ciertamente esta posee limitaciones o problemas que dificultan el análisis de las señales como es el caso de la fuga espectral en el caso del análisis de señales de duración finita utilizando la Transformada Discreta de Fourier [2]. Uno de los problemas críticos de la Transformada de Fourier es que no otorga información de cuánto dura un cierto componente frecuencial en el dominio del tiempo, o en palabras más simples, que el dominio de la frecuencia se vuelve ciego al dominio del tiempo. Este problema, aunque para señales sencillas que presenten un comportamiento "altamente" periódico no resulte un gran problema, en el caso de señales más complejas, como es el caso de las señales biomédicas, esto sí representa un gran impedimento para extraer información valiosa de estas señales dado su naturaleza no estacionaria[3].

### ¿Es posible solucionar esto?
Podríamos pensar que, si tomar toda la señal por completo en el dominio del tiempo y hallar su transformada haría que no pueda localizar la ubicación temporal de sus componentes frecuenciales; entonces, lo mejor sería tomar pequeños trozos (formalmente conocidos como ventanas) de la señal en el dominio del tiempo y hallar la transformada de cada uno de ellos, de esta manera lograría localizar temporalmente las frecuencias que obtendría de cada una de las transformadas. Efectivamente, este es el razonamiento que sigue la Transformada De Fourier de Tiempo Corto para analizar una señal en distintos intervalos de tiempo [4]. 

Sin embargo, se puede demostrar matemáticamente que, mientras más pequeña sea la ventana, el rango de frecuencias que conforman tal ventana se dispersará cada vez más haciendo que los verdaderos componentes de frecuencia, los de mi señal completa, se encuentren en un rango de frecuencias cada vez más amplio sin que uno conozca dónde se encuentran con total certeza. Esto es una conclusión directa del principio de incertidumbre de Heisenberg [5].

<p align="center" style="margin-bottom:0">
<img src="/ISB/Imágenes - Multimedia/Multimedia - Lab7/Heisenberg Principle.png" align="center"/>
<div align="center"> <i>Fig. 1. Principio de Incertidumbre de Heisenberg. La integral de la izquierda representa el dominio del tiempo y la integral de la derecha el dominio de la frecuencia. Ambas integrales expresan la dispersión del tiempo y frecuencia, respectivamente. [5]</i></div>
</p>

Por tanto, siempre se tiene un intercambio entre resolución temporal y resolución frecuencial que se desean. Dado que la Transformada en Tiempo Corto de Fourier utiliza ventanas de una misma duración temporal, entonces la distinción de frecuencias altas, en caso se utilicen ventanas amplias, se dificulta [6]. 

### Transformada de Wavelet:

La Transformada de Wavelet, a diferencia de la Transformada en Tiempo Corto de Fourier, no utiliza ventanas de un mismo tamaño, sino que esta "adecúa" el tamaño de las ventanas, a través de funciones conocidas como *wavelets*,  haciendo que frecuencias más altas tengan ventanas más pequeñas que para las frecuencias más bajas [6]. A partir de esto, la Transformada de Wavelet gana una mayor resolución temporal para frecuencias más altas que la Transformada en Tiempo Corto de Fourier. 



## Objetivos
* Usar la transformada Wavelet para filtrar señales de EMG, ECG, EEG.
  
## Filtrado de EMG

Se siguió la metodología que presenta en el artículo: "Surface electromyography signal denoising via EEMD and improved wavelet thresholds", específicamente la sección 2.2 "Extract the useful component from the first IMF and Remove the noise"  para la selección de la Transformada Discreta de Wavelet (Sym8) que se empleó [7]. Adicionalmente, para la selección del threshold o umbral, se hizo uso de “Adaptive Wavelet Thresholding for Image Denoising and Compression” donde se detalla que este valor es la mediana de los coeficientes de primer nivel de la transformada de Wavelet entre 0.6745 [8].
Se comienza aplicando la Transformada Discreta de Wavelet (Symlet 8 - Sym8) debido a que es la wavelet que presenta el mejor efecto de eliminación de ruido. Luego se procede a elegir el nivel de descomposición, esta se realizó de la siguiente manera:
Se calcula la relación de señal-ruido (SNR) donde se emplea la potencia de la señal
Se determina si los coeficientes de la wavelet presentan ruido mediante la comparación respecto a un umbral.
Se halla el nivel de descomposición máximo, luego se calcula si estos coeficientes son mayoritariamente ruido, si esto se cumple se disminuye en uno el nivel de descomposición y se vuelve iterar hasta llegar a un nivel.


A continuación presentamos los resultados obtenidos después de realizar el procedimiento mencionado en cual fue implementado en un [notebook](https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/main/ISB/Laboratorios/Laboratorios%207/EMG_WAVELET.ipynb). Recordar que realizamos el procedimiento las tomas de la señal:
* Primera Señal (Reposo): Tomamos una señal de 6 segundos mientras el voluntario estaba en reposo. 

* Segunda Señal (Tensión): El voluntario se encontraba inicialmente en reposo, luego realizó una fuerza de tensión por aproximadamente 8 segundos. 

* Tercera Señal (Oposición): El voluntario se encontraba inicialmente en reposo, luego realizó una fuerza de oposición respecto a otra persona por aproximadamente 4 segundos.

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/main/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab7/Wavelet_Se%C3%B1alReposo.png" align="center"/>
<div align="center"> <i>Fig. 2. Señal EMG original vs filtrada en Reposo</i></div>
</p>

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/main/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab7/Wavelet_Se%C3%B1alTensi%C3%B3n.png" align="center"/>
<div align="center"> <i>Fig. 3. Señal EMG original vs filtrada en Tensión</i></div>
</p>

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/main/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab7/Wavelet_Se%C3%B1alOposici%C3%B3n.png" align="center"/>
<div align="center"> <i>Fig. 4. Señal EMG original vs filtrada en Oposición</i></div>
</p>

## Filtrado de ECG

Para el filtrado de la señal, se usó como base el trabajo “Simulation for Design the Compressed ECG Signal Transmission System with Baseline Wander Noise”.[9] 

Para el análisis de la señal se utilizó una DWT Daubechie de tipo “db6”, se escogieron 6 niveles de descomposición, y el umbral seleccionado fue de 0.22, ya que era, tal como indicaba el artículo mencionado anteriormente.[9] 

Con ello, luego de haber realizado la descomposición de coeficientes, el umbral se encargará de eliminar todos aquellos coeficientes inferiores al valor de umbral establecido.

Una vez eliminados los coeficientes, se hará la reconstrucción mediante IDWT de múltiple niveles.

Para el desarrollo del código, se utilizó Google Colab, donde también fue necesaria la implementación de la librería “pywt” (PyWavelets - Wavelet Transforms in Python). 

Se utilizaron las 3 señales de ECG, las cuales fueron tomadas durante momentos y actividades distintas del voluntario:

* Primera señal de ECG : Estado de Reposo
* Segunda señal de ECG : Ciclos de respiración
* Tercera Señal de ECG : Actividad física seguido de descanso

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/4563ed79b720d716c675f407ee061e73e6505320/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab7/descomp_reposo.png" align="center"/>
<div align="center"> <i>Fig. 3. Niveles de descomposición de los coeficientes de la señal ECG en reposo</i></div>
</p>


<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/4563ed79b720d716c675f407ee061e73e6505320/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab7/ecg_reposo.png" align="center"/>
<div align="center"> <i>Fig. 3. Comparación de un tramo entre la señal ECG en reposo original y filtrada</i></div>
</p>


<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/4563ed79b720d716c675f407ee061e73e6505320/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab7/decomp_respiracion.png" align="center" />
<div align="center"> <i>Fig. 3. Niveles de descomposición de los coeficientes de la señal ECG en ciclos de respiración</i></div>
</p>

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/4563ed79b720d716c675f407ee061e73e6505320/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab7/ecg_respiracion.png" align="center" />
<div align="center"> <i>Fig. 3. Comparación de un tramo entre la señal ECG en ciclos de respiración original y filtrada</i></div>
</p>

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/4563ed79b720d716c675f407ee061e73e6505320/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab7/descomp_ejercicio.png" align="center" />
<div align="center"> <i>Fig. 3. Niveles de descomposición de los coeficientes de la señal ECG en ciclos de respiración</i></div>
</p>

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/4563ed79b720d716c675f407ee061e73e6505320/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab7/ecg_ejercicio.png" align="center" />
<div align="center"> <i>Comparación de un tramo entre la señal ECG en ejercicio original y filtrada</i></div>
</p>

## Filtrado de EEG
Nuestro trabajo siguió el enfoque propuesto en el artículo "Automated Classification and Removal of EEG Artifacts with SVM and Wavelet-ICA", específicamente en la sección B, que describe el Procedimiento para el Análisis Multirresolución con Wavelet, WMA. [11]

Comenzamos aplicando WMA a las señales EEG registradas con el fin de mantener solo las bandas de frecuencia de interés. Cada canal de la señal se descompuso utilizando la Transformada Discreta de Wavelet (DWT) en 8 niveles utilizando la wavelet madre db8. Durante este proceso, eliminamos los detalles en los niveles D1 y D2, que representan el rango de frecuencia de 32 a 128 Hz, y también la wavelet madre A8, que cubre el rango de frecuencia de 0 a 0.5 Hz. Esto nos permitió conservar los detalles relevantes de D8 a D3, que corresponden al rango de frecuencia de interés para las señales EEG, es decir, de 0.5 a 32 Hz. Estos detalles de la wavelet representan las bandas de frecuencia tradicionales de las señales EEG, como las bandas delta, theta, alpha y beta. [11]

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

### EMG

Nuestro código reflejó fielmente este procedimiento. Utilizamos la biblioteca pywt (PyWavelets) y PyEMD de Python para aplicar la DWT. De la librería pywt se emplearon “wavedec”, “threshold”, “waverec”. Mientras, que de la librería PyEMD se empleó EEMD para la eliminación de ruido utilizando el modo empírico de conjunto descomposición el cual correspondió al método empleado en la literatura [1]. La visualización de los resultados mostró claramente la señal EMG original y la señal filtrada.

Los gráficos obtenidos evidenciaron que la señal filtrada conservaba las características de interés mientras se atenuaron picos bruscos y la señal se tenía más suavizada, lo que indica que el método implementado fue efectivo. 


### ECG

En una señal de electrocardiograma (ECG), existen varios tipos de ruido que afectan su calidad, y por ende, hacen que su análisis e interpretación sea mucho más complicada. De los ruidos y/o artefactos que pueden perjudicar la señal existen los siguientes [10]:

- <strong>Desplazamiento de línea de base:</strong> Se trata de un ruido que puede ser ocasionado por movimientos de la persona evaluada, movimiento de extremidades y el ritmo de respiración. Este tipo de ruido suele tener una baja frecuencia, de alrededor de 0.1 Hz.

- <strong>Interferencia de red eléctrica:</strong> Uno de los ruidos más conocidos es el ocasionado por la red eléctrica. Esta señal suele tener una frecuencia de 50 Hz o 60 Hz dependiendo de donde se encuentre. Afectan la señal medida ya que disminuyen el ratio señal a ruido (SNR).

- <strong>Ruido electromiográfico:</strong> Ocasionado por la actividad de las fibras musculares, este tipo de ruidos son de alta frecuencia y no tienen una amplitud ni frecuencia determinada, lo que hace que los métodos de cancelación de ruido convencionales difícilmente ayuden a eliminarlo.

En cuanto a los niveles de descomposición, tenemos que todos aquellos coeficientes que tengan un valor menor a 0.22, serán atenuados hasta tener un valor de 0, que es lo que se le conoce como “soft thresholding”. Estos coeficientes podemos observarlos en los niveles de descomposición 4 a 6, en las señales de reposo y respiración, mientras que abarca los niveles 5 y 6 de la señal en ejercicio. 

Respecto a las gráficas comparativas entre la señal original y la señal filtrada, podemos observar que, en los 3 casos evaluados de ECG el filtrado ha resultado efectivo, lo que indica que el método y procedimiento utilizado fueron los adecuados.

### EEG
Es importante destacar que las señales EEG suelen estar contaminadas por artefactos biológicos y ambientales en entornos prácticos. Los artefactos biológicos provienen de fuentes no cerebrales en el cuerpo humano, como la actividad cardíaca, ocular o muscular, mientras que los artefactos ambientales provienen de fuentes externas, como el movimiento de electrodos o la interferencia de dispositivos externos. Estos artefactos pueden distorsionar las señales EEG, dificultando el diagnóstico clínico o las aplicaciones de interfaz cerebro-computadora (BCI). [11]

Los métodos tradicionales para eliminar artefactos EEG, como los filtros lineales o las regresiones, pueden causar una pérdida significativa de la actividad cerebral observada debido a la superposición espectral entre la actividad neurológica y los artefactos de señal. Por el contrario, el análisis multirresolución con wavelets utilizando la DWT ha demostrado ser más efectivo para eliminar artefactos mientras se preservan las características esenciales de las señales EEG en los dominios de tiempo y frecuencia. [11]

En el caso de nuestro trabajo, el código reflejó fielmente este procedimiento. Utilizamos la biblioteca pywt de Python para aplicar la DWT y filtrar los coeficientes de la wavelet según lo descrito en el artículo. Hicimos uso de la wavelet madre db8 y ajustamos los parámetros según las especificaciones del estudio. La visualización de los resultados mostró claramente la señal EEG original, los niveles de wavelet y la señal filtrada.

El procedimiento demostró ser efectivo al filtrar la mayoría de los artefactos fuera del rango de frecuencia de interés, incluido el ruido de alta frecuencia (>32 Hz) y el movimiento de tendencia lineal a frecuencias extremadamente bajas (<0.5 Hz). Esto lo podemos evidenciar en los gráficos obtenidos donde la señal filtrada conservaba las características de interés mientras eliminaba los artefactos no deseados, lo que indica que el método implementado fue efectivo. Esto subraya la importancia crítica de un buen filtrado en el análisis de señales EEG. Un filtrado adecuado es fundamental para obtener resultados precisos y confiables en aplicaciones de monitoreo y diagnóstico médico basadas en señales EEG, ya que permite separar las señales de interés de las interferencias no deseadas.


## Bibliografía

[1] J. Semmlow, “Fourier Transform,” Signals and Systems for Bioengineers. Elsevier, pp. 81–129, 2012. doi: 10.1016/b978-0-12-384982-3.00003-1. <br>

[2] A. Breitenbach, “Against spectral leakage,” Measurement, vol. 25, no. 2. Elsevier BV, pp. 135–142, Mar. 1999. doi: 10.1016/s0263-2241(98)00074-8. <br>

[3] M. S. Manikandan and S. Dandapat, “Wavelet-based electrocardiogram signal compression methods and their performances: A prospective review,” Biomedical Signal Processing and Control, vol. 14. Elsevier BV, pp. 73–107, Nov. 2014. doi: 10.1016/j.bspc.2014.07.002. <br>

[4] N. Kehtarnavaz, “Frequency Domain Processing,” Digital Signal Processing System Design. Elsevier, pp. 175–196, 2008. doi: 10.1016/b978-0-12-374490-6.00007-6. <br>

[5] Gröchenig, K. (2003). Uncertainty Principles for Time-Frequency Representations. In: Feichtinger, H.G., Strohmer, T. (eds) Advances in Gabor Analysis. Applied and Numerical Harmonic Analysis. Birkhäuser, Boston, MA. https://doi.org/10.1007/978-1-4612-0133-5_2 <br>

[6] Daubechies, "The wavelet transform, time-frequency localization and signal analysis," in IEEE Transactions on Information Theory, vol. 36, no. 5, pp. 961-1005, Sept. 1990, doi: 10.1109/18.57199 <br>

[7] Z. Sun, X. Xi, C. Yuan, Y. Yang, and X. Hua, “Surface electromyography signal denoising via EEMD and improved wavelet thresholds,” Mathematical Biosciences and Engineering, vol. 17, no. 6, pp. 6945–6962, 2020, doi: https://doi.org/10.3934/mbe.2020359 <br>

[8]S. G. Chang, Bin Yu, and M. Vetterli, “Adaptive wavelet thresholding for image denoising and compression,” IEEE Transactions on Image Processing, vol. 9, no. 9, pp. 1532–1546, 2000, doi: https://doi.org/10.1109/83.862633. <br>

[9] Ali Abdrhman Ukasha, Mousa Hasan Omar, and Mabrouka Idrees Fadel, “Simulation for Design the Compressed ECG Signal Transmission System with Baseline Wander Noise,” May 2023, doi: https://doi.org/10.1109/iecres57315.2023.10209428 <br>

[10]  F. Shi, "A review of noise removal techniques in ECG signals," 2022 IEEE Conference on Telecommunications, Optics and Computer Science (TOCS), Dalian, China, 2022, pp. 237-240, doi: 10.1109/TOCS56154.2022.10015982. keywords: {Noise reduction;Interference;Electrocardiography;White noise;Wavelet analysis;Optics;Electromyography;ECG;Denoising;Wavelet threshold;modal decomposition;threshold},

[11] T. Olund, J. Duun-Henriksen, T. W. Kjaer, y H. B. D. Sorensen, “Automatic detection and classification of artifacts in single-channel EEG”, en 2014 36th Annual International Conference of the IEEE Engineering in Medicine and Biology Society, 2014, vol. 2014. 

