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

| Señales                               |
| :-----------------------------------: |
| ![Señal 4](https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/5fc379c6565f3b6fae136db10cdbe91b48f2012f/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab%206/senalnormal.png)        |
| ![Señal 5](https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/5fc379c6565f3b6fae136db10cdbe91b48f2012f/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab%206/senalfiltrada_fir.png)        |
| ![Señal 6](https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/5fc379c6565f3b6fae136db10cdbe91b48f2012f/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab%206/senalfiltrada_iir.png)        |


## Filtrado de EEG
Para plotear las señales utilizamos el procedimiento señalado en una investigación realizada acerca del método de estimulación sonora y el análisis de cambios en el EEG para el desarrollo de terapias digitales que puedan estimular el sistema nervioso: Activación cortical y potencial de sustitución de medicamentos [10]. En dicha investigación se señala que podemos aplicar un filtro Butterworth de 1 a 40 Hz y un filtro notch de 50 Hz con un factor de calidad de 30. Después de eso, se subdividen los EEG en bandas delta (0.5-4 Hz), theta (4-8 Hz), alpha (8-13 Hz), beta (13-30 Hz) y gamma (30-45 Hz) para poder analizarlas. 

FILTRADO DE SEÑALES EN REPOSO Y SEPARACIÓN POR BANDAS UTILIZANDO FILTRO IIR:
![reposo_iir](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/122c1b3c-ecd5-48dc-a057-5d4303a6602c)

DFT DE SEÑALES EN REPOSO Y SEPARACIÓN POR BANDAS UTILIZANDO FILTRO IIR:
![DFT_REPOSO_IIR](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/d52cfbc5-9cd3-4dc0-995e-ae50f0aa900a)

FILTRADO DE SEÑALES EN REPOSO Y SEPARACIÓN POR BANDAS UTILIZANDO FILTRO FIR:
![REPOSO_FIR](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/4dc664c0-e610-428f-8b80-9c776bf7651c)

DFT DE SEÑALES EN REPOSO Y SEPARACIÓN POR BANDAS UTILIZANDO FILTRO FIR:
![REPOSO_DFT_FIR](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/c42023d9-b8dd-4258-ab01-689c9b732e73)

FILTRADO DE SEÑALES EN CICLO DE ABRIR Y CERRAR OJOS Y SEPARACIÓN POR BANDAS UTILIZANDO FILTRO IIR:
![OJOS_IIR](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/d5880857-13cd-495e-8820-62c0280c659a)

DFT DE SEÑALES EN CICLO DE ABRIR Y CERRAR OJOS Y SEPARACIÓN POR BANDAS UTILIZANDO FILTRO IIR:
![DFT_OJOS](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/187ece2b-1f30-4e99-8477-b6deb70de8db)

FILTRADO DE SEÑALES EN CICLO DE ABRIR Y CERRAR OJOS Y SEPARACIÓN POR BANDAS UTILIZANDO FILTRO FIR:
![OJOS_FIR](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/57383afe-d397-4414-b2d2-7155d8bed742)

DFT DE SEÑALES EN CICLO DE ABRIR Y CERRAR OJOS Y SEPARACIÓN POR BANDAS UTILIZANDO FILTRO FIR:
![DFT_OJOS_FIR](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/a41c2466-0528-4a3d-8e51-08768558f22f)

FILTRADO DE SEÑALES REALIZANDO PROBLEMAS MATEMÁTICOS Y SEPARACIÓN POR BANDAS UTILIZANDO FILTRO IIR:
![MATE_IIR](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/902b29ef-c6b2-4630-bc8a-e0c0ad467e50)

DFT DE SEÑALES REALIZANDO PROBLEMAS MATEMÁTICOS Y SEPARACIÓN POR BANDAS UTILIZANDO FILTRO IIR:
![DFT_ MAT](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/e6da6925-cd38-41f2-be14-055d37b641be)

FILTRADO DE SEÑALES REALIZANDO PROBLEMAS MATEMÁTICOS Y SEPARACIÓN POR BANDAS UTILIZANDO FILTRO FIR:
![DFT_FIR](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/05236b43-741c-4be4-a3a1-022218ab08e1)

DFT DE SEÑALES REALIZANDO PROBLEMAS MATEMÁTICOS Y SEPARACIÓN POR BANDAS UTILIZANDO FILTRO FIR:
![DFT_MAT_FIT](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/36454ea2-4737-4b2a-9852-f0ec3074b7bf)

## Discusiones

### EEG:
Como mencionamos anteriormente para plotear las señales utilizamos  un filtro Butterworth de 1 a 40 Hz y un filtro notch de 50 Hz con un factor de calidad de 30. Después de eso, se subdividen los EEG en bandas delta (0.5-4 Hz), theta (4-8 Hz), alpha (8-13 Hz), beta (13-30 Hz) y gamma (30-45 Hz) para poder analizarlas [10]. 

