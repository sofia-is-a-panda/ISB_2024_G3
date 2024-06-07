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

Antes de extraer las características del ECG, vimos conveniente realizar el filtrado correspondiente de la señal.
A continuacion, mostramos una breve comparativa entre las senales filtradas y sin filtrar.
<table>
    <tr>
        <th>Estado del sujeto</th>
        <th>Senal</th>
    </tr>
    <tr>
        <th>REPOSO</th>
        <td><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/d894851771a7567fd40d6ceb55f7eb9100b73bcf/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab9/filtro_reposo.png"></td>
    </tr>
    <tr>
        <th>RESPIRACION</th>
        <td><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/d894851771a7567fd40d6ceb55f7eb9100b73bcf/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab9/filtro_respiracion.png"></td>
    </tr>
    <tr>
        <th>EJERCICIO</th>
        <td><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/d894851771a7567fd40d6ceb55f7eb9100b73bcf/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab9/filtro_ejercicio.png"></td>
    </tr>

</table>

## HRV - Heart Rate Variability


### UBICACION DE PICO R-R

<table>
    <tr>
        <th>Estado del sujeto</th>
        <th>Estado de la senal</th>
        <th>Ploteo de la senal</th>
    </tr>
    <tr>
        <td rowspan="2">REPOSO</td>
        <td>SIN FILTRAR</td>
        <td><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/d894851771a7567fd40d6ceb55f7eb9100b73bcf/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab9/picos_nofilter_reposo.png"></td>
    </tr>
    <tr>
        <td>FILTRADA</td>
        <td><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/d894851771a7567fd40d6ceb55f7eb9100b73bcf/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab9/picos_filter_reposo.png"></td>
    </tr>
    <tr>
        <td rowspan="2">RESPIRACION</td>
        <td>SIN FILTRAR</td>
        <td><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/d894851771a7567fd40d6ceb55f7eb9100b73bcf/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab9/picos_nofilter_respiracion.png"></td>
    </tr>
    <tr>
        <td>FILTRADA</td>
        <td><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/d894851771a7567fd40d6ceb55f7eb9100b73bcf/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab9/picos_filter_respiracion.png"></td>
    </tr>
    <tr>
        <td rowspan="2">EJERCICIO</td>
        <td>SIN FILTRAR</td>
         <td><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/d894851771a7567fd40d6ceb55f7eb9100b73bcf/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab9/picos_nofilter_ejercicio.png"></td>       
    </tr>
    <tr>
        <td>FILTRADA</td>
        <td><img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/d894851771a7567fd40d6ceb55f7eb9100b73bcf/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab9/picos_filter_ejercicio.png"></td>
    </tr>
</table>

### COMPARACION DE LAS DIFERENCIAS ENTRE PICOS R

<div align="center">
    <img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/749bac511724ddc1c06244b4be181948bb9360b7/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia_Lab9/picos_R_diff.png">
    <div>Figura 1. Grafico de diferencia entre picos R</div>
</div>

### VALORES DE RMSSD

<table>
    <tr>
        <th>ESTADO DEL SUJETO</th>
        <th>VALOR DE RMSSD</th>
    </tr>
    <tr>
        <th>REPOSO</th>
        <td>48.42</td> 
    </tr>
    <tr>
        <th>RESPIRACION</th>
        <td>30.65</td>
    </tr>
    <tr>
        <th>EJERCICIO</th>
        <td>13.79</td>
    </tr>
</table>

## Discusión

## Bibliografía
