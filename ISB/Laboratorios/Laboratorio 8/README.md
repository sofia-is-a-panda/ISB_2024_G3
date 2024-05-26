# LABORATORIO 8 - PROCESAMIENTO DE EMG
## TABLA DE CONTENIDO

* [Introducción](#introducción)
* [Objetivos](#objetivos)
* [Filtrado](#filtrado)
* [Segmentación](#segmentación)
* [Extracción de características](#extracción-de-características)
* [Discusiones](#discusiones)
* [Bibliografía](#bibliografía)

## Introducción
Anteriormente, se utilizaron 3 tipos distintos distintos de filtros para conseguir una señal más limpia del electromiograma, estas fueron filtros FIR, IIR y tipo Wavelet. Sin embargo, estos filtros presentan ventajas y desventajas como por ejemplo el gran tamaño computacional para realizar filtros FIR de gran orden y la escasa lineariedad de la fase en el caso de los filtros IIR [1]; por lo que es necesario realizar una comparación, utilizando la señal EMG capturada anteriormente, para establecer, mediante el Signal-Noise Ratio (SNR) el cual es un valor altamente significativo en la comparación entre entre el ruido y la señal [2], cuál es la mejor opción para utilizar frente a este tipo de señales.

<p align="center" style="margin-bottom:0">
<img src="/ISB/Imágenes - Multimedia/Multimedia - Lab 8/SNR.png" align="center"/>
<div align="center"> <i>Fig. 1. Razón Ruido-Señal (SNR por sus siglas en inglés) [2] </i></div>
</p>


Una vez establecido el tipo de filtro más adecuado y habiendo filtrado la señal correspondiente, finalmente se puede realizar la extracción de características más importantes de la señal, entre las cuales podemos encontrar los valores Root Mean Square, Mean Absolute Value, Kurtosis y Zero Crossing [3].
## Objetivos
* Comparar los filtros FIR, IIR y Wavelet en el caso de EMG.
* Extraer características de la señal EMG adquirida en el laboratorio

## Comparación de Filtros:
## Extracción de características:

### Reposo

### Tensión

### Oposición

## Discusiones

### Comparación entre tensión y oposición

## Bibliografía
[1] R. Pal, “Comparison of the design of FIR and IIR filters for a given specification and removal of phase distortion from IIR filters,” 2017 International Conference on Advances in Computing, Communication and Control (ICAC3). IEEE, Dec. 2017. doi: 10.1109/icac3.2017.8318772. <br>

[2] É. Thibault, F. L. Désilets, B. Poulin, M. Chioua, and P. Stuart, “Comparison of signal processing methods considering their optimal parameters using synthetic signals in a heat exchanger network simulation,” Computers &amp; Chemical Engineering, vol. 178. Elsevier BV, p. 108380, Oct. 2023. doi: 10.1016/j.compchemeng.2023.108380. <br>

[3] T. Oo and P. Phukpattaranont, “Signal-to-Noise Ratio Estimation in Electromyography Signals Contaminated with Electrocardiography Signals,” Fluctuation and Noise Letters, vol. 19, no. 03. World Scientific Pub Co Pte Lt, p. 2050027, Feb. 17, 2020. doi: 10.1142/s0219477520500273.