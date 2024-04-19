# LABORATORIO 4 – USO DE BITALINO PARA ADQUISICIÓN DE ECG

## Tabla de contenidos:
* [Introducción](#introducción)
* [Objetivos](#objetivos)
* [Laboratorio](#laboratorio)
  * [Materiales y equipos](#materiales-y-equipos) 
  * [Conexiones](#conexiones)
  * [Metodología](#metodología)
  * [Video de señal](#video-de-señal)
  * [Gráficos OpenSignals](#gráficos-opensignals)
  * [Discusión](#discusión)
  * [Archivos](#archivos)
  * [Gráficos en Python](#gráficos-en-python)
* [Bibliografía](#bibliografía)


## Introducción

### ¿Qué es un ECG?
Un electrocardiograma (ECG) es una prueba común que registra la actividad eléctrica del corazón. Es una herramienta valiosa para diagnosticar una variedad de enfermedades cardíacas. [1]

### ¿Cómo funciona un ECG?

El corazón genera pequeñas señales eléctricas cada vez que late. Un ECG mide estas señales usando electrodos colocados en la piel del pecho y las extremidades. Las señales se amplifican y registran en un papel o en una pantalla de computadora. [1]

### ¿Qué muestra un ECG?

Un ECG normal muestra una onda característica en forma de "V". Esta onda se compone de varias partes, cada una de las cuales representa una parte diferente del ciclo cardíaco. [2]


<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/b9b58d7f882522677eb139213e377c75eb6078a7/ISB/imagenes_multimedia/Multimedia-Lab4/ecg.png"/>
<div align="center"> <i>Figura 1: Ondas y picos de un ECG normal [2]</i></div>
<p>


* La onda P representa la despolarización de las aurículas, las cámaras superiores del corazón. [2]
* El complejo QRS representa la despolarización de los ventrículos, las cámaras inferiores del corazón. [2]
* La onda T representa la repolarización de los ventrículos. [2]

### BITalino
Como mencionamos anteriormente utilizaremos BITalino, que es una plataforma de hardware y software de bajo costo y código abierto que permite la adquisición de señales biomédicas, incluyendo ECG. La plataforma BITalino está compuesta por una placa de desarrollo, varios sensores y un software de adquisición y análisis de datos. La placa de desarrollo cuenta con un microcontrolador, conectividad Bluetooth y varios canales analógicos y digitales que permiten conectar una variedad de sensores. Los sensores BITalino incluyen sensores de ECG, EMG, EEG, acelerometría, fotopletismografía (PPG), temperatura, respiración y actividad electrodermal. El software de adquisición y análisis de datos permite visualizar las señales en tiempo real, guardar los datos para su posterior análisis y exportar los datos a diferentes formatos [3]. 

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/a00509f2813c3d4ebdd4ee62013c09907bc469c5/ISB/imagenes_multimedia/Multimedia-Lab4/bitalino%20kit.jpeg" align="center" width="500" height="300"/>
<div align="center"> <i>Figura 2: Kit BITalino</i></div>
<p>
  
## Objetivos
En el presente laboratorio, utilizaremos la plataforma BITalino para adquirir señales de ECG utilizando el procedimiento indicado en BITalino (r)evolution Home Guide EXPERIMENTAL GUIDES TO MEET & LEARN YOUR BIOSIGNALS for ECG [4]. Las señales de ECG serán visualizadas en tiempo real utilizando el software OpenSignals y guardaremos la información de las señales obtenidas para poder plotearlas en Python.

* Adquirir e interpretar señales biomédicas de electrocardiograma (ECG) en reposo, aguantando la respiración y después de realizar actividad física.
* Realizar la configuración del BiTalino de manera adecuada para garantizar mediciones fiables.
* Utilizar eficientemente el software OpenSignals 
* Plotear las señales utilizando Python ara analizar y extraer datos relevantes de las señales ECG, lo que contribuirá a una comprensión más profunda de los patrones y comportamientos cardíacos.

## Laboratorio

### Materiales y equipos
<div align="center">

|  **Modelo**  | **Descripción** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| (R)EVOLUTION |   Kit BITalino  |       1      |
|       -      |      Laptop     |       1      |


<div align="left">
  
### Conexiones
Se utilizo el cable de 3 hilos con sus respectivos electrodos. Cada uno de estso electrodos representa positivo (rojo), tierra (negro) y referencia (blanco). Para realizar las conexiones nos basamos en el protocolo BITalino (r)evolution Home Guide EXPERIMENTAL GUIDES TO MEET & LEARN YOUR BIOSIGNALS for ECG [4].

Para iniciar colocamos el electrodo positivo (color rojo) en el brazo izquierdo (LA), el electrodo de tierra (color negro) en el brazo derecho (RA) y el electrodo de referencia (color blanco) en la cresta ilíaca. Así como observamos en la Figura 3.

## Resultados

## Discusión

## Bibliografía
[1] American Heart Association [Internet]. Dallas (TX): American Heart Association Inc.; c2022. Electrocardiogram (ECG or EKG); [Consultado: 19-abr-2024]. Available from: http://www.heart.org/en/health-topics/heart-attack/diagnosing-a-heart-attack/electrocardiogram-ecg-or-ekg

[2] Cleveland Clinic: Health Library: Diagnostics & Testing [Internet]. Cleveland (OH): Cleveland Clinic; c2022. Electrocardiogram (EKG); [Consultado: 19-abr-2024]. Available from: https://my.clevelandclinic.org/health/diagnostics/16953-electrocardiogram-ekg

[3] “BITalino Lab Guides (Home Guides) – Support PLUX Biosignals official,” support.pluxbiosignals.com. https://support.pluxbiosignals.com/knowledge-base/bitalino-lab-guides/. [Accessed: 19-Apr-2024].

[4] “BITalino Lab Guides (Home Guides) – Support PLUX Biosignals official,” support.pluxbiosignals.com. https://support.pluxbiosignals.com/knowledge-base/bitalino-lab-guides/ [Accessed: 19-Apr-2024].

