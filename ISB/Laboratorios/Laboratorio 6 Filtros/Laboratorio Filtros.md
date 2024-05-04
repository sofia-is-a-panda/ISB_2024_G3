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

Este tipo de filtro depende únicamente de los valores de entrada, por lo que se le considera como un filtro no recursivo. La salida de este filtro es la siguiente:
$$y[n]=\sum_{k=0}^{M} b_k x[n-k]$$

![image](https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/main/ISB/Laboratorios/Laboratorio%206%20Filtros/Imagenes/Diagrama_de_bloques_FIR.png)   
<center><i>Fig. 1 Diagrama de bloques de filtro FIR. Recuperado de [3]</i></center>



### Filtros IIR (Infinite Impulse Response)

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

[3]N. AlHinai, “Introduction to biomedical signal processing and artificial intelligence,” Biomedical Signal Processing and Artificial Intelligence in Healthcare, pp. 1–28, 2020, doi: https://doi.org/10.1016/b978-0-12-818946-7.00001-9. <br>
