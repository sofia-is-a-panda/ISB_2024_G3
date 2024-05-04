# LABORATORIO 6 - FILTROS FIR E IIR
## TABLA DE CONTENIDO

* [Introducción](#introducción)
* [Objetivos](#objetivos)
* [Filtrado de EMG](#filtrado-de-emg)
* [Filtrado de ECG](#filtrado-de-ecg)
* [Filtrado de EEG](#filtrado-de-eeg)
* [Discusiones](#discusiones)
* [Bibliografía](#bibliografía)

## Introducción

En el ámbito de la ingeniería biomédica, filtrar señales es de suma relevancia. Las señales biomédicas, como las obtenidas durante los laboratorios, es decir la electromiografía (EMG), electrocardiografía (ECG) y electroencefalografía (EEG), suelen ser afectadas por ruido, lo cual puede llevar a un diagnóstico erróneo [1]. Por lo tanto, el filtrado de señales se convierte en un paso fundamental para eliminar el ruido no deseado y corregir posibles distorsiones, permitiendo así un análisis más preciso y fiable de los datos biomédicos. 
En este laboratorio, nos enfocaremos en el diseño de filtros FIR e IIR, herramientas fundamentales para abordar estos desafíos y mejorar la calidad de las señales biomédicas procesadas.

### Filtros FIR (Finite Impulse Response)

Este tipo de filtro depende únicamente de los valores de entrada, por lo que se le considera como un filtro no recursivo [2]. La ecuación que representa la salida del filtro es la siguiente:
$$y[n]=\sum_{k=0}^{M} b_k x[n-k]$$

De forma gráfica, se puede apreciar en el diagrama de bloques que las entradas pasadas tienen un valor de peso el cual varía

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/main/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab%206/Diagrama_de_bloques_FIR.png" align="center" width="400" height="100"/>
<div align="center"> <i>Fig. 1 Diagrama de bloques de filtro FIR de quinto orden. Recuperado de [3]</i></div>
<p>

Uno de los métodos existentes para el diseño de filtros FIR es el método de las ventanas. 

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/main/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab%206/Ventanas.png" align="center" width="600" height="200"/>
<div align="center"> <i>Fig. 2 Ejemplos de ventanas. Recuperado de [3]</i></div>
<p>

### Filtros IIR (Infinite Impulse Response)

A diferencia de los filtros IIR, la salida del filtro es calculada haciendo uso de la entrada y además de valores pasados de la salida. La ecuación que representa la salida es la siguiente:
$$y[n]=\sum_{k=0}^{\infty} b_k x[n-k]$$
## Objetivos
* Diseñar filtros 3 FIR e IIR para señales de EMG, ECG, EEG
* Filtrar señales de EMG, ECG, EEG que se obtuvieron de forma experimental en los laboratorios

## Filtrado de EMG

## Filtrado de ECG

## Filtrado de EEG

## Discusiones

## Bibliografía
[1] Y. Zhou, Bingo Wing-Kuen Ling, and X. Zhou, “Biomedical Signal Denoising Via Permutating, Thresholding and Averaging Noise Components Obtained from Hierarchical Multiresolution Analysis-Based Empirical Mode Decomposition,” Circuits, systems, and signal processing, vol. 42, no. 2, pp. 943–970, Sep. 2022, doi: https://doi.org/10.1007/s00034-022-02142-z. <br>

[2]G. Ellis, “Chapter 9 - Filters in Control Systems,” ScienceDirect, Jan. 01, 2012. https://www.sciencedirect.com/science/article/abs/pii/B9780123859204000096 <br>

[3]“FIR Filters by Windowing - The Lab Book Pages,” www.labbookpages.co.uk. http://www.labbookpages.co.uk/audio/firWindowing.html <br>