Después de realizar el procedimiento podemos ver los siguientes resultados con la elección del filtro IIR:
* Reposo: Cuando analizamos las señales nos damos cuenta que el filtro está amortiguando demasiado la señal y ya no podemos distinguir con claridad las sinusoidales. Al hallar la DFT podemos notar algunas frecuencias importantes. Debemos mencionar que la frecuencia que está en 0 Hz hace referencia al componente DC de la señal del EEG, También podemos observar unas frecuencias aproximadamente en 20 Hz, 40 Hz y 60 Hz en la señal original. Y después de filtrar la señal podemos ver que estas frecuencias han desaparecido, lo cual indicaría que el filtro está funcionando de manera correcta. Además, apreciamos picos en aproximadamente 10 Hz en la banda alfa, lo cual es correcto al momento de compararlo con la literatura ya que estos son característicos de un EEG de una persona normal despierta en la región occipital de la cabeza [11]. También podemos apreciar frecuencias de aproximadamente 20 Hz  en la región betta, lo cual también es correcto y son bastante frecuentes en adultos y niños, estos son característicos de la región frontal y central del cerebro [11]. Y finalmente también encontramos frecuencias en aproximadamente 40 Hz, en la banda gamma, dicho ritmo gamma se ha atribuido a la percepción sensorial que integra diferentes áreas [11].
  
* Ciclo de abrir y cerrar ojos: Igualmente, nos damos cuenta que el filtro está amortiguando demasiado la señal y ya no podemos distinguir con claridad las sinusoidales. Al hallar la DFT podemos notar algunas frecuencias importantes. Debemos mencionar que la frecuencia que está en 0 Hz hace referencia al componente DC de la señal del EEG. Cuando ploteamos las DFT, podemos notar que la señal original es más ruidosa que la anterior y tiene frecuencias en 10, 20, 50, 60 Hz. Después de pasarla por el filtro podemos notar que estas frecuencias se han atenuado, lo cual indicaría que el filtro está funcionando de manera correcta. No vemos frecuencias en la banda delta, lo cual es correcto ya que estas se ven en el sueño profundo [11]. Tampoco vemos frecuencias en la banda theta, lo cual es correcto ya que estas se presentan en las etapas iniciales del sueño. Pero encontramos además las frecuencias en las bandas alfa (10 Hz), betta (20 Hz) y gamma (40 Hz) que como ya explicamos anteriormente, son señales normales y características en adultos.
  
* Respuestas a preguntas matemáticos: Por último, podemos notar los mismos inconvenientes que en las otras dos señales. Pero al momento de analizar su DFT notamos que tampoco hay frecuencias en las bandas delta y theta como era de esperarse y notamos los picos característicos en las frecuencias en las bandas alfa (10 Hz), betta (20 Hz) y gamma (40 Hz) [11].

El amortiguamiento de las señales debido a los filtros puede deberse a distintos factores como el orden del filtro Butterworth, ya que afecta la respuesta de amplitud del filtro. Un orden más alto generalmente resulta en una mejor atenuación fuera de la banda de paso, pero también puede introducir más distorsión en la señal dentro de la banda de paso. También podría deberse al tipo de filtro Butterworth puede afectar cómo se atenúan las frecuencias fuera de la banda de paso. Finalmente también podemos considerar factores como las frecuencias de corte elegidas y la frecuencia de muestreo, ya que es probable que no hayamos capturado suficiente información de las señales.


En segundo lugar, para realizar el filtrado de las señales con un filtro FIR, decidimos utilizar la ventana tipo Hanning debido a que proporciona una buena supresión del ruido fuera de la banda de paso, lo que es crucial en el procesamiento de señales de EEG, donde es fundamental mantener la integridad de las señales cerebrales mientras se reduce el ruido no deseado.  Mantuvimos las mismas frecuencias de corte y filtrado por bandas mencionadas anteriormente para el filtro FIR. Como podemos apreciar en laos resultados obtenidos con el filtro FIR, vemos que no podemos distinguir muy bien las señales, pero a grandes rasgos notamos los componentes sinusoidales. 

* Reposo: al analizar las DFTs, nos damos cuenta que el filtro funcionó de manera adecuada y eliminó los ruidos y podemos apreciar las frecuencias en las bandas delta y theta como era de esperarse y notamos los picos característicos en las frecuencias en las bandas alfa (10 Hz), betta (20 Hz) y gamma (40 Hz) [11].

* Ciclo de abrir y cerrar ojos: En este caso, no se pueden apreciar las DFT de manera correcta por ende no podemos realizar un analisis de las frecuencias obtenidas.

* Respuestas a problemas matemáticos: En este caso, podemos observar que el filtro disminuyó los ruidos pero no podemos identificar las frecuncias en cada una de las bandas correspondientes.

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

[10] D. Kim, J. Woo, J. Jeong, y S. Kim, “The sound stimulation method and EEG change analysis for development of digital therapeutics that can stimulate the nervous system: Cortical activation and drug substitution potential”, CNS Neurosci. Ther., vol. 29, núm. 1, pp. 402–411, 2023. <br>

[11] C. S. Nayak y A. C. Anilkumar, EEG Normal Waveforms. StatPearls Publishing, 2023. <br>


