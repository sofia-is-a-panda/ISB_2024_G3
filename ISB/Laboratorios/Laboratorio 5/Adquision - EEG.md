# LABORATORIO 5 – ADQUISICIÓN DE ECG CON BITALINO Y ULTRACORTEX MARK IV

## Tabla de contenidos:
* [Introducción](#introducción)
* [Objetivos](#objetivos)
* [Laboratorio](#laboratorio)
  * [Materiales y equipos](#materiales-y-equipos) 
  * [Conexiones](#conexiones)
  * [Videos de las señales](#videos-de-las-señales)
  * [Gráficos OpenBCI GUI](#gráficos-openbci-gui)
  * [Gráficos OpenSignals](#gráficos-opensignals)
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

![image](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/aee1db3c-3ddf-4f9a-82f1-b9449b4bc759)
<p align="center">Figura 1. El cerebro junto a los lóbulos que lo conforman y las funciones que cumplen. Recuperado de [3]</p>

Lóbulo Frontal:
El lóbulo frontal es la región del cerebro donde se originan la mayoría de nuestros pensamientos conscientes y decisiones. 
&nbsp;
Lóbulo Parietal:
El lóbulo parietal se enfoca en integrar información procedente de fuentes externas, así como retroalimentación sensorial interna de los músculos esqueléticos, extremidades, cabeza, ojos, otoconias, etc. 
&nbsp;
Lóbulo Occipital:
El lóbulo occipital es la región del cerebro responsable del procesamiento visual, abarcando desde la elaboración de información visual básica como la orientación y la frecuencia espacial, hasta la diferenciación de colores y la percepción del movimiento. 
&nbsp;
Lóbulo Temporal:
Finalmente, el lóbulo temporal está asociado con el procesamiento de la entrada sensorial para derivar significados superiores utilizando memorias visuales, lenguaje y asociación emocional, y está involucrado en la comprensión del lenguaje escrito y hablado [4].


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

* Board Kit Bitalino:
El Kit de tarjeta (R)Evolution BITalino consta de una tarjeta all-in-one de obtención de bioseñales que incluye principalmente 1 sensor de EEG, 1 sensor de EKG, 1 sensor de EMG, 1 microcontrolador, 1 módulo Bluetooth, entre otras cosas como actuadores y conversores. Esta tarjeta permite capturar las bioseñales a una frecuencia de sampleo máxima de 1000 Hz a una resolución de 10 bits en los canales de sensado de EEG, EKG, EMG y EDA.
Para más especificaciones, visitar la página de compra del Kit: https://www.pluxbiosignals.com/collections/bitalino/products/bitalino-revolution-board-kit-ble-bt
&nbsp;

* UltraCortex MARK IV:
El UltraCortex MARK IV es un arreglo de 35 electrodos desarrollado por la plataforma OpenBCI y orientado a la obtención de electroencefalograma basado en el sistema 10-20 para el posicionamiento de electrodos. En esta oportunidad, solo se utilizarán 8 electrodos dado que se cuenta únicamente con la tarjeta de biosensado Cyton de 8 canales.
Para más especificaciones, visitar la página de compra: https://shop.openbci.com/products/ultracortex-mark-iv
&nbsp;

* Tarjeta Cyton:
La tarjeta Cyton es una tarjeta de biosensado desarrollado por la plataforma OpenBCI al igual que el UltraCortex MARK IV. Esta solamente cuenta con 8 canales  de 24 bits y, si se requiere ampliar a 16 canales, es necesario utilizar el módulo Daisy de 8 canales extra. 
La tarjeta Cyton es compatible con la plataforma OpenBCI GUI y permite capturar las señales de electroencefalograma a una frecuencia de sampleo de 250 Hz en todos sus canales. Además, el kit incluye una llave electrónica para la comunicación Bluetooth entre la tarjeta y una PC o laptop.
Para más especificaciones, visitar las siguientes páginas de compra: 
Tarjeta Cyton: https://shop.openbci.com/products/cyton-biosensing-board-8-channel
Tarjeta Cyton + Módulo Daisy: https://shop.openbci.com/products/cyton-daisy-biosensing-boards-16-channel

### Metodología

* Conexiones y ajustes del UltraCortex MARK IV + Tarjeta Cyton:
-Descarga de la plataforma OpenBCI GUI.
-Alimentación de la tarjeta Cyton utilizando una batería de litio incluida en el kit de compra.
-Conexión del UltraCortex MARK IV con la tarjeta Cyton.
-Ajuste del UltraCortex en la cabeza del voluntario siguiendo el sistema 10-20 de posicionamiento de electrodos.
-Conexión de la laptop y la tarjeta Cyton a través de la llave electrónica (dongle) incluida en el kit de compra.
&nbsp;
* Conexiones y ajustes del Board Kit BITalino (R)evolution:
-Descarga de la plataforma OpenSignals.
-Alimentación de la tarjeta BITalino utilizando una batería de litio incluida en el kit de compra.
-Conexión de los 3 electrodos (Positivo, Negativo y Referencia) a la placa de sensado a través de un conector hacia el canal de sensado de EEG.
-Conectar por Bluetooth a la tarjeta BITalino con la laptop.
&nbsp;
* Obtención de señales: 
-Obtención de las señales de electroencefalograma en un estado de reposo (respiración normal, sin movimientos oculares y ojos cerrados) durante 30 segundos.
-Obtención de las señales de electroencefalograma repitiendo 5 ciclos de 10 segundos de ojos abiertos - ojos cerrados.
-Obtención de las señales en reposo durante 30 segundos nuevamente.
-Obtención de las señales en un estado de razonamiento lógico-matemático a través de preguntas leídas por un agente externo.

### Conexiones
* UltraCortex MARK IV + Tarjeta Cyton:

![Image](https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/main/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/UltraCortex%20-%20Cyton.jpg?raw=true)
<div align="center"> <i>Figura 1 - Conexión entre el UltraCortex MARK IV y la tarjeta Cyton</i></div>
<p>

![Image](https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/main/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/10-20.jpg?raw=true)
<div align="center"> <i>Figura 2 - Sistema 10 - 20 para el posicionamiento de electrodos. En azul, se observan los 8 electrodos utilizados por el UltraCortex + Tarjeta Cyton. En rojo, se observan los 8 electrodos extra utilizando el UltraCortex + Tarjeta Cyton + Módulo Daisy.</i></div>
<p>

![Image](https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/main/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/UltraCortex-%20%208%20canales.jpg?raw=true)
<div align="center"> <i>Figura 3 - Arreglo físico de los 8 electrodos utilizados del UltraCortex.</i></div>
<p>

![Image](https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/main/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/UltraCortex%20-%20Conexion.jpg?raw=true)
<div align="center"> <i>Figura 4 - Conexión y ajuste del UltraCortex en la cabeza de la voluntaria. El gancho negro ubicado en el lóbulo de la oreja corresponde a la referencia.</i></div>
<p>

* BITalino Board + Electrodos:

![Image](https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/main/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/Adaptador%20-%20Bitalino.png?raw=true)
<div align="center"> <i>Figura 5 - Cable de conexión entre electrodos y la entrada al sensor EEG. Los terminales rojo, negro y blanco corresponden a los electrodos positivo, negativo y referencia, respectivamente.</i></div>
<p>


![Image](https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/main/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/Electrodos%20-%20Conexion2.jpg?raw=true)
<div align="center"> <i>Figura 6 - Posicionamiento de los electrodos positivo y negativo en la voluntaria. </i></div>
<p>

![Image](https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/main/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab5/Electrodos%20-%20Conexion1.jpg?raw=true)

<div align="center"> <i>Figura 7 - Posicionamiento del electrodo de referencia en la voluntaria.</i></div>
<p>

### Videos de la obtención de las señales

### Gráficos en OpenBCI GUI

### Gráficos en OpenSignals

### Gráficos en Python

### Discusión

### Bibliografia 
[1] Hahn CD, Emerson RG. Electroencephalography and evoked potentials. In: Jankovic J, Mazziotta JC, Pomeroy SL, Newman NJ, eds. Bradley and Daroff's Neurology in Clinical Practice. 8th ed. Philadelphia, PA: Elsevier; 2022:chap 35.
[2] https://www.mayoclinic.org/es/tests-procedures/eeg/about/pac-20393875
[3] “BITalino (r)evolution Lab Guide.” Available: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide3_EEG.pdf
[4] “EEG (Electroencephalography): The Complete Pocket Guide - iMotions,” iMotions, Aug. 27, 2019. https://imotions.com/blog/learning/best-practice/eeg/
[5]
