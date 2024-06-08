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
    <div>Figura 2. Parámetros estadísticos de la variabilidad de la frecuencia cardíaca en el dominio del tiempo. [7]</div>
</div>
<br>

<div align="center">
    <img src="/ISB/Imágenes - Multimedia/Multimedia_Lab9/rMSSD.png">
    <div>Figura 3. Cálculo del rMSSD. [9]</div>
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

A continuacion, se muestran los resultados obtenido luego de realizar la extraccion de los parametros que caraacterizan el HRV. El codigo utilizado para ello lo puede ecnontrar [aqui](https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/5b81ecc35d245ff29e78e1bbf10b284eb15236d1/ISB/Laboratorios/Laboratorio%209/PROCESAMIENTO_ECG.ipynb)
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
        <td><img src="/ISB/Imágenes - Multimedia/Multimedia_Lab9/picos_filter_respiracion.png"></td>
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
    <div>Figura 4. Gráfico de diferencia entre picos R</div>
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

### VARIACION DE LA DURACION DEL INTERVALO RR
De acuerdo a la Figura 1, podemos decir que los valores de diferencia entre picos R varían más cuando el sujeto se encontraba en reposo y respiración, mientras que cuando se encontraba realizando ejercicio, habia menos variacion entre los intervalos RR. El hecho de que haya mayor variacion de los intervalos RR, nos indica tambien un aumento de la Variabilidad de la Frecuencia Cardiaca y viceversa, es decir, que una menor variacion de la longitud del intervalos RR, una menor Variabilidad de Frecuencia Cardiaca. [10]

### VALOR DEL INTERVALO R-R

En cuanto al intervalo R-R, en la Figura 1. también podemos observar lo siguiente:

* En reposo: Los valores van desde los 700 ms a los 840 ms aproximadamente. 
* En respiración: De 800 milisegundos a 700 milisegundos aproximadamente.
* En ejercicio: Entre 450 a 575 milisegundos.

De acuerdo a ello vemos que el valor del intervalo R-R es menor cuando el sujeto se encontraba en ejercicio. Esto tiene sentido ya que el ritmo cardíaco aumenta cuando se realiza actividad física, es por ello que la duración del intervalo R-R es menor, ya que el tiempo entre latido disminuye.[10]

Los valores de reposo y respiración están en rangos de valores similares, y son mayores a los valores registrados cuando el sujeto se encontraba realizando ejercicio, dando a entender que el ritmo cardiaco disminuye cuando se está en reposo o respiracion.

### VALOR DE RMSSD

En cuanto a los valores de RMSSD que pudimos obtener, podemos observar que este es más grande cuando el sujeto está en reposo, y es menor cuando está realizando ejercicio. 

Este valor es uno de los parámetros que son considerados al momento de querer evaluar la Variabilidad de Frecuencia Cardiaca. Este valor suele ser mayor cuando la longitud del intervalo R-R varía más, y es menor cuando la longitud de este intervalo se mantiene de forma casi constante.

Es por ello que el valor es mayor cuando el sujeto se encontraba en reposo, ya que como pudimos observar en la Figura 1, la longitud del intervalo RR variaba más, en comparación a los otros 2 casos. De forma análoga, la señal obtenida cuando el sujeto realizaba ejercicio proporcionaba un valor de RMSSD bastante menor, ya que la longitud del intervalo R-R era casi constante.

En resumen, el HRV (Variabilidad de la Frecuencia Cardiaca) era mayor cuando el sujeto estaba en respiracion y reposo, y menor cuando se encontraba haciendo ejercicio.
De acuerdo a lo mencionado en "Normative Values of Heart Rate Variability During Sleep in Indian Population"[11], el HRV refleja la actividad conjunta de las 2 partes del Sistema Nervioso Autonomo, el Sistema Nervioso Simpatico y el Sistema Nervioso Parasimpatico. Se menciona tambien que el incremento de la frecuencia cardiaca es una de las respuestas del cuerpo humano ante situaciones de estres o esfuerzo, siendo esta tambien una causa de la disminucion del HRV. Por otra parte, se pone tambien de ejemplo al cuerpo humano en un estado de reposo, donde predomina el Sistema Nervioso Parasimpatico, lo que genera el aumento del HRV.

Un dato a considerar es que la cantidad de picos fue menor cuando el sujeto se encontraba en ejercicio, por lo que hubo un mayor número de muestra utilizados para calcular el RMSSD a diferencia de los 2 casos anteriores.

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

[10] M. Gusev, S. Tudjarski and A. Anagelevska, "Sampling Rate Impact on Heart Rate Variability," 2022 30th Telecommunications Forum (TELFOR), Belgrade, Serbia, 2022, pp. 1-4, doi: 10.1109/TELFOR56187.2022.9983696. 

[11]R. Aishwarya, S. P. Preejith and M. Sivaprakasam, "Normative Values of Heart Rate Variability During Sleep in Indian Population," 2023 IEEE International Symposium on Medical Measurements and Applications (MeMeA), Jeju, Korea, Republic of, 2023, pp. 1-5, doi: 10.1109/MeMeA57477.2023.10171932. 

