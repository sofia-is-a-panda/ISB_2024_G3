# LABORATORIO 10 - PROCESAMIENTO DE EEG
## TABLA DE CONTENIDO

* [Introducción](#introducción)
* [Objetivos](#objetivos)
* [Filtrado](#filtrado)
* [Discusión](#discusión)
* [Bibliografía](#bibliografía)

## Introducción

## Objetivos

* Extraer características de señales EEG

## Base de datos escogida

La señales que se emplearon fueron obtenidas de la siguiente base de datos ["Auditory evoked potential EEG-Biometric dataset"](https://physionet.org/content/auditory-eeg/1.0.0/#files-panel) la cual es el libre acceso via Physionet. 
Consiste de 240 señales de EEG de dos minutos de duración que fueron obtenidas de 20 voluntarios. La toma de la señal siguió los siguientes pasos:

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

Dado que se tiene la información para los 10 experimentos para cada persona, resultó de interés el analizar la actividad cerebral en las actividades 5 (escuchar canción en idioma nativo) y 6 (escuchar canción en idioma no nativo)

Adicionalmente, se presenta información para cuatro canales, la frecuencia de muestreo fue de 200Hz.

## Filtrado de la Señal

Para el filtrado de la señal, se hizo uso de un filtropasabanda con una frecuencia inferior de 0.48 Hz y una frecuencia superior de 30 Hz.

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

## Extracción de Características

Para la extracción de las características, se hizo uso de un filtro Wavelet (db4).





## Discusión

## Bibliografía
