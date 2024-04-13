
# LABORATORIO 3 – USO DE BITALINO PARA ADQUISICIÓN DE EMG

## CONTENIDO
* [Objetivos](#objetivos)
* [Introducción](#introducción)
* [Materiales](#materiales)
* [Laboratorio3](#laboratorio3)
  * [Conexiones](#conexiones)
  * [Videos de la señal](#videos-de-señal)
  * [Gráficos OpenSignals](#gráficos-opensignals)
  * [Ploteo en Python](#ploteo-en-python)
  * [Discusión](#discusión)
* [Bibliografía](#bibliografía)


## OBJETIVOS
* Adquirir correctamente una señal de EMG.
* Realizar una correcta configuración del BITalino
* Extraer la información de las señal del EMG mediante el software OpenSignals (r)evolution. 
## INTRODUCCIÓN 
En este laboratorio, utilizaremos la plataforma BITalino para adquirir señales de EMG utilizando el procedimiento para el estudio de conducción nerviosa motora del
nervio mediano del MINSA [1]. Las señales de EMG serán visualizadas en tiempo real utilizando el software OpenSignals y guardaremos la información de las señales obtenidas para poder plotearlas en Python.

## MATERIALES
<table border=1px>
    <tr>
        <th>
            <div align="center">MATERIAL</div>
        </th>
        <th>
            <div align="center">CANTIDAD</div>
        </th>
    </tr>
    <tr>
        <th>
             Kit BITalino
        </th>
        <th>
            <div align="center">1</div>      
        </th> 
    </tr>
    <tr>
        <th>
             Laptop
        </th>
        <th>
            <div align="center">1</div>  
        </th> 
    </tr>
    <tr>
        <th>
        Electrodos desechables
        </th>
        <th>
            <div align="center">3</div>  
        </th>
    </tr>
</table>
En la sesión de laboratorio, se hizo uso del kit BITalino (r)evolution (Figura 1). Dentro del mismo se encuentra el board del BITalino, 1 cable de 3 hilos, 1 cable de 2 hilos, 5 electrodos, 1 bateria de polímero de litio de 500 mAh y una breve guía de usuario.

&nbsp;
<p align="center" style="margin-bottom:0">
<img src="Multimedia/kit_bitalino.jpeg" width="400" height="500"/>
<div align="center"> <i>Figura 1. Kit Bitalino</i></div>
<p>



## LABORATORIO
Como mencionamos anteriormente utilizaremos BITalino, que es una plataforma de hardware y software de bajo costo y código abierto que permite la adquisición de señales biomédicas, incluyendo EMG. La plataforma BITalino está compuesta por una placa de desarrollo, varios sensores y un software de adquisición y análisis de datos. La placa de desarrollo cuenta con un microcontrolador, conectividad Bluetooth y varios canales analógicos y digitales que permiten conectar una variedad de sensores. Los sensores BITalino incluyen sensores de ECG, EMG, EEG, acelerometría, fotopletismografía (PPG), temperatura, respiración y actividad electrodermal. El software de adquisición y análisis de datos permite visualizar las señales en tiempo real, guardar los datos para su posterior análisis y exportar los datos a diferentes formatos [2]. 

### Conexiones
Se utilizo el cable de 3 hilos con sus respectivos electrodos. Cada uno de estso electrodos representa positivo (rojo), tierra (negro) y referencia (blanco). Para realizar las conexiones nos basamos en el protocolo del MINSA  "DE ELECTROMIOGRAFÍA Y VELOCIDAD DE CONDUCCIÓN DE NERVIOS PERIFÉRICOS". En este caso, utilizamos especificamente la técnica del estudio de conducción nerviosa motora del nervio mediano [1].

Para iniciar colocamos el electrodo positivo (G1) sobre el centro del músculo abductor corto del pulgar y el electrodo de referencia (G2) eN la articulación metacarpo falángico del primer dedo. Así como observamos en la Figura 2. 
<p align="center" style="margin-bottom:0">
<img src="Multimedia/posicion2.jpeg" width="250" height="400"/>
<div align="center"> <i>Figura 2: Posición del electrodo positivo y de referencia.</i></div>
<p>

 Finalmente, colocamos el electrodo de tierra en el dorso de la mano, como observamos en la Figura 3.
<p align="center" style="margin-bottom:0">
<img src="Multimedia/posicion1.jpeg" width="250" height="400"/>
<div align="center"> <i>Figura 3:Posición del electro de tierra.</i></div>
<p>

Después de posicionar los electrodos, se estableció la conexión Bluetooth entre el BiTalino y OpenSignals para visualizar la señal deseada. Se llevaron a cabo 3 pruebas: Una con el músculo en reposo, otra tensionando el músculo sin oposición externa y la última tensionando el músculo con oposición externa.

### VIDEOS DE LA SEÑAL
En los próximos videos se exhiben las conexiones entre los electrodos y el cuerpo, así como la visualización de la señal en OpenSignals.

<div align="center">
<p align="justify">Video de la toma de señal del músculo en reposo:</p>
 https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/245eb187-d307-48d9-b9f2-d8b08d0ef189
</div>

<div align="center">
<p align="justify">Video de la toma de señal del músculo en tensión:</p>
https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/8904b899-1dba-4b86-8b5a-1ba2ec50f83e
</div>

<div align="center">
<p align="justify">Video de la toma de señal del músculo en oposición:</p>
https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/83306ae2-ede3-4c62-a038-f5998ad6f474
</div>

## GRÁFICOS OpenSignals
### Señal en reposo:
Podemos ver que observamos un poco de ruido cuando el músculo se encuentra en reposo que es debido a la mala colocación del electrodo de referencia.

<p align="center">
<img src="Multimedia\ploteo_OS_reposo.jpeg" align="center" width="500" height="300"/>
<div align="center"> <i>Figura 4: Gráfica en OpenSignals músculo en reposo.</i></div>
<p>
</p>

Señal en tensión:
Cuando el músculo empieza a hacer un poco de tensión, empezamos a notar señales.

<p align="center">
<img src="Multimedia\ploteo_OS_tension.jpeg" align="center" width="500" height="300"/>
<div align="center"> <i>Figura 5: Gráfica en OpenSignals músculo en tensión</i></div>
<p>
</p>

Señal en oposición:
Cuando el músculo se enfrenta a una oposición, en este caso una fuerza externa aplicada por un compañero, empezamos a notar señales más pronunciadas.

<p align="center">
<img src="Multimedia\ploteo_OS_oposicion.jpeg" align="center" width="500" height="300"/>
<div align="center"> <i>Figura 6: Gráfica en OpenSignals músculo en oposición</i></div>
<p>
</p>

### PLOTEO EN PYTHON
Las señales obtenidas en la sesión fueron recuperadas y procesadas en Python de 1 alumno, del cual se realizó 
* Lectura en reposo
* Lectura durante la tensión
* Lectura durante oposición

| Lectura en reposo | Lectura durante la tensión | Lectura durante oposición |
| :---      |   :---:  |   :---:  | 
|![emg_reposo](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/23c4744c-6a88-4d14-ab0b-93058803fe03) | ![emg_tension](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/11ae7671-05e1-4ac6-a21c-f4294123e23c) | ![emg_oposicion](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/c4b56ebe-0bcc-49d4-89bd-8cb78bc723b6) |
| :---      |   :---:  |   :---:  | 
|![fft_reposo](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/a1cb8c2f-8eb8-48ba-a0ee-3e46efd19f1e) | ![fft_tension](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/164d4aa8-cdf9-4cac-98dd-e75262fe4631) | ![fft_oposicion](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/b91bae71-5999-4fa7-8810-b2e850cc40a1) |



### DISCUSIÓN
Se llevó a cabo la captura de las señales eléctricas del músculo abductor corto del pulgar, como se mostró en las imágenes. Dado que se utilizaron electrodos superficiales, existe la posibilidad de que se hayan registrado diversos ruidos externos o señales ajenas al segmento mencionado, aunque para evitar dichos ruidos al momento de tomar las mediciones retiramos todos los aparatos electronicos y joyas de la voluntaria. A partir de este punto, se realizaron tres movimientos. El primero fue de relajación, en el cual las señales exhibieron una variación mínima, casi similar al silencio, como se puede observar en la imagen donde la señal permanece cerca de su centro, mostrando una baja amplitud que, a gran escala, parece casi una línea.

Posteriormente, se procedió a inducir una tensión prolongada del músculo mediante un arqueo del falange, manteniendo la contracción por unos segundos. Y por último, se realizó un movimiento de oposición, en el cual pudimos detectar señales de mayor amplitud.

## BIBLIOGRAFÍA
[1] MINSA, GUÍA DE PROCEDIMIENTO DE ELECTROMIOGRAFÍA Y VELOCIDAD DE CONDUCCIÓN DE NERVIOS PERIFÉRICOS UNIDAD DE ATENCIÓN INTEGRAL ESPECIALIZADA
SUB UNIDAD DE ATENCION INTEGRAL ESPECIALIZADA PEDIÁTRICA Y SUB ESPECIALIDADES NEUROLOGIA PEDIATRICA. Disponible en: https://www.insnsb.gob.pe/docs-trans/resoluciones/archivopdf.php?pdf=2020/RD%20N%C2%B0%20000226-2020-DG-INSNSB%20Gu%C3%ADa%20Proced%20Electromiograf%C3%ADa_2020%203REV%20UGC%20CHN%2019.06.2020.pdf

[2] “BITalino Lab Guides (Home Guides) – Support PLUX Biosignals official,” support.pluxbiosignals.com. https://support.pluxbiosignals.com/knowledge-base/bitalino-lab-guides/


