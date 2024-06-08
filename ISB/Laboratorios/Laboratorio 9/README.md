# LABORATORIO 9 - PROCESAMIENTO DE ECG
## TABLA DE CONTENIDO

* [Introducción](#introducción)
* [Objetivos](#objetivos)
* [Filtrado](#filtrado)
* [Heart Rate Variability](#hrv---heart-rate-variability)
* [Valores rMSSD](#valores-de-rmssd)
* [Discusión](#discusión)
* [Bibliografía](#bibliografía)

## Introducción
Anteriormente, se trabajó el filtrado de la señal electrocardiograma. Ahora es turno de realizar la extracción de características más importantes respecto a esta señal. En este entregable, solo nos enfocaremos en la extracción y análisis de la variabilidad de la frecuencia cardíaca, aun así, existen otras características importantes en la detección de enfermedades cardíacas y estudios fisiológicos tales como la detección de los complejos QRS, las onda P y las onda Q obtenidas, por ejemplo, a través de un análisis en descomposición de la señal usando distintas Wavelets [1][2] debido a la no estacionariedad del electrocardiograma [3]. De manera general, se puede trabajar en 4 dominios, o dimensiones, de la señal que traen consigo distintas herramientas, como la descomposición por Wavelets, y algoritmos, como el algoritmo Pan Tompkins, para la extracción de características [4][5]. 

<div align="center">
    <img src="/ISB/Imágenes - Multimedia/Multimedia_Lab9/Characteristics_EKG.png">
    <div>Figura 1. Vista General de Distintos Métodos de Extracción de Características en los distintos Dominios. [4]</div>
</div>
<br>

El análisis de la variabilidad de la frecuencia cardíaca (HRV por sus en inglés) parte de la identificación de los picos R que se puede llevar a cabo en el dominio del tiempo utilizando el ya mencionado algoritmo Pan Tompkins o, en el dominio tiempo-frecuencia, usando la transformada Wavelet Estacionaria [6]. Una vez identificado las posiciones de los picos R, se procede a realizar el cálculo de distintas medidas estadísticas, en el dominio del tiempo, que resuman y compacten la variabilidad de la frecuencia cardíaca. Algunas de estas medidas más importantes son la raíz de la media cuadrada de las diferencias de intervalos RR consecutivos (rMSSD por sus siglas en inglés) y la desviación estándar de las diferencias de intervalos RR consecutivos [7][8]. 

<div align="center">
    <img src="/ISB/Imágenes - Multimedia/Multimedia_Lab9/HRV_Characteristics.png">
    <div>Figura 2. Parámetros estadísticos de la variabilidad de la frecuencia cardíaca en el dominio del tiempo [7]</div>
</div>
<br>

<div align="center">
    <img src="/ISB/Imágenes - Multimedia/Multimedia_Lab9/rMSSD.png">
    <div>Figura 3. Cálculo del rMSSD [9]</div>
</div>

## Objetivos 
* Ubicar los picos R de los electrocardiogramas obtenidos previamente utilizando la librería [scipy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks.html) de Python.
* Realizar el cálculo del rMSSD a partir de los picos R obtenidos.
* Discutir los resultados obtenidos.
## Filtrado

Antes de extraer las características del ECG, se vio conveniente realizar el filtrado correspondiente de la señal. A continuación, mostramos una breve comparativa entre las señales filtradas, usando el filtro Wavelet del [laboratorio 7](lhttps://github.com/sofia-is-a-panda/ISB_2024_G3/tree/main/ISB/Laboratorios/Laboratorio%207), y sin filtrar.
<table>
    <tr>
        <th>Estado del sujeto</th>
        <th>Señal</th>
    </tr>
    <tr>
        <th>Reposo</th>
        <td><img src= "/ISB/Imágenes - Multimedia/Multimedia_Lab9/filtro_reposo.png" ></td>
    </tr>
    <tr>
        <th>Respiración</th>
        <td><img src= "/ISB/Imágenes - Multimedia/Multimedia_Lab9/filtro_respiracion.png"></td>
    </tr>
    <tr>
        <th>Ejercicio</th>
        <td><img src="/ISB/Imágenes - Multimedia/Multimedia_Lab9/filtro_ejercicio.png"></td>
    </tr>

</table>

## HRV - Heart Rate Variability

### Ubicación de Picos R

<table>
    <tr>
        <th>Estado del sujeto</th>
        <th>Estado de la señal</th>
        <th>Ploteo de la señal</th>
    </tr>
    <tr>
        <td rowspan="2">Reposo</td>
        <td>Sin Filtrar</td>
        <td><img src="/ISB/Imágenes - Multimedia/Multimedia_Lab9/picos_nofilter_reposo.png"></td>
    </tr>
    <tr>
        <td>Filtrada</td>
        <td><img src="/ISB/Imágenes - Multimedia/Multimedia_Lab9/picos_filter_reposo.png"></td>
    </tr>
    <tr>
        <td rowspan="2">Respiración</td>
        <td>Sin Filtrar</td>
        <td><img src="/ISB/Imágenes - Multimedia/Multimedia_Lab9/picos_nofilter_respiracion.png"></td>
    </tr>
    <tr>
        <td>Filtrada</td>
        <td><img src="/ISB/Imágenes - Multimedia/Multimedia_Lab9/filtro_respiracion.png"></td>
    </tr>
    <tr>
        <td rowspan="2">Ejercicio</td>
        <td>Sin Filtrar</td>
         <td><img src="/ISB/Imágenes - Multimedia/Multimedia_Lab9/picos_nofilter_ejercicio.png"></td>       
    </tr>
    <tr>
        <td>Filtrada</td>
        <td><img src="/ISB/Imágenes - Multimedia/Multimedia_Lab9/picos_filter_ejercicio.png"></td>
    </tr>
</table>

### Comparación de la Diferencia Entre Picos R

<div align="center">
    <img src="/ISB/Imágenes - Multimedia/Multimedia_Lab9/picos_R_diff.png">
    <div>Figura 2. Gráfico de diferencia entre picos R</div>
</div>

### Valores de RMSSD
<div align="center">
    <table>
        <tr>
            <th>Estado</th>
            <th>Valor de RMSSD</th>
        </tr>
        <tr>
            <th>Reposo</th>
            <td>48.42</td> 
        </tr>
        <tr>
            <th>Respiración</th>
            <td>30.65</td>
        </tr>
        <tr>
            <th>Ejercicio</th>
            <td>13.79</td>
        </tr>
    </table>
</div>

## Discusión

## Bibliografía
[1] Bhyri C, Hamde ST, Waghmare LM. ECG feature extraction and disease diagnosis. J Med Eng Technol. 2011 Aug-Oct;35(6-7):354-61. doi: 10.3109/03091902.2011.595530. <br> 
[2] I. Patel, A. Sandhya, V. S. Raja, and S. Saravanan, “Extraction of Features from ECG Signal,” International Journal of Current Research and Review, vol. 13, no. 08. Radiance Research Academy, pp. 103–109, 2021. doi: 10.31782/ijcrr.2021.13806. <br>
[3] B. Lenka, "Time-frequency analysis of non-stationary electrocardiogram signals using Hilbert-Huang Transform," 2015 International Conference on Communications and Signal Processing (ICCSP), Melmaruvathur, India, 2015, pp. 1156-1159, doi: 10.1109/ICCSP.2015.7322686 <br>
[4] Singh, A.K., Krishnan, S. ECG signal feature extraction trends in methods and applications. BioMed Eng OnLine 22, 22 (2023). doi: https://doi.org/10.1186/s12938-023-01075-1 <br>
[5] J. D. Peshave and R. Shastri, "Feature extraction of ECG signal," 2014 International Conference on Communication and Signal Processing, Melmaruvathur, India, 2014, pp. 1864-1868, doi: 10.1109/ICCSP.2014.6950168 <br>
[6] Yun, Donghwan, et al. “Robust R-Peak Detection in an Electrocardiogram with Stationary Wavelet Transformation and Separable Convolution.” Scientific Reports, vol. 12, no. 1, 16 Nov. 2022, p. 19638, www.nature.com/articles/s41598-022-19495-9#Sec16, https://doi.org/10.1038/s41598-022-19495-9. <br>
[7] Pham T, Lau ZJ, Chen SHA, Makowski D. Heart Rate Variability in Psychology: A Review of HRV Indices and an Analysis Tutorial. Sensors (Basel). 2021 Jun 9;21(12):3998. doi: 10.3390/s21123998 <br>
[8] C. A. Calvert, “Heart Rate Variability,” Veterinary Clinics of North America: Small Animal Practice, vol. 28, no. 6. Elsevier BV, pp. 1409–1427, Nov. 1998. doi: 10.1016/s0195-5616(98)50129-5 <br>
[9] C. Wang and J. Guo, “A data-driven framework for learners’ cognitive load detection using ECG-PPG physiological feature fusion and XGBoost classification,” Procedia Computer Science, vol. 147. Elsevier BV, pp. 338–348, 2019. doi: 10.1016/j.procs.2019.01.234