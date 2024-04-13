
# LABORATORIO 3 – USO DE BITALINO PARA ADQUISICIÓN DE EMG

## CONTENIDO
* [Objetivos](#objetivos)
* [Introducción](#introducción)
* [Materiales](#materiales)
* [Laboratorio3](#laboratorio3)
  * [Conexiones](#conexiones)
  * [Videos de la señal](#videos-de-señal)
  * [Gráficos OpenSignals](#gráficos-opensignals)
  * [Discusión](#discusión)
  * [Ploteo en Python](#ploteo-en-python)
* [Bibliografía](#bibliografía)


## OBJETIVOS
* Adquirir de manera correcta una señal de EMG
* Realizar una correcta configuración del BITalino
* Extraer la información de las señal del EMG mediante el software OpenSignals (r)evolution 
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
        Electrodo desechable
        </th>
        <th>
            <div align="center">3</div>  
        </th>
    </tr>
</table>
En la sesión de laboratorio se hizo uso del kit BITalino (r)evolution (Figura 1). Dentro del mismo se encuentra el board del BITalino, 1 cable de 3 hilos, 1 cable de 2 hilos, 5 electrodos, 1 bateria de polimero de litio de 500 maH y  la guia de usuario.

<p align="center" style="margin-bottom:0">
<img src="Multimedia/kit_bitalino.jpeg" width="400" height="250"/>
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

Después de posicionar los electrodos, se estableció la conexión Bluetooth entre el BiTalino y OpenSignals para visualizar la señal deseada. Se llevaron a cabo dos pruebas: una con el músculo en reposo y otra aplicando fuerza. La variación en la fuerza aplicada al músculo se reflejará en el gráfico de la señal de OpenSignals de la siguiente forma:

## VIDEOS DE LA SEÑAL
poner videos

## PLOTEO EN OPEN SIGNALS

<img src="multimedia/ploteo_OS_reposo.jpeg"><img>

<img src="multimedia/ploteo_OS_tension.jpeg"><img>

<img src="multimedia/ploteo_OS_oposicion.jpeg"><img>


## PLOTEO EN PYTHON








