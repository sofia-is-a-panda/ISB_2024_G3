# LABORATORIO 8 - PROCESAMIENTO DE EMG
## TABLA DE CONTENIDO

* [Introducción](#introducción)
* [Objetivos](#objetivos)
* [Filtros](#filtrado)
* [Extracción de características](#extracción-de-características)
* [Discusión](#discusión)
* [Bibliografía](#bibliografía)

## Introducción
Anteriormente, se utilizaron 3 tipos distintos distintos de filtros para conseguir una señal más limpia del electromiograma, estas fueron filtros FIR, IIR y tipo Wavelet. Sin embargo, estos filtros presentan ventajas y desventajas como por ejemplo el gran tamaño computacional para realizar filtros FIR de gran orden y la escasa lineariedad de la fase en el caso de los filtros IIR [1]; por lo que es necesario realizar una comparación, utilizando la señal EMG capturada anteriormente, para establecer, mediante el Signal-Noise Ratio (SNR) el cual es un valor altamente significativo en la comparación entre entre el ruido y la señal [2], cuál es la mejor opción para utilizar frente a este tipo de señales.

<p align="center" style="margin-bottom:0">
<img src="/ISB/Imágenes - Multimedia/Multimedia - Lab 8/SNR.png" align="center"/>
<div align="center"> <i>Fig. 1. Razón Ruido-Señal (SNR por sus siglas en inglés) [2] </i></div>
</p>


Una vez establecido el tipo de filtro más adecuado y habiendo filtrado la señal correspondiente, finalmente se puede realizar la extracción de características más importantes de la señal, entre las cuales podemos encontrar los valores Root Mean Square, Mean Absolute Value, Kurtosis, Zero Crossing, etc [3].
## Objetivos
* Comparar los filtros FIR, IIR y Wavelet en el caso de EMG.
* Extraer características de la señal EMG adquirida en el laboratorio

## Filtrado de las senales:

#### Reposo
En este caso, no consideraremos la extracción de parámetros para esta señal, ya que al estar en reposo no debería ocurrir ningún evento que defina valores para los parámetro que deseamos calcular.
<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/5bd77fbb06dd660484f1389c28c29380f8e35a1e/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab_8/reposo_filtro.png" align="center"/>
<div align="center"> <i>Fig. 2. Señal en reposo luego de aplicar el filtro Wavelet </i></div>
</p>

#### Tensión
<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/5bd77fbb06dd660484f1389c28c29380f8e35a1e/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab_8/tension_filtrado.png" align="center"/>
<div align="center"> <i>Fig. 3. Senal en tensión luego de aplicar el filtro Wavelet </i></div>
</p>

### Oposición
<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/5bd77fbb06dd660484f1389c28c29380f8e35a1e/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab_8/oposicion_filtrado.png" align="center"/>
<div align="center"> <i>Fig. 4. Senal en oposición luego de aplicar el filtro Wavelet </i></div>
</p>


### Filtros IIR y FIR

#### Reposo
<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/365ba95fd4c1e5236c147ba0bc043ae0dbf4de09/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab%206/Se%C3%B1alReposo.png" align="center"/>
<div align="center"> <i>Fig. 5. Comparacion de senal en reposo luego de aplicar filtros IIR y FIR </i></div>
</p>

#### Tension 
<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/365ba95fd4c1e5236c147ba0bc043ae0dbf4de09/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab%206/Se%C3%B1alTensi%C3%B3n.png" align="center"/>
<div align="center"> <i>Fig. 6. Comparacion de senal en tension luego de aplicar filtros IIR y FIR </i></div>
</p>

#### Oposicion
<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/365ba95fd4c1e5236c147ba0bc043ae0dbf4de09/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab%206/Se%C3%B1alOposici%C3%B3n.png" align="center"/>
<div align="center"> <i>Fig. 7. Comparacion de senal en oposicion luego de aplicar filtros IIR y FIR </i></div>
</p>

Luego de haber filtrado las senales, calculamos el SNR (Signal Noise Ratio) de las mismas a través de la adquisición del componente de ruido a través de la sustracción de la señal filtrada de la señal original en los 3 casos.

Asimismo, obtuvimos los siguientes valores de SNR para los filtros utilizados:

### Usando filtro Wavelet

* SNR Senal en Reposo filtrada: 1.64 dB
* SNR Senal en Tension fitlrada : 3.82 dB
* SNR Senal en Oposicion filtrada : 2.15 dB

### Usando filtro IIR

* SNR Senal en Reposo filtrada: 11.14 dB
* SNR Senal en Tension fitlrada : 5.46 dB
* SNR Senal en Oposicion filtrada : 6.89 dB

### Usando filtro FIR

* SNR Senal en Reposo filtrada: -1.44 dB
* SNR Senal en Tension fitlrada : -2.88 dB
* SNR Senal en Oposicion filtrada : -3.06 dB

## Extracción de características:
Tras el filtrado, se procedió a la extracción de las características de la señal filtrada.

<table>
        <tr>
            <th>Parameter</th>
            <th>Senal EMG en Reposo</th>
            <th>Senal EMG en Tension</th>
            <th>Senal EMG en Oposicion</th>
        </tr>
        <tr>
            <td>Number of Muscular Activations</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Maximum Muscular Activation Duration</td>
            <td>6.049</td>
            <td>4.917</td>
            <td>9.453</td>
        </tr>
        <tr>
            <td>Minimum Muscular Activation Duration</td>
            <td>6.049</td>
            <td>4.917</td>
            <td>9.453</td>
        </tr>
        <tr>
            <td>Average Muscular Activation Duration</td>
            <td>6.049</td>
            <td>4.917</td>
            <td>9.453</td>
        </tr>
        <tr>
            <td>Standard Deviation of Muscular Activation Duration</td>
            <td>0.0</td>
            <td>0.0</td>
            <td>0.0</td>
        </tr>
        <tr>
            <td>Maximum Sample Value</td>
            <td>0.044</td>
            <td>0.702</td>
            <td>1.331</td>
        </tr>
        <tr>
            <td>Minimum Sample Value</td>
            <td>-0.057</td>
            <td>-0.635</td>
            <td>-1.255</td>
        </tr>
        <tr>
            <td>Average Sample Value</td>
            <td>-0.016</td>
            <td>-0.016</td>
            <td>-0.016</td>
        </tr>
        <tr>
            <td>Standard Deviation Sample Value</td>
            <td>0.026</td>
            <td>0.090</td>
            <td>0.186</td>
        </tr>
        <tr>
            <td>RMS</td>
            <td>0.031</td>
            <td>0.092</td>
            <td>0.186</td>
        </tr>
        <tr>
            <td>Area</td>
            <td>-106.884</td>
            <td>-141.796</td>
            <td>-242.323</td>
        </tr>
        <tr>
            <td>Total Power Spect</td>
            <td>0.00070</td>
            <td>0.00835</td>
            <td>0.03316</td>
        </tr>
        <tr>
            <td>Median Frequency</td>
            <td>62.5</td>
            <td>25</td>
            <td>117.1875</td>
        </tr>
        <tr>
            <td>Maximum Power Frequency</td>
            <td>58.5938</td>
            <td>109.375</td>
            <td>113.2813</td>
        </tr>
    </table>

## Discusión

Wavelet SNR Post-filtrado: 
Un SNR de 1.32 dB post-filtrado sugiere que hay una mejora en la relación señal/ruido después de aplicar el filtro, pero esta mejora aún sigue siendo limitada. En términos prácticos, esto significa que el filtrado ha reducido algo de ruido, pero no de manera significativa. <br>

Posibles efectos adversos: <br>
Parámetros del Filtro: Los parámetros del filtro (umbral de wavelet, selección de IMFs) pueden no estar optimizados.
Método de Filtrado: El método de filtrado utilizado (EEMD y wavelet denoising) puede no ser el más adecuado para el tipo de ruido presente en la señal. <br>
Calidad de la señal original: Si la señal original tiene un nivel de ruido extremadamente alto, puede ser necesario un filtrado más agresivo o una combinación de varios métodos de filtrado. <br>
Recomendaciones: <br>
Wavelet Denoising: Experimenta con diferentes niveles de descomposición y umbrales. Un umbral más alto puede eliminar más ruido pero también puede afectar la señal útil. <br>
Selección de IMFs: Revisa el umbral utilizado para seleccionar los IMFs. Puede que necesites un umbral diferente para distinguir mejor entre IMFs ruidosos y aquellos que contienen la señal útil. <br>

## Bibliografía
[1] R. Pal, “Comparison of the design of FIR and IIR filters for a given specification and removal of phase distortion from IIR filters,” 2017 International Conference on Advances in Computing, Communication and Control (ICAC3). IEEE, Dec. 2017. doi: 10.1109/icac3.2017.8318772. <br>

[2] É. Thibault, F. L. Désilets, B. Poulin, M. Chioua, and P. Stuart, “Comparison of signal processing methods considering their optimal parameters using synthetic signals in a heat exchanger network simulation,” Computers &amp; Chemical Engineering, vol. 178. Elsevier BV, p. 108380, Oct. 2023. doi: 10.1016/j.compchemeng.2023.108380. <br>

[3] T. Oo and P. Phukpattaranont, “Signal-to-Noise Ratio Estimation in Electromyography Signals Contaminated with Electrocardiography Signals,” Fluctuation and Noise Letters, vol. 19, no. 03. World Scientific Pub Co Pte Lt, p. 2050027, Feb. 17, 2020. doi: 10.1142/s0219477520500273.