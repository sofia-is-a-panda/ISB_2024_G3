# LABORATORIO 6 - FILTRADO DE SEÑALES BIOMÉDICAS
## TABLA DE CONTENIDO

* [Introducción](#introducción)
* [Objetivos](#objetivos)
* [Filtrado de EMG](#filtrado-de-emg)
* [Filtrado de ECG](#filtrado-de-ecg)
* [Filtrado de EEG](#filtrado-de-eeg)
* [Discusiones](#discusiones)
* [Bibliografía](#bibliografía)

## Introducción

En el ámbito de la ingeniería biomédica, filtrar señales es de suma relevancia para su correcto análisis e interpretación. Las señales biomédicas como la electromiografía (EMG), electrocardiografía (ECG) o electroencefalografía (EEG) suelen ser afectadas por ruido o artefactos, lo cual puede llevar a un diagnóstico o análisis erróneo [1]. Por lo tanto, el filtrado de señales, previo a su procesamiento, se convierte en un paso fundamental para eliminar el ruido no deseado y corregir posibles distorsiones, permitiendo así un análisis más preciso y fiable de los datos biomédicos. En este laboratorio, nos enfocaremos en el diseño de filtros digitales que actuén en el dominio de la frecuencia de la señal, permitiendo atenuar una banda de frecuencias, lo que eliminaría los componentes de tales frecuencias en el dominio del tiempo. 
Los filtros digitales más sencillos utilizados son los filtros no recursivos, también llamados FIR (Finite Impulse Response), y los filtros recursivos, también llamados IIR (Infinite Impulse Response) [2], siendo ambos sistemas lineales e invariantes en el tiempo; sin embargo, también existen otros tipos de filtros que sirven en el estudio de procesos estocásticos frente a señales no determinísticas (i.e. estocásticas) como es el caso de la señal EKG que es considerada como una señal no estacionaria dado que la recolección de esta señal se ve afectada por otros factores estocásticos como potenciales del músculo o ruido del exterior [3]. Para esto último, existen otras técnicas de análisis que involucran la descomposición multirresolucional de la señal (MSD) utilizando otro tipos de transformadas como la transformada de Wavelet [4] o la transformada de Hilbert-Huang [3].

### Filtros Ideales y Filtros Reales
Idealmente, se busca que la banda de paso de un filtro tengan una ganancia de 0 dB en todas las frecuencias de paso; mientras que la banda de rechazo sea atenuada totalmente de tal manera que los componentes de las frecuencias de rechazo de la señal de entrada desaparezcan por completo. Sin embargo, la realización de este tipo de filtros no es posible en la realidad debido a que la formulación matemática de este tipo de filtros involucra el uso de sistemas no causales los cuales son físicamente imposibles [5]; por lo tanto, los filtros reales representan aproximaciones a tal versión idealizada. 

<p align="center" style="margin-bottom:0">
<img src="/ISB/Imágenes - Multimedia/Multimedia - Lab 6/Filtros-ideales.png" align="center"/>
<div align="center"> <i>Fig. 1. Filtros ideales. Recuperado de [6] </i></div>
<p>

<p align="center" style="margin-bottom:0">
<img src="/ISB/Imágenes - Multimedia/Multimedia - Lab 6/Filtros-reales.png" align="center"/>
<div align="center"> <i>Fig. 2. Filtro pasa bajo real. Recuperado de [6] </i></div>
<p>

Como podemos observar, los filtros pasa bajo reales poseen una banda de paso, limitada por una frecuencia de paso $w_p$; una banda de transición y una banda de rechazo, limitada por una frecuencia de rechazo $w_s$. Por otro lado, también podemos observar un rizado $\delta$ en ambas bandas que determinan a su vez el nivel de atenuación de la banda de rechazo respecto de la banda de paso.

### Filtros FIR (Finite Impulse Response)

Los filtros FIR son filtros en los que la salida es una combinación lineal de shifteos de la señal de entrada en el dominio del tiempo. Matemáticamente, esto se expresa como [2]: 

$$y[n]=\sum_{k=0}^{M} b_k x[n-k]$$

<p align="center" style="margin-bottom:0">
<img src="/ISB/Imágenes - Multimedia/Multimedia - Lab 6/Diagrama_de_bloques_FIR.png" align="center" width="400" height="100"/>
<div align="center"> <i>Fig. 3. Diagrama de bloques de filtro FIR de quinto orden. Recuperado de [7]</i></div>
<p>

Donde los coeficientes de la combinación lineal representan los valores de la respuesta al impulso que claramente es de duración finita.
De igual manera, se puede obtener la función de transferencia H(z) de un filtro FIR a través de los coeficientes de la combinación lineal [8]:

$$H[z]=\sum_{k=0}^{M} b_k z^{-k}$$

Uno de los métodos existentes y más utilizados para el diseño de filtros FIR es el método de las ventanas que proporciona una forma simple de calcular los coeficientes necesarios para obtener las bandas de paso y bandas de rechazo deseadas. En este método, existen distintos tipos de ventanas, aproximaciones matemáticas, cada una con ventajas y desventajas dentro de las cuales se encuentran las ventanas rectangular, Hamming, Hanning, Bartle, etc [8].


<p align="center" style="margin-bottom:0">
<img src="/ISB/Imágenes - Multimedia/Multimedia - Lab 6/Ventanas.png" align="center" width="600" height="200"/>
<div align="center"> <i>Fig. 4. Diagramas de Bode de las distintas ventanas. Recuperado de [7]</i></div>
<p>


<p align="center" style="margin-bottom:0">
<img src="/ISB/Imágenes - Multimedia/Multimedia - Lab 6/Ventanas_FIR.png" align="center" width="600" height="200"/>
<div align="center"> <i>Fig. 5. Tipos de ventanas y sus características. Recuperado de [8]</i></div>
<p>

### Filtros IIR (Infinite Impulse Response)

A diferencia de los filtros FIR, en los filtros IIR, la salida del filtro es calculada haciendo uso de la entrada y además de valores pasados de la salida, por este motivo, también son llamados filtros recursivos. La ecuación que representa la salida es la siguiente [9]:
$$y[n]=\sum_{k=0}^N b_k x[n-k] - \sum_{k=0}^M a_k y[n-k]$$

De igual manera, la función de transferencia H está dada por [9]:

<p align="center" style="margin-bottom:0">
<img src="/ISB/Imágenes - Multimedia/Multimedia - Lab 6/Transferencia_IIR.png" align="center"/>
<div align="center"> <i>Fig. 6. Función de transferencia de un filtro IIR. Recuperado de [9]</i></div>
<p>

Los métodos de desarrollo de estos filtros para establecer los coeficientes $b_k$ y $a_k$ necesarios para especificar una frecuencia de paso, frecuencia de rechazo y los rizados involucran mucha más fondo matemático que los filtros FIR, por lo que los programas o librerías de procesamiento digital de señales incluyen funciones para hallar tales coeficientes.

## Objetivos
* Diseñar filtros FIR e IIR para señales de EMG, ECG, EEG.
* Filtrar señales de EMG, ECG, EEG que se obtuvieron de forma experimental en los laboratorios.

## Filtrado de EMG
| Filtros|
| :---:  |
![filtros emg](https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/main/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab%206/Filtros.png)



| Señales                               |
| :-----------------------------------: |
| ![Señal 1](https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/main/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab%206/Se%C3%B1alReposo.png)        |
| ![Señal 2](https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/main/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab%206/Se%C3%B1alOposici%C3%B3n.png)        |
| ![Señal 3](https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/main/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab%206/Se%C3%B1alTensi%C3%B3n.png)        |


## Filtrado de ECG

## Filtrado de EEG

## Discusiones

## Bibliografía
[1] Y. Zhou, Bingo Wing-Kuen Ling, and X. Zhou, “Biomedical Signal Denoising Via Permutating, Thresholding and Averaging Noise Components Obtained from Hierarchical Multiresolution Analysis-Based Empirical Mode Decomposition,” Circuits, systems, and signal processing, vol. 42, no. 2, pp. 943–970, Sep. 2022, doi: https://doi.org/10.1007/s00034-022-02142-z. <br>

[2] R. Hamming, Digital Filters. Dover Publications, 1998. Disponible en: https://books.google.com.pe/books?id=JQ35s71Vv10C&printsec=frontcover&hl=es&source=gbs_ge_summary_r&cad=0#v=onepage&q&f=false <br>

[3] B. Lenka, "Time-frequency analysis of non-stationary electrocardiogram signals using Hilbert-Huang Transform," 2015 International Conference on Communications and Signal Processing (ICCSP), Melmaruvathur, India, 2015, pp. 1156-1159, doi: 10.1109/ICCSP.2015.7322686 <br>

[4] M. S. Manikandan and S. Dandapat, “Wavelet-based electrocardiogram signal compression methods and their performances: A prospective review,” Biomedical Signal Processing and Control, vol. 14. Elsevier BV, pp. 73–107, Nov. 2014. doi: 10.1016/j.bspc.2014.07.002. <br>

[5] W. Alexander and C. Williams, “Design of Digital Filters,” Digital Signal Processing. Elsevier, pp. 205–275, 2017. doi: 10.1016/b978-0-12-804547-3.00004-8.<br>

[6] V. Giurgiutiu, “Signal Processing and Pattern Recognition for Structural Health Monitoring with PWAS Transducers,” Structural Health Monitoring with Piezoelectric Wafer Active Sensors. Elsevier, pp. 807–862, 2014. doi: 10.1016/b978-0-12-418691-0.00014-9.<br>

[7] “FIR Filters by Windowing - The Lab Book Pages,” www.labbookpages.co.uk. http://www.labbookpages.co.uk/audio/firWindowing.html <br>

[8] P. P. VAIDYANATHAN, “Design and Implementation of Digital FIR Filters,” Handbook of Digital Signal Processing. Elsevier, pp. 55–172, 1987. doi: 10.1016/b978-0-08-050780-4.50007-2. <br>

[9] E. Lai, “Infinite impulse response (IIR) filter design,” Practical Digital Signal Processing. Elsevier, pp. 145–170, 2003. doi: 10.1016/b978-075065798-3/50007-2. <br>

