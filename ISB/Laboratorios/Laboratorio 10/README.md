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
Asimismo, se hizo uso de la librería MNE.
Para el filtrado de la señal, se hizo uso de un filtropasabanda con una frecuencia inferior de 0.48 Hz y una frecuencia superior de 30 Hz.

Una vez realizado el filtrado, obtuvimos ambas gráficas, tanto para el sujeto que escuchaba música nativa, como aquel que escuchaba música no nativa.



<div><img "src"=></div>
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

Se hizo uso de la libreria MNE. A continuacion, mostraremos los resultados obtenidos con la herramienta mencionada anteriormente.

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

Para la extracción de características, utilizamos una DWT para este propósito, tomando como base el procedimiento realizado en el artículo "". Las características que se analizaron en el mismo incluyen: 
* Varianza
* SD (Desviacion Estandar)
* Kurtosis
* Entropía
* LBP (Local Binary Pattern)

Primero, mostramos las caracterististicas de EEG del sujeto que fue sometido el experimento 5 (escuchar música en idioma nativo).
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


Además, también se muestran las características de EEG de la señal de aquel sujeto realizando el experimento 6 (eschuchar música no nativa) 

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

## Bibliografía
[1]
[2]
[3]