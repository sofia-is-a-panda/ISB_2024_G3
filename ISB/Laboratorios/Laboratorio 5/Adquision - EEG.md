# LABORATORIO 5 – ADQUISICIÓN DE ECG CON BITALINO Y ULTRACORTEX MARK IV

## Tabla de contenidos:
* [Introducción](#introducción)
* [Objetivos](#objetivos)
* [Laboratorio](#laboratorio)
  * [Materiales y equipos](#materiales-y-equipos) 
  * [Conexiones](#conexiones)
  * [Videos de las señales](#videos-de-las-señales)
  * [Gráficos OpenBCI GUI](#gráficos-en-openbci-gui)
  * [Gráficos OpenSignals](#gráficos-en-opensignals)
  * [Gráficos en Python](#gráficos-en-python)
  * [Discusión](#discusión)
  * [Archivos](#archivos)
* [Bibliografía](#bibliografía)

## Introducción

### ¿Qué es un EEG?

El electroencefalograma (EEG) es una prueba neurofisiológica no invasiva que registra la actividad eléctrica del cerebro. Se utiliza para evaluar una amplia gama de trastornos neurológicos como epilepsia, convulsiones, trastornos del sueño y enfermedades degenerativas del cerebro [1].

El EEG se realiza colocando electrodos en el cuero cabelludo. Estos electrodos detectan los pequeños cambios de voltaje que se producen cuando las neuronas del cerebro se comunican entre sí. La actividad eléctrica se registra y se muestra como un patrón de ondas en una computadora [2].

### Partes del cerebro y conexión del EEG

El cerebro se puede clasificar en cuatro lóbulos principales (ver Figura 1), que son el lóbulo frontal (en naranja), el lóbulo parietal (en celeste), el lóbulo occipital (en amarillo) y el lóbulo temporal (en verde). Cada uno de estos lóbulos intervienen en diferentes procesos del cuerpo humano, por lo que cada uno tiene una función diferente y emite una señal distina según la actividad realizada [3].

<div align = "center">
  <img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/aee1db3c-3ddf-4f9a-82f1-b9449b4bc759" alt="Texto alternativo" style="width: 50%;">
</div>
<p align="center">Figura 1. El cerebro junto a los lóbulos que lo conforman y las funciones que cumplen. Recuperado de [3]</p>

Lóbulo Frontal: <br>
El lóbulo frontal es la región del cerebro donde se originan la mayoría de nuestros pensamientos conscientes y decisiones. 
&nbsp;

Lóbulo Parietal: <br>
El lóbulo parietal se enfoca en integrar información procedente de fuentes externas, así como retroalimentación sensorial interna de los músculos esqueléticos, extremidades, cabeza, ojos, otoconias, etc. 
&nbsp;

Lóbulo Occipital: <br>
El lóbulo occipital es la región del cerebro responsable del procesamiento visual, abarcando desde la elaboración de información visual básica como la orientación y la frecuencia espacial, hasta la diferenciación de colores y la percepción del movimiento. 
&nbsp;

Lóbulo Temporal: <br>
Finalmente, el lóbulo temporal está asociado con el procesamiento de la entrada sensorial para derivar significados superiores utilizando memorias visuales, lenguaje y asociación emocional, y está involucrado en la comprensión del lenguaje escrito y hablado [4].

### Ondas del EEG

Los diferentes tipos de ondas cerebrales en un EEG se caracterizan por tener una amplitud baja, en el caso del cerebro humano estamos hablando de microvoltios, y también presentan diferentes frecuencias, algunas más rápidas y otras más lentas. Estas ondas pueden clasificarse según su frecuencia [9]:

* Onda delta: Se encuentra en el rango de 0.5Hz a 4Hz y su amplitud varía. Está asociada con el sueño profundo o el despertar, aunque a veces puede confundirse con artefactos del cuello o la mandíbula.
* Onda Gamma: Se caracteriza por tener una frecuencia más alta, con rangos que van desde 35Hz hasta 200-400Hz. Este tipo de onda refleja cómo se maneja la conciencia.
* Onda Mu: Presenta rangos de 8Hz a 12Hz y está asociada con actividades motoras. Su actividad disminuye con el movimiento o la intención de movimiento.
* Onda Tetha: Se localiza entre los 4Hz y 7Hz y suele aparecer en situaciones de estrés emocional, como la frustración y la decepción. Sin embargo, también está asociada con la inspiración creativa y la meditación.


## Objetivos
* Obtener señales de electroencefalograma utilizando el arreglo de electrodos UltraCortex MARK IV y la tarjeta  de biosensado Cyton de 8 canales. 
* Obtener una señal de electroencefalograma utilizando el Kit BITalino (R)evolution.
* Analizar y plotear las señales obtenidas utilizando Python.

## Laboratorio 
### Materiales y equipos
<div align="center">

|  **Modelo**  | **Descripción** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| (R)EVOLUTION |   Board Kit BITalino  |       1      |
|   MARK IV    |   Ultracortex   |       1      |
| Cyton |  Tarjeta de biosensado | 1
|   -    |   Electrodos  |       3     |
|       -      |      Laptop     |       1      |
</div>

* Board Kit Bitalino [5]: <br>
El Kit de tarjeta (R)Evolution BITalino consta de una tarjeta all-in-one de obtención de bioseñales que incluye principalmente 1 sensor de EEG, 1 sensor de EKG, 1 sensor de EMG, 1 microcontrolador, 1 módulo Bluetooth, entre otras cosas como actuadores y conversores. Esta tarjeta permite capturar las bioseñales a una frecuencia de sampleo máxima de 1000 Hz a una resolución de 10 bits en los canales de sensado de EEG, EKG, EMG y EDA. <br>
&nbsp;

* UltraCortex MARK IV [6]: <br>
El UltraCortex MARK IV es un arreglo de 35 electrodos desarrollado por la plataforma OpenBCI y orientado a la obtención de electroencefalograma basado en el sistema 10-20 para el posicionamiento de electrodos. En esta oportunidad, solo se utilizarán 8 electrodos dado que se cuenta únicamente con la tarjeta de biosensado Cyton de 8 canales.<br>
&nbsp;

* Tarjeta Cyton [7] [8]: <br>
La tarjeta Cyton es una tarjeta de biosensado desarrollado por la plataforma OpenBCI al igual que el UltraCortex MARK IV. Esta solamente cuenta con 8 canales  de 24 bits y, si se requiere ampliar a 16 canales, es necesario utilizar el módulo Daisy de 8 canales extra. 
La tarjeta Cyton es compatible con la plataforma OpenBCI GUI y permite capturar las señales de electroencefalograma a una frecuencia de sampleo de 250 Hz en todos sus canales. Además, el kit incluye una llave electrónica para la comunicación Bluetooth entre la tarjeta y una PC o laptop.

### Metodología

* Conexiones y ajustes del UltraCortex MARK IV + Tarjeta Cyton: <br>
-Descarga de la plataforma OpenBCI GUI. <br>
-Alimentación de la tarjeta Cyton utilizando una batería de litio incluida en el kit de compra. <br>
-Conexión del UltraCortex MARK IV con la tarjeta Cyton. <br>
-Ajuste del UltraCortex en la cabeza del voluntario siguiendo el sistema 10-20 de posicionamiento de electrodos. <br>
-Conexión de la laptop y la tarjeta Cyton a través de la llave electrónica (dongle) incluida en el kit de compra. <br>
&nbsp;
* Conexiones y ajustes del Board Kit BITalino (R)evolution: <br>
-Descarga de la plataforma OpenSignals. <br>
-Alimentación de la tarjeta BITalino utilizando una batería de litio incluida en el kit de compra. <br>
-Conexión de los 3 electrodos (Positivo, Negativo y Referencia) a la placa de sensado a través de un conector hacia el canal de sensado de EEG. <br>
-Conectar por Bluetooth a la tarjeta BITalino con la laptop. <br>
&nbsp;
* Obtención de señales: <br>
-Obtención de las señales de electroencefalograma en un estado de reposo (respiración normal, sin movimientos oculares y ojos cerrados) durante 30 segundos. <br>
-Obtención de las señales de electroencefalograma repitiendo 5 ciclos de 10 segundos de ojos abiertos - ojos cerrados. <br>
-Obtención de las señales en reposo durante 30 segundos nuevamente. <br>
-Obtención de las señales en un estado de razonamiento lógico-matemático a través de preguntas leídas por un agente externo. <br>

### Conexiones
* UltraCortex MARK IV + Tarjeta Cyton:
  
<div align = "center">
  <img src="/ISB/Imágenes - Multimedia/Multimedia - Lab5/UltraCortex - Cyton.jpg" alt="Texto alternativo" width="350" height="175">
</div>
<div align="center"> <i>Figura 2 - Conexión entre el UltraCortex MARK IV y la tarjeta Cyton</i></div>
<p>

<div align = "center">
  <img src="/ISB/Imágenes - Multimedia/Multimedia - Lab5/10-20.jpg" alt="Texto alternativo" style="width: 80%;">
</div>
<div align="center"> 
<i>Figura 3 - Sistema 10 - 20 para el posicionamiento de electrodos. En azul, se observan los 8 electrodos utilizados por el UltraCortex + Tarjeta Cyton. En rojo, se observan los 8 electrodos extra utilizando el UltraCortex + Tarjeta Cyton + Módulo Daisy.</i></div>
<p>

<div align = "center">
<img src="/ISB/Imágenes - Multimedia/Multimedia - Lab5/UltraCortex-  8 canales.jpg" alt="Texto alternativo" style="width: 50%;">
</div>
<div align="center"> <i>Figura 4 - Arreglo físico de los 8 electrodos utilizados del UltraCortex.</i></div>
<p>

<div align = "center">
<img src="/ISB/Imágenes - Multimedia/Multimedia - Lab5/UltraCortex - Conexion.jpg" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 5 - Conexión y ajuste del UltraCortex en la cabeza de la voluntaria. El gancho negro ubicado en el lóbulo de la oreja corresponde a la referencia.</i></div>
<p>

* BITalino Board + Electrodos:

<div align = "center">
<img src="/ISB/Imágenes - Multimedia/Multimedia - Lab5/Adaptador - Bitalino.png" alt="Texto alternativo" style="width: 50%;">
</div>
<div align="center"> <i>Figura 6 - Cable de conexión entre electrodos y la entrada al sensor EEG. Los terminales rojo, negro y blanco corresponden a los electrodos positivo, negativo y referencia, respectivamente.</i></div>
<p>


<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/a77bda8006294e78871e6e5e62dc82651f26490f/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/figura6.png" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 7 - Posicionamiento de los electrodos positivo y negativo en la voluntaria. </i></div>
<p>

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/a77bda8006294e78871e6e5e62dc82651f26490f/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/figura7.png" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 8 - Posicionamiento del electrodo de referencia en la voluntaria.</i></div>
<p>

### Videos de la obtención de las señales
* Reposo: Primero tomamos las señales de la voluntaria mientras se encuentra en reposo, tiene los ojos cerrados y sin moverse durante 30 segundos.

https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/a0df66e1-15c4-4b6d-bff8-e3e5eba4d935

* Ciclo de ojos: La segunda medición fue realizada mientras que la voluntaria mantenia los ojos cerrados por 5 segundos y luego los abría durante 5 segundos. Este ciclo se realizó un total de 5 veces.

https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/2027559b-710a-42a6-b76c-9dd1d9e6e19b

* Segundo Reposo: Volvemos a tomar las señales de la voluntaria mientras se encuentra en reposo, tiene los ojos cerrados y sin moverse durante 30 segundos.

https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/ccaaec57-f907-478b-91c5-de9c86da443f

* Actividad: Por último tomamos las medidas cuando la voluntaria está resolviendo una serie de problemas matemáticos simples.

https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/30704235-0047-4abd-afde-5516d22286f7

* En este video podemos observar la toma de medidas en actividad pero utilizando el Ultracortex.

https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/910e2889-25a7-42ee-a660-b6f337fbcebf



Este protocolo fue extraído de BITalino (r)evolution Home Guide EXPERIMENTAL GUIDES TO MEET & LEARN YOUR BIOSIGNALS for EEG[3]

### Gráficos en OpenBCI GUI

Algunas consideraciones que se tomaron antes de realizar el ploteo de las señales fueron las siguientes:

* La frecuencia de muestreo que se empleó fue de 250 Hz.
* Se utilizado un factor de conversión de 0.02235 (microvoltios por cuenta).

La información mencionada la encontramos en la referencia [10]:

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/22d2b0f9aab8627ac2f7eb20d71b7ac079ef85be/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/Todas_las_se%C3%B1ales.png" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 9 - Gráfico de las señales de todos los canales en el tiempo</i></div>
<p>

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/a77bda8006294e78871e6e5e62dc82651f26490f/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/Canal0.png" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 10 - FFT de la señal del Canal 0</i></div>
<p>

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/a77bda8006294e78871e6e5e62dc82651f26490f/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/Canal1.png" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 11 - FFT de la señal del Canal 1.</i></div>
<p>

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/a77bda8006294e78871e6e5e62dc82651f26490f/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/Canal5.png" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 12 - FFT de la señal del Canal 5.</i></div>
<p>

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/a77bda8006294e78871e6e5e62dc82651f26490f/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/Canal6.png" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 13 - FFT de la señal del Canal 6.</i></div>
<p>

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/a77bda8006294e78871e6e5e62dc82651f26490f/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/Canal7.png" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 14 - FFT de la señal del Canal 7.</i></div>
<p>


### Gráficos en OpenSignals
A continuacion mostraremos los graficos ploteados en Open Signals.

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/8356a06ea1b9e45714050c259e6741be9808fa0d/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/reposo1.jpeg" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 15 - Señal completa de EEG con los ojos cerrados durante 30 segundos</i></div>
<p>

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/8356a06ea1b9e45714050c259e6741be9808fa0d/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/ojos.jpeg" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 16 - Señal de EEG con los ojos abiertos</i></div>
<p>

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/8356a06ea1b9e45714050c259e6741be9808fa0d/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/reposo2.jpeg" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 17 - Señal de EEG con los ojos cerrados durante 30 segundos</i></div>
<p>

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/8356a06ea1b9e45714050c259e6741be9808fa0d/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/pensamiento%20de%205%20a%208.jpeg" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 18 - Señal de EEG de 5 a 8 segundos durante pensamiento</i></div>
<p>

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/8356a06ea1b9e45714050c259e6741be9808fa0d/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/pensamiento%20de%2015%20a%2018.jpeg" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 19 - Señal de EEG de 15 a 18 segundos durante pensamiento</i></div>
<p>

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/8356a06ea1b9e45714050c259e6741be9808fa0d/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/pensamiento%20de%2025%20a%2028.jpeg" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 20 - Señal de EEG de 25 a 28 segundos durante pensamiento</i></div>
<p>

### Gráficos en Python

Asimismo, se realizo el ploteo de las señales de OpenSignals en Python.

Para ello, es importante recordar que, la frecuencia de muestreo utilizada fue de 1000 Hz.

Por otro lado, para realizar la conversión de valor ADC a voltios, se tomo en cuenta lo siguiente:

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/9b1f382676c90c247084ccc77a31cd24955ad0fe/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/funcion.jpeg" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 21 - Señal completa de EEG sin movimientos oculares y con los ojos cerrados</i></div>
<p>

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/694f01c3327e9642220980f09f06cd02efa830ce/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/BITalino_1.png" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 22 - Señal completa de EEG sin movimientos oculares y con los ojos cerrados</i></div>
<p>

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/f508c9aadf46d4e20525921cd9de2169abdbeef9/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/BITalino_2.png" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 23 - Señal acotada de EEG (5 a 8 segundos) sin movimientos oculares y con los ojos cerrados</i></div>
<p>

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/694f01c3327e9642220980f09f06cd02efa830ce/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/BITalino_3.png" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 24 - Señal acotada de EEG (15 a 18 segundos) sin movimientos oculares y con los ojos cerrados</i></div>
<p>

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/694f01c3327e9642220980f09f06cd02efa830ce/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/BITalino_4.png" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 25 - Señal acotada de EEG (25 a 28 segundos) sin movimientos oculares y con los ojos cerrados</i></div>
<p>

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/694f01c3327e9642220980f09f06cd02efa830ce/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/BITalino_5.png" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 26 - Señal completa de EEG en un ciclo de ojos abiertos y ojos cerrados</i></div>
<p>

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/694f01c3327e9642220980f09f06cd02efa830ce/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/BITalino_6.png" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 27 - Señal acotada de EEG (5 a 8 segundos) en un ciclo de ojos abiertos y ojos cerrados</i></div>
<p>

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/694f01c3327e9642220980f09f06cd02efa830ce/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/BITalino_7.png" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 28 - Señal acotada de EEG (15 a 18 segundos) en un ciclo de ojos abiertos y ojos cerrados</i></div>
<p>

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/694f01c3327e9642220980f09f06cd02efa830ce/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/BITalino_8.png" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 29 - Señal acotada de EEG (25 a 28 segundos) en un ciclo de ojos abiertos y ojos cerrados</i></div>
<p>

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/694f01c3327e9642220980f09f06cd02efa830ce/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/BITalino_9.png" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 30 - Señal completa de EEG sin movimientos oculares y con los ojos cerrados</i></div>
<p>

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/694f01c3327e9642220980f09f06cd02efa830ce/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/BITalino_10.png" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 31 - Señal acotada de EEG (5 a 8 segundos) sin movimientos oculares y con los ojos cerrados</i></div>
<p>

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/694f01c3327e9642220980f09f06cd02efa830ce/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/BITalino_11.png" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 32 - Señal acotada de EEG (15 a 18 segundos) sin movimientos oculares y con los ojos cerrados</i></div>
<p>

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/694f01c3327e9642220980f09f06cd02efa830ce/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/BITalino_12.png" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 33 - Señal acotada de EEG (25 a 28 segundos) sin movimientos oculares y con los ojos cerrados</i></div>
<p>

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/694f01c3327e9642220980f09f06cd02efa830ce/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/BITalino_13.png" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 34 - Señal completa de EEG durante sesion de preguntas</i></div>
<p>

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/694f01c3327e9642220980f09f06cd02efa830ce/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/BITalino_14.png" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 35 - Señal acotada de EEG (5 a 8 segundos) durante sesion de preguntas</i></div>
<p>

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/694f01c3327e9642220980f09f06cd02efa830ce/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/BITalino_15.png" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 36 - Señal acotada de EEG (15 a 18 segundos) durante sesion de preguntas</i></div>
<p>

<div align = "center">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/694f01c3327e9642220980f09f06cd02efa830ce/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/BITalino_16.png" alt="Texto alternativo" style="width: 60%;">
</div>
<div align="center"> <i>Figura 37 - Señal acotada de EEG (25 a 28 segundos) durante sesion de preguntas</i></div>
<p>


### Discusión

### Bibliografia 
[1] Hahn CD, Emerson RG. Electroencephalography and evoked potentials. In: Jankovic J, Mazziotta JC, Pomeroy SL, Newman NJ, eds. Bradley and Daroff's Neurology in Clinical Practice. 8th ed. Philadelphia, PA: Elsevier; 2022:chap 35. <br>
[2] “Electroencefalografía (EEG) - Mayo Clinic,” www.mayoclinic.org. https://www.mayoclinic.org/es/tests-procedures/eeg/about/pac-20393875 <br>
[3] “BITalino (r)evolution Lab Guide.” Available: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide3_EEG.pdf <br>
[4] “EEG (Electroencephalography): The Complete Pocket Guide - iMotions,” iMotions, Aug. 27, 2019. https://imotions.com/blog/learning/best-practice/eeg/ <br>
[5] “BITalino (r)evolution Board Kit BLE/BT,” PLUX Biosignals. https://www.pluxbiosignals.com/collections/bitalino/products/bitalino-revolution-board-kit-ble-bt <br>
[6] “Ultracortex ‘Mark IV’ EEG Headset,” OpenBCI Online Store. https://shop.openbci.com/products/ultracortex-mark-iv <br>
[7] “Cyton Biosensing Board (8-channels),” OpenBCI Online Store. https://shop.openbci.com/products/cyton-biosensing-board-8-channel <br>
[8] “Cyton + Daisy Biosensing Boards (16-Channels),” OpenBCI Online Store. https://shop.openbci.com/products/cyton-daisy-biosensing-boards-16-channel <br>
[9] “Extracción de características sobre señales EEG para detección de actividades mentalmotoras en sistemas BCI”https://inaoe.repositorioinstitucional.mx/jspui/bitstream/1009/155/1/RosasChG.pdf <br>
[10] “Cyton data format”, Openbci.com. [En línea]. Disponible en: https://docs.openbci.com/Cyton/CytonDataFormat/. <br>
