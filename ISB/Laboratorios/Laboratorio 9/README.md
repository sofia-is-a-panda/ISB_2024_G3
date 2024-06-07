# LABORATORIO 9 - PROCESAMIENTO DE ECG
## TABLA DE CONTENIDO

* [Introducción](#introducción)
* [Objetivos](#objetivos)
* [Filtros](#filtrado)
* [Extracción de características](#extracción-de-características)
* [Discusión](#discusión)
* [Bibliografía](#bibliografía)

## Introducción

## Objetivos

## Filtrado

Antes de extraer las características del ECG, se vio conveniente realizar el filtrado correspondiente de la señal.
A continuación, mostramos una breve comparativa entre las señales filtradas, usando el filtro Wavelet del [laboratorio 7](lhttps://github.com/sofia-is-a-panda/ISB_2024_G3/tree/main/ISB/Laboratorios/Laboratorio%207), y sin filtrar.
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
        <td><img src="/ISB/Imágenes - Multimedia/Multimedia_Lab9/filtro_respiracion.png"></td>
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
    <div>Figura 1. Gráfico de diferencia entre picos R</div>
</div>

### Valores de RMSSD

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

## Discusión

## Bibliografía
