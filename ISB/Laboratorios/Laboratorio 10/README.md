# LABORATORIO 10 - PROCESAMIENTO DE EEG
## TABLA DE CONTENIDO

* [Introducción](#introducción)
* [Objetivos](#objetivos)
* [Filtrado](#filtrado)
* [Discusión](#discusión)
* [Bibliografía](#bibliografía)

## Introducción
### Procesamiento de la señal EEG
Sabemos que el proceso de adquisición de una señal electroencefalograma consta del posicionamiento de los electrodos, o canales, según sistemas de posicionamiento como el sistema 10-20 establecido internacionalmente o el sistema 10-10 [1]. Ambos sistemas se basan en la posición relativa entre electrodos adyacentes como se puede observar en las imágenes de abajo.

<div align="center">
    <img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/6c12496ceee0eb19fbada3c91fd4f1c66cef4220/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab10/eeg_10_10.png">
    <div>Figura 1. Posicionamiento de los electrodos de acerudo al sistema 10-10 [2] </div>
</div>
<br>

<div align="center">
    <img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/6c12496ceee0eb19fbada3c91fd4f1c66cef4220/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab10/eeg_10_20.png">
    <div>Figura 2. Posicionamiento de los electrodos de acuerdo al sistema 10-20 [3] </div>
</div>
<br>

Posterior a la adquisión de los datos a través de los diferentes canales, se obtiene un arreglo (o matriz) de señales no procesadas, cada una de las cuales presenta componentes electroencefalográficos con ciertas contribuciones provenientes de distintas regiones del cerebro [4]. Asimismo, cada sensor también se encuentra expuesto a componentes provenientes de fuentes fisiológicas no relacionadas con la actividad eléctrica cerebral como la actividad eléctrica ocular, cardíaca o muscular [5]. Estas últimas claramente no contienen información pertinente al análisis cerebral, por lo que se consideran como artefactos. Existen varias técnicas utilizadas para la eliminación de estos componentes, tales como métodos regresivos, Transformada Wavelet o métodos de separación ciega de fuentes (BSS por sus siglas en inglés) [5]. Los métodos de este último buscan solucionar el problema de la estimación de cada uno de las fuentes (cerebrales y artefactos), representados como una matriz S, así como también las contribuciones, representados como una matriz A (conocida como matriz de mezcla) y el posible ruido en cada una de las fuentes, representado por una matriz V, solamente a partir de la matriz de señales combinadas, denotada por la letra X suponiendo que la combinación de cada una de las fuentes es lineal [6].

<div align="center">
    <img src="/ISB/Imágenes - Multimedia/Multimedia_Lab10/BSS_methods.png">
    <div>Figura 3. Problema de descomposición ciega de fuentes (BSS) representadas por la matriz de fuentes S. [6] </div>
</div>
<br>

Dentro los métodos de esta última, se destaca el análisis de componentes independientes (ICA por sus siglas en inglés) el cual supone que las fuentes de la matriz S son estadísticamente independientes y no gaussianas [7]. 

Por otra parte, así como se buscó separar las fuentes de actividad cerebral de los artefactos fisiológicos provenientes de otras fuentes no cerebrales, durante el estudio del electroencefalograma, también se busca localizar espacial y temporalmente cada una de la fuentes cerebrales lo cual se conoce como estimación de fuentes. En general, esto se modela como un problema inverso en el cual se busca reconstruir la distribución espacial de las fuentes eléctricas y/o magnéticas, en el caso del magnetoencefalograma, a partir de la adquisición de estas [4].

<div align="center">
    <img src="/ISB/Imágenes - Multimedia/Multimedia_Lab10/Source_estimation.png">
    <div>Figura 4. Proceso o modelo de estimación de la distribución espacial y temporal de fuentes de actividad eléctrica del cerebro. [4] </div>
</div>
<br>

La compleja librería de Python enfocada en el preprocesado,procesamiento y análisis de señales electroencefalogramas y magnetoencefalogramas que fue utilizada en este informe, llamada *MNE*, incluye métodos de remoción de artefactos tales como el método ICA o métodos regresivos, además de métodos de estimación de fuentes y otros procesos.

## Objetivos
* Buscar señales de electroencefalogramas de varios canales a partir de base de datos públicas.
* Realizar un filtrado, en frecuencia, de la señal para obtener el rango de frecuencias, 0.5 a 30 Hz, de las ondas de un electroencefalograma.
* Eliminar componentes no cerebrales de las señales de electroencefalograma utilizando el método ICA.
* Realizar la extracción de características más importantes de las señales de electroencefalograma.

## Base de datos escogida

La señales que se emplearon fueron obtenidas de la siguiente base de datos ["Auditory evoked potential EEG-Biometric dataset"](https://physionet.org/content/auditory-eeg/1.0.0/#files-panel) la cual es de libre acceso via Physionet. 
Esta consiste de 240 señales de EEG de dos minutos de duración que fueron obtenidas de 20 voluntarios. La toma de la señal siguió los siguientes pasos:

1. Tres minutos de estado de reposo, con los ojos abiertos durante tres sesiones.
2. Tres minutos de estado de reposo, con los ojos cerrados durante tres sesiones.
3. Experimento no relacionado (no proporcionado en el conjunto de datos). Tres minutos de estado de reposo, con los ojos abiertos durante tres sesiones utilizando auriculares con aislamiento de ruido.
4. Experimento no relacionado (no proporcionado en el conjunto de datos). Tres minutos de estado de reposo, con los ojos abiertos durante tres sesiones utilizando auriculares con aislamiento de ruido.
5. Tres minutos escuchando una canción en su idioma nativo usando audífonos internos.
6. Tres minutos de escucha de una canción en un idioma no nativo utilizando auriculares internos.
7. Tres minutos de escucha de música neutra usando auriculares internos.
8. Tres minutos escuchando una canción en su idioma nativo utilizando auriculares de conducción ósea.
9. Tres minutos de escucha de una canción en un idioma no nativo utilizando auriculares de conducción ósea.
10. Tres minutos de escucha con música neutra utilizando auriculares de conducción ósea.

Dado que se tiene la información para los 10 experimentos para cada persona, resultó de interés analizar la actividad cerebral en las actividades 5 (escuchar canción en idioma nativo) y 6 (escuchar canción en idioma no nativo)

Adicionalmente, se presenta información para cuatro canales con una frecuencia de muestreo de 200 Hz.

## Filtrado de la Señal
Para el preprocesamiento de la señal, see hizo uso de la librería MNE-Python.
Para el filtrado de la señal, se hizo uso de un filtropasabanda con una frecuencia inferior de 0.48 Hz y una frecuencia superior de 30 Hz, el cual fue utilizado en el trabajo "Adaptive filtering based artifact removal from electroencephalogram (EEG) signals" [9].

Una vez realizado el filtrado, obtuvimos ambas gráficas, tanto para el sujeto que escuchaba música nativa, como aquel que escuchaba música no nativa.

<table>
    <tr>
        <th>Experimento</th>
        <th>Estado de la señal</th>
        <th>Ploteo de la señal</th>
    </tr>
    <tr>
        <td rowspan="2">Escuchando música nativa</td>
        <td>Sin Filtrar</td>
        <td><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/efd794555b1c1362e8d6620d94d44e1c296a8248/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab10/espectro_nofiltro.png"></td>
    </tr>
    <tr>
        <td>Filtrada</td>
        <td><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/efd794555b1c1362e8d6620d94d44e1c296a8248/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab10/espectro_filtrado.png"></td>
    </tr>
    <tr>
        <td rowspan="2">Escuchando música no nativa</td>
        <td>Sin Filtrar</td>
        <td><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/efd794555b1c1362e8d6620d94d44e1c296a8248/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab10/nofilter_nonative.png"></td>
    </tr>
    <tr>
        <td>Filtrada</td>
        <td><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/efd794555b1c1362e8d6620d94d44e1c296a8248/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab10/filter_nonative.png"></td>
    </tr>

</table>

## Analisis de ICA

Para un análisis más detallado de ambas señales EEG, se hizo uso de la libreria [MNE](https://mne.tools/stable/index.html) . A continuacion, mostraremos los resultados obtenidos con la herramienta mencionada anteriormente.

<table>
    <tr>
    <th>Experimento 5</th>
    <th>Esperimento 6</th>
    </tr>
    <tr>
        <td><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/7920f361dc2203e83862d9d6f765181675df29ca/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab10/ica_1.png"></td>
        <td><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/581edef149f6f48341a8a0c8153c8132c8b32efb/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab10/ica0_nonative.png"></td>
    </tr>
    <tr>
        <td><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/7920f361dc2203e83862d9d6f765181675df29ca/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab10/ica_2.png"></td>
        <td><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/581edef149f6f48341a8a0c8153c8132c8b32efb/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab10/ica1_nonative.png"></td>
    </tr>
    <tr>
        <td><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/7920f361dc2203e83862d9d6f765181675df29ca/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab10/ica_3.png"></td>
        <td><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/581edef149f6f48341a8a0c8153c8132c8b32efb/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab10/ica2_nonative.png"></td>
    </tr>
    <tr>
        <td><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/7920f361dc2203e83862d9d6f765181675df29ca/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab10/ica_4.png"></td>
        <td><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/581edef149f6f48341a8a0c8153c8132c8b32efb/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab10/ica3_nonative.png"></td>
    </tr>
</table>

Luego de ello, se obtuvo la puntuacion del ICA.
<table>
    <tr>
        <th>ICA Score (Musica en idioma nativo)</th>
        <th>ICA Score (Musica en idioma no nativo)</th>
    </tr>
        <td><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/581edef149f6f48341a8a0c8153c8132c8b32efb/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab10/ica_score_native.png"></td>
        <td><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/581edef149f6f48341a8a0c8153c8132c8b32efb/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab10/ica_score_nonative.png"></td>
    <tr>
    </tr>
</table>

## Extracción de Características

Para la extracción de características, utilizamos una DWT para este propósito, tomando como base el procedimiento realizado en el artículo *EEG Signal Analysis for Diagnosing Neurological Disorders Using Discrete Wavelet Transform and Intelligent Techniques* [8]. Las características que se tomaron en cuenta en el mismo incluyen: 
* Varianza
* SD (Desviacion Estandar)
* Kurtosis
* Entropía
* LBP (Logarithmic Band Power)

El calculo de estos parametros los hicimos de acuerdo a la siguiente tabla, la cual la hicimos basados en el trabajo anteriormente mencionado. [8]

<table>
<tr>
<th>Varianza</th>
<th>Desviacion Estandar</th>
<th>Kurtosis</th>
<th>Entropia</th>
<th>Logarithmic Band Power</th>
</tr>
<tr>
<td><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/e84916f4b2a375ea76bc96a228efef2dd2540c5e/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab10/varianza.png"></td>
<td><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/e84916f4b2a375ea76bc96a228efef2dd2540c5e/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab10/desvi.png"></td>
<td><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/e84916f4b2a375ea76bc96a228efef2dd2540c5e/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab10/kurtosis.png"></td>
<td><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/e84916f4b2a375ea76bc96a228efef2dd2540c5e/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab10/entropia.png"></td>
<td><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/e84916f4b2a375ea76bc96a228efef2dd2540c5e/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab10/lbp.png"></td>
</tr>
</table>
Utilizando el DWT para realizar un ICA (Independent Component Anlysis),obtuvimos los siguientes niveles de descomposición, cuyas gráficas mostramos a continuación.

En este caso, se observa los coeficientes de aproximación A4, y los coeficientes de detalle D1,D2,D3 y D4. Estos coeficientes nos dan información de la señal en distintos rangos de frecuencia [8], los cuales son explicados a continuación:

* A4: 0.1 Hz a 4 Hz 
* D1: 30 Hz a 60 Hz
* D2: 15 Hz a 30 Hz
* D3: 8 Hz a 15 Hz
* D4: 4 Hz a 8 Hz

<div align="center"><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/581edef149f6f48341a8a0c8153c8132c8b32efb/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab10/feature_native.png"></div>

<div align="center">Figura 5. Niveles de descomposición de los coeficientes de la señal del sujeto que escuchaba música nativa </div>

<div align="center"><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/581edef149f6f48341a8a0c8153c8132c8b32efb/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab10/feature_nonative.png"></div>

<div align="center">Figura 6. Niveles de descomposición de los coeficientes de la señal del sujeto que escuchaba música no nativa  </div>

Asimismo, mostramos también las caracterististicas de EEG del sujeto que fue sometido el experimento 5 (escuchar música en idioma nativo).
<table>
    <tr>    
        <th>Fuente de la señal/Característica</th>
        <th>Varianza</th>
        <th>SD (Desviacion Estandar)</th>
        <th>Kurtosis</th>
        <th>Entropia</th>
        <th>LBP</th>
    </tr>
        <td>Canal 0</td>
        <td>185.08</td>
        <td>13.60</td>
        <td>133.13</td>
        <td>7359745.14</td>
        <td>15.81</td>
    <tr>
        <td>Canal 1</td>
        <td>4749.88</td>
        <td>68.92</td>
        <td>34.16</td>
        <td>188874344.02</td>
        <td>19.05</td>
    </tr>
    <tr>
        <td>Canal 2</td>
        <td>192.40</td>
        <td>13.87</td>
        <td>165.12</td>
        <td>7650684.97</td>
        <td>15.85</td>
    </tr>
    <tr>
        <td>Canal 3</td>
        <td>116.25</td>
        <td>10.78</td>
        <td>140.39</td>
        <td>4622786.52</td>
        <td>15.34</td>
    </tr>
</table>


Además, también se muestran las características de EEG de la señal de aquel sujeto realizando el experimento 6 (escuchar música no nativa) 

<table>
    <tr>    
        <th>Fuente de la señal/Característica</th>
        <th>Varianza</th>
        <th>SD (Desviacion Estandar)</th>
        <th>Kurtosis</th>
        <th>Entropia</th>
        <th>LBP</th>
    </tr>
        <td>Canal 0</td>
        <td>167.78</td>
        <td>12.95</td>
        <td>154.89</td>
        <td>6911882.18</td>
        <td>15.74</td>
    <tr>
        <td>Canal 1</td>
        <td>5474.31</td>
        <td>73.98</td>
        <td>41.61</td>
        <td>225514352.60</td>
        <td>19.23</td>
    </tr>
    <tr>
        <td>Canal 2</td>
        <td>186.35</td>
        <td>13.65</td>
        <td>168.49</td>
        <td>7676796.11</td>
        <td>15.85</td>
    </tr>
    <tr>
        <td>Canal 3</td>
        <td>146.12</td>
        <td>12.08</td>
        <td>152.52</td>
        <td>6019761.26</td>
        <td>15.61</td>
    </tr>
</table>

## Discusión

En los espectros de magnitud de las señales no filtradas, lo que más resalta es la presencia de un pico alrededor de una frecuencia aproximada de 50 Hz. Esto es posible que se deba al PNS (Power Noise Signal). Este tipo de ruidos son generados por la red eléctrica, cuyas frecuencias suelen ser de 50 Hz o 60 Hz dependiendo de la zona donde se encuentre. Dado que las señales fueron adquiridas en la Marche Polytechnic University (UNIVPM), la red eléctrica suele presentar una frecuencia de 50 Hz, coincidiendo con lo observado en la gráfica de espectros de magnitud.

En la primera parte aplicamos un filtro pasabanda que tenía una frecuencia de corte que iba entre 0.48 y 30 Hz, con el objetivo de reducir frecuencias altas, incluyendo también el ruido anteriormente mencionado.

Por otro lado, analizando el ICA component score, observamos que estos valores eran muy pequeños, lo que indicaba la poca o nula presencia de artefactos en la señal, y por ende, no vimos necesario eliminar los coeficientes de algun nivel de descomposición de la señal.

Para la extracción de características, habíamos empleado una DWT Daubechies 4, como wavelet madre, y los coeficientes que analizamos fueron A4,D1,D2,D3 y D4.

En este caso, el coeficiente A4 abarcaba un rango de frecuencia de 0.1 a 4 Hz, por lo que vendría a representar la banda delta. Asimismo, siguiendo la misma lógica, el coeficiente D4, abarcaba de 4 a 8 Hz (theta), el coeficiente D3, abarcaba de 8 a 15 Hz (alpha), el coeficiente D2, abarcaba de 15 a 30 Hz (beta) y el coeficiente D1, abarcaba de 30 a 60 Hz (gamma).[8]

Asimismo, en cuanto a las caracteristicas que podemos observar, una de las que mas resalta es la entropía de la señal proveniente del Canal 1 en ambos casos, ya que podemos observar que la entropía es mucho mayor en este canal que en los demás.

La Kurtosis está defininda como una medida que representa la cantidad de valores atípicos que pueden haber presentes en una muestra [10], en este caso, la señal de EEG. Con esto en mente, podemos ver que al contrario de lo que pasaba con la entropia, la kurtosis presenta un valor menor en el canal 1 de ambos casos, en comparacion a los demas canales.




## Bibliografía

[1] V. Jurcak, D. Tsuzuki, and I. Dan, “10/20, 10/10, and 10/5 systems revisited: Their validity as relative head-surface-based positioning systems,” NeuroImage, vol. 34, no. 4. Elsevier BV, pp. 1600–1611, Feb. 2007. doi: 10.1016/j.neuroimage.2006.09.024. <br>

[2] Novo-Olivas, Carlos & Guitiérrez, Leticia & Bribiesca, José. (2010). Mapeo Electroencefalográfico y Neurofeedback. 

[3] Korats, Gundars & Cam, Steven & Ranta, Radu & Hamid, Mohamed. (2013). Applying ICA in EEG: Choice of the Window Length and of the Decorrelation Method. Communications in Computer and Information Science. 357, 2013. 269-286. 10.1007/978-3-642-38256-7_18. 

[4] S. P. Ahlfors and M. S. Hämäläinen, “MEG and EEG: source estimation,” in Handbook of Neural Activity Measurement, R. Brette and A. Destexhe, Eds. Cambridge: Cambridge University Press, 2012, pp. 257–286 <br>

[5] X. Jiang, G.-B. Bian, and Z. Tian, “Removal of Artifacts from EEG Signals: A Review,” Sensors, vol. 19, no. 5. MDPI AG, p. 987, Feb. 26, 2019. doi: 10.3390/s19050987. <br>

[6] A. Kachenoura, L. Albera, and L. Senhadji, “Blind source separation methods applied to synthesized polysomnographic recordings: a comparative study,” 2007 29th Annual International Conference of the IEEE Engineering in Medicine and Biology Society. IEEE, Aug. 2007. doi: 10.1109/iembs.2007.4353177. <br>

[7] Puntonet, C.G., Górriz, J.M., Salmerón, M., Hornillo-Mellado, S. (2004). Theoretical Method for Solving BSS-ICA Using SVM. In: Puntonet, C.G., Prieto, A. (eds) Independent Component Analysis and Blind Signal Separation. ICA 2004. Lecture Notes in Computer Science, vol 3195. Springer, Berlin, Heidelberg. https://doi.org/10.1007/978-3-540-30110-3_33 <br>

[8] Alturki, Fahd A.; AlSharabi, Khalil; Abdurraqeeb, Akram M.; Aljalal, Majid (2020). EEG Signal Analysis for Diagnosing Neurological Disorders Using Discrete Wavelet Transform and Intelligent Techniques. Sensors, 20(9), 2505–. doi:10.3390/s20092505 <br>

[9] R. Kher and R. Gandhi, "Adaptive filtering based artifact removal from electroencephalogram (EEG) signals," 2016 International Conference on Communication and Signal Processing (ICCSP), Melmaruvathur, India, 2016, pp. 0561-0564, doi: 10.1109/ICCSP.2016.7754202. 

[10] “Resumir: Estadísticos.” Www.ibm.com, www.ibm.com/docs/es/spss-statistics/saas?topic=summarize-statistics.