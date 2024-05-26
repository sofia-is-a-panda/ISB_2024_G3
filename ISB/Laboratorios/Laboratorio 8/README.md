# LABORATORIO 8 - PROCESAMIENTO DE EMG
## TABLA DE CONTENIDO

* [Introducción](#introducción)
* [Objetivos](#objetivos)
* [Filtros](#filtrado)
* [Extracción de características](#extracción-de-características)
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

## Filtros:

### Reposo
En este caso, no consideraremos la extracción de parámetros para esta señal, ya que al estar en reposo no debería ocurrir ningún evento que defina valores para los parámetro que deseamos calcular.
<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/5bd77fbb06dd660484f1389c28c29380f8e35a1e/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab_8/reposo_filtro.png" align="center"/>
<div align="center"> <i>Fig. 2. Señal en reposo luego de aplicar el filtro Wavelet </i></div>
</p>

### Tensión
<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/5bd77fbb06dd660484f1389c28c29380f8e35a1e/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab_8/tension_filtrado.png" align="center"/>
<div align="center"> <i>Fig. 3. Senal en tensión luego de aplicar el filtro Wavelet </i></div>
</p>


### Oposición
<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/5bd77fbb06dd660484f1389c28c29380f8e35a1e/ISB/Im%C3%A1genes%20-%20Multimedia/Multimedia%20-%20Lab_8/oposicion_filtrado.png" align="center"/>
<div align="center"> <i>Fig. 4. Senal en oposición luego de aplicar el filtro Wavelet </i></div>
</p>

Luego de haber filtrado las senales, calculamos el SNR (Signal Noise Ratio) de las mismas a través de la adquisición del componente de ruido a través de la sustracción de la señal filtrada de la señal original en los 3 casos.

Con ello obtuvimos los siguientes valores:

* SNR Senal en Reposo filtrada: 1.64 dB
* SNR Senal en Tension fitlrada : 3.82 dB
* SNR Senal en Oposicion filtrada : 2.15 dB


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
            <td>6.0499379748798265</td>
            <td>4.917555656006327</td>
            <td>9.453643104973128</td>
        </tr>
        <tr>
            <td>Minimum Muscular Activation Duration</td>
            <td>6.0499379748798265</td>
            <td>4.917555656006327</td>
            <td>9.453643104973128</td>
        </tr>
        <tr>
            <td>Average Muscular Activation Duration</td>
            <td>6.0499379748798265</td>
            <td>4.917555656006327</td>
            <td>9.453643104973128</td>
        </tr>
        <tr>
            <td>Standard Deviation of Muscular Activation Duration</td>
            <td>0.0</td>
            <td>0.0</td>
            <td>0.0</td>
        </tr>
        <tr>
            <td>Maximum Sample Value</td>
            <td>0.044714754707631366</td>
            <td>0.7026604311199208</td>
            <td>1.3318609080773043</td>
        </tr>
        <tr>
            <td>Minimum Sample Value</td>
            <td>-0.057490398909811787</td>
            <td>-0.6355882990584738</td>
            <td>-1.255207042864222</td>
        </tr>
        <tr>
            <td>Average Sample Value</td>
            <td>-0.016568227882199745</td>
            <td>-0.016024050232231954</td>
            <td>-0.01649122739098117</td>
        </tr>
        <tr>
            <td>Standard Deviation Sample Value</td>
            <td>0.02642526322805102</td>
            <td>0.0909902158935363</td>
            <td>0.18601376405757442</td>
        </tr>
        <tr>
            <td>RMS</td>
            <td>0.031189753314643038</td>
            <td>0.09239041927709515</td>
            <td>0.18674335597211486</td>
        </tr>
        <tr>
            <td>Area</td>
            <td>-106.88423330648733</td>
            <td>-141.79687499999793</td>
            <td>-242.3236283603801</td>
        </tr>
        <tr>
            <td>Total Power Spect</td>
            <td>0.0007000399299170216</td>
            <td>0.008355839629936957</td>
            <td>0.033161401354944164</td>
        </tr>
        <tr>
            <td>Median Frequency</td>
            <td>62.5</td>
            <td>25</td>
            <td>117.1875</td>
        </tr>
        <tr>
            <td>Maximum Power Frequency</td>
            <td>58.59375</td>
            <td>109.375</td>
            <td>113.28125</td>
        </tr>
    </table>

## Bibliografía
[1] R. Pal, “Comparison of the design of FIR and IIR filters for a given specification and removal of phase distortion from IIR filters,” 2017 International Conference on Advances in Computing, Communication and Control (ICAC3). IEEE, Dec. 2017. doi: 10.1109/icac3.2017.8318772. <br>

[2] É. Thibault, F. L. Désilets, B. Poulin, M. Chioua, and P. Stuart, “Comparison of signal processing methods considering their optimal parameters using synthetic signals in a heat exchanger network simulation,” Computers &amp; Chemical Engineering, vol. 178. Elsevier BV, p. 108380, Oct. 2023. doi: 10.1016/j.compchemeng.2023.108380. <br>

[3] T. Oo and P. Phukpattaranont, “Signal-to-Noise Ratio Estimation in Electromyography Signals Contaminated with Electrocardiography Signals,” Fluctuation and Noise Letters, vol. 19, no. 03. World Scientific Pub Co Pte Lt, p. 2050027, Feb. 17, 2020. doi: 10.1142/s0219477520500273.