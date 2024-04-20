# LABORATORIO 4 – USO DE BITALINO PARA ADQUISICIÓN DE ECG

## Tabla de contenidos:
* [Introducción](#introducción)
* [Objetivos](#objetivos)
* [Laboratorio](#laboratorio)
  * [Materiales y equipos](#materiales-y-equipos) 
  * [Conexiones](#conexiones)
  * [Videos de las señales](#videos-de-las-señales)
  * [Gráficos OpenSignals](#gráficos-opensignals)
  * [Gráficos en Python](#gráficos-en-python)
  * [Discusión](#discusión)
  * [Archivos](#archivos)
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
Se utilizo el cable de 3 hilos con sus respectivos electrodos. Cada uno de estos electrodos representa positivo (rojo), tierra (negro) y referencia (blanco). Para realizar las conexiones nos basamos en el protocolo BITalino (r)evolution Home Guide EXPERIMENTAL GUIDES TO MEET & LEARN YOUR BIOSIGNALS for ECG [4].

Para iniciar colocamos el electrodo positivo (color rojo) en el brazo izquierdo (LA), el electrodo de tierra (color negro) en el brazo derecho (RA) y el electrodo de referencia (color blanco) en la cresta ilíaca. Así como observamos en la Figura 3.

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/2fa317490d28b054b08d5514ffaf15fa897ba176/ISB/imagenes_multimedia/Multimedia-Lab4/electrodos_posicion.jpeg" align="center" width="500" height="300"/>
<div align="center"> <i>Figura 3: Conexiones de los electrodos [4]</i></div>
<p>


### Videos de las señales
En los próximos videos se exhiben las conexiones entre los electrodos y el cuerpo, así como la visualización de la señal en OpenSignals.

En el primer video podemos ver la toma de datos mientras el voluntario se encuentra en reposo:

https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/74bf5743-b49f-42ba-a7a9-069db939b2e3

En el segundo video podemos ver la toma de datos mientras el voluntario inhala, retiene el aire y exhala en intervalos de 5 segundos y repitiendo el ciclo 3 veces.

https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/08f5c110-b067-41a3-b808-52e580c174cb

En el tercer video podemos ver la toma de datos mientras el voluntario realiza actividad física por 3 minutos.

https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/c8472407-25ef-414d-acdf-0da7afba72b0

En el cuarto video podemos ver la toma de datos 30 segundos después de que el voluntario terminara de realizar la actividad física.

https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/a67f14d2-20e0-4fd5-a7d9-8645a3a4b376

En el quinto video podemos ver  la señal en OpenSignalsFluke resultante del dispositivo ProSim 4 Vital Signs Patient Simulator l mientras simula una parada cardíaca con las siguientes características:

* ECG 80 lpm
* CYP (VI)
* Taquicardia ventricular 160 lpm
* Fibrilación ventricular severa
* Asistolia

https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/a93f4b83-0696-41df-8bf7-1c22f4d6ab00

### Gráficos OpenSignals
En las gráficas obtenidas se aprecia la disposición espacial de las ondas PQRST, el intervalo QT, el segmento ST y el complejo QRS. Hemos indicado en cada imágen donde empieza cada onda para un mejor análisis. En la Figura 4, 5 y 7 se pueden apreciar mejor los segmentos de las ondas PQRST a comparación de la Figura 6, donde el voluntario estaba haciendo ejercicio y esto puede deberse al ruido causado por el movimiento del BITalino.

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/8eff27c4180e70eeab2fd06f877e03ae0a7fd0ea/ISB/imagenes_multimedia/Multimedia-Lab4/reposo_os.png" align="center" width="500" height="300"/>
<div align="center"> <i>Figura 4: Señal en reposo OpenSignal</i></div>
<p>

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/8eff27c4180e70eeab2fd06f877e03ae0a7fd0ea/ISB/imagenes_multimedia/Multimedia-Lab4/ciclo_respiraci%C3%B3n_os.png" align="center" width="500" height="300"/>
<div align="center"> <i>Figura 5: Señal en los ciclos de respiración OpenSignal</i></div>
<p>

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/8eff27c4180e70eeab2fd06f877e03ae0a7fd0ea/ISB/imagenes_multimedia/Multimedia-Lab4/ejercicio_os.png" align="center" width="500" height="300"/>
<div align="center"> <i>Figura 6: Señal mientras el voluntario hace ejercicio OpenSignal</i></div>
<p>

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/8eff27c4180e70eeab2fd06f877e03ae0a7fd0ea/ISB/imagenes_multimedia/Multimedia-Lab4/post_ejercicio_os.png" align="center" width="500" height="300"/>
<div align="center"> <i>Figura 7: Señal 30 segundos después del ejercicio OpenSignal</i></div>
<p>

Es importante destacar que significa cada uno de los segmentos de la onda que estamos viendo:
* Onda P: Representa la despolarización auricular en el ECG. La primera mitad muestra la despolarización de la aurícula derecha, seguida de la despolarización de la aurícula izquierda suele  tener una duración menor a 100ms y una amplitud maxima de 0.25mV. [5]
* Intervalo PR: Representa el tiempo desde el inicio de la despolarización auricular hasta el comienzo de la despolarización ventricular e incluye el retraso en el nodo AV. Su duración promedio es de 120 a 200 ms. Variaciones en el intervalo PR pueden indicar diversos trastornos. [5]
* Complejo QRS:Representa la despolarización ventricular a medida que la corriente pasa por el nodo AV. Un complejo QRS estándar tiene una duración generalmente de 60 a 100 ms. [5]
  * Onda Q: Representa la despolarización del tabique interventricular. Su duración no debe ser mayor a¿a 40 milisegundos. [5]
  * Onda R:Es la onda más alta del complejo QRS, representando el estímulo eléctrico a medida que pasa por los ventrículos durante la despolarización. [5]
  * Onda S: Representa la despolarización final de las fibras de Purkinje. Es cualquier deflexión hacia abajo después de la onda R. [5]
 * Onda T: Representa la repolarización ventricular. Su morfología es altamente susceptible a influencias cardíacas y no cardíacas. Usualmente es positiva en derivaciones con ondas R altas (deflexión hacia arriba). [5]
* Segmento ST: Representa el final de la despolarización ventricular y el comienzo de la repolarización ventricular. La elevación o depresión del segmento ST por 1 mm o más, medido en el punto J, es anormal. [5]
* Intervalo QT: Representa el inicio de la despolarización hasta el final de la repolarización de los ventrículos. La duración normal del intervalo QT es menos de 400 a 440 milisegundos. Un intervalo QT prolongado presenta un riesgo inminente de arritmias ventriculares graves. [5]

Ahora plotearemos los datos recopilados en Python para poder obtener un mejor analisis. 

### Gráficos en Python

Después de recopilar los datos, ploteamos en Python para poder analizar mejor las señales obtenidas.

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/62b2c775246810dce0b9eafbf1d66b164a0f14ac/ISB/imagenes_multimedia/Multimedia-Lab4/reposo_py.png" align="center" width="500" height="300"/>
<div align="center"> <i>Figura 8: Señal en reposo ploteada en Python</i></div>
<p>

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/62b2c775246810dce0b9eafbf1d66b164a0f14ac/ISB/imagenes_multimedia/Multimedia-Lab4/respiraci%C3%B3n_py.png" align="center" width="500" height="300"/>
<div align="center"> <i>Figura 9: Señal en los ciclos de respiración ploteada en Python</i></div>
<p>

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/62b2c775246810dce0b9eafbf1d66b164a0f14ac/ISB/imagenes_multimedia/Multimedia-Lab4/ejercicio_py.png" align="center" width="500" height="300"/>
<div align="center"> <i>Figura 10: Señal mientras el voluntario hace ejercicio ploteada en Python</i></div>
<p>

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/62b2c775246810dce0b9eafbf1d66b164a0f14ac/ISB/imagenes_multimedia/Multimedia-Lab4/post_ejercicio_py.png" align="center" width="500" height="300"/>
<div align="center"> <i>Figura 11: Señal 30 segundos después del ejercicio ploteada en Python</i></div>
<p>

En las gráficas obtenidas después de plotear en Python podemos apreciar con más claridad la disposición espacial de las ondas PQRST, el intervalo QT, el segmento ST y el complejo QRS. Hemos indicado en cada imágen donde empieza cada onda para un mejor análisis. Al igual que con las gráficas de OpenSignal en los ploteos de las señales en reposo, en el ciclo de respiración se pueden notar mejor los segmentos y en la recuperación después del ejercicio (Figura 8,9,11). A comparación de la Figura 10, donde el voluntario estaba haciendo ejercicio y no se pueden apreciar de manera correcta los segmentos, esto puede deberse al ruido causado por el movimiento del BITalino.

Para finalizar, plotearemos también las señales que obtuvimos del dispositivo ProSim 4 Vital Signs Patient Simulator l mientras simula una parada cardíaca.

| Nivel 1: ECG 80 lpm | Nivel 2: CYP (VI) | Nivel 3: Taq. Ventricular 160 lpm | Nivel 4: FiB. Ventricular Severa | Nivel 5: Asistolia |
| :---      |   :---:  |   :---:  |   :---:  |   :---:  |   
| ![señal_ecg_rsn_py](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/37b3151d-0174-4024-a453-0848635ad7da) | ![nivel2_py](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/d8a908ac-dd91-4b82-b905-cd67bf596c35) | ![NIVEL3](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/7432f389-bd97-43c4-8970-7c78a4b97f49) | ![NIVEL4](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/f7a40d05-3cbc-45d0-b9e6-ab5bd93627e0) | ![NIVEL 5](https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/b4f91027-ce77-414b-a02b-49e77f0eeb09) |


Podemos notar que en la primera gráfica podemos observar con precisión la disposición espacial de las ondas PQRST y analizar cada fase:

* Fase 1: ECG 80 lpm: En esta fase, podemos decir que el paciente presenta una frecuencia cardíaca normal de 80 latidos por minuto (lpm). Ya que es menor a 100 lpm y mayor a 60 lpm. [6]
  * Onda P: La onda P parece ser normal.
  * Complejo QRS: El complejo QRS parece ser normal.
  * Onda T: La onda T parece ser normal.
   
* Fase 2: CYP (VI): En esta fase, el paciente presenta una contracción ventricular prematura (CYP) en el ventrículo izquierdo (VI). Una CYP es un tipo de latido cardíaco anormal que se origina fuera del marcapasos natural del corazón. Las CYP pueden ser benignas o pueden ser un signo de una enfermedad cardíaca más grave.[6]
  * Onda P: La onda P parece ser normal.
  * Complejo QRS: Podemos distinguir el complejo QRS pero tiene una morfología diferente a la de un latido normal.
  * Onda T: La onda T no se puede distinguir muy bien.
   
* Fase 3: Taq. Ventricular 160 lpm: En esta fase, el paciente presenta una taquicardia ventricular (TV), que es un ritmo cardíaco rápido y anormal que se origina en los ventrículos. La TV puede ser una condición grave que puede conducir a un paro cardíaco. [6]
  * Onda P: Notamos que las ondas P son difíciles de distinguir debido a la frecuencia cardíaca rápida.
  * Complejo QRS: Los complejos QRS son estrechos y regulares y la frecuencia cardíaca es muy alta.
  * Onda T: Las ondas T son difíciles de distinguir debido a la frecuencia cardíaca rápida.

* Fase 4: FiB. Ventricular Severa: En esta fase, el paciente presenta una fibrilación ventricular (FV), que es un ritmo cardíaco caótico e irregular que se origina en los ventrículos. La FV es una condición mortal que requiere desfibrilación inmediata. [6]
  * Onda P: Las ondas P no están presentes debido a la actividad eléctrica caótica en los ventrículos.
  * Complejo QRS: Tampoco hay complejos QRS discernibles, solo una línea ondulada que representa la actividad fibrilacionante.
  * Onda T: No hay ondas T debido a la actividad eléctrica caótica.

* Fase 5: Asistolia: En esta fase, el paciente presenta asistolia, que es la ausencia de actividad eléctrica en el corazón. [7]
  * Onda P: No hay ondas P debido a la ausencia de actividad eléctrica en el corazón.
  * Complejo QRS: No hay complejos QRS debido a la ausencia de actividad eléctrica en el corazón.
  * Onda T: No hay ondas T debido a la ausencia de actividad eléctrica en el corazón.

### Discusión
Después de obtener las señales en cuatro condiciones diferentes: en reposo, durante el ciclo de respiración, durante y después de la actividad física. Revisammos la literatura para comparar nuestros resultados. En un estudio realizado acerca de los cambios graduales en la forma de onda del ECG durante y después del ejercicio en sujetos normales podemos encontrar que durante el ejercicio, se observó una disminución en el intervalo entre el pico de la onda P y el inicio del complejo QRS, acompañada de un aumento en la magnitud de la onda P, lo que indica una sobrecarga auricular derecha predominante. No se registraron cambios significativos en la duración del complejo QRS, ni en la magnitud y orientación espacial de los vectores QRS máximos. Sin embargo, el intervalo entre el inicio del QRS y el pico de la onda T se acortó. Durante el ejercicio, los vectores terminales QRS y los vectores ST se desplazaron gradualmente hacia la derecha y hacia arriba. [8]

* Descanso: Durante esta fase, se observaron los picos QRS correspondientes a la despolarización ventricular. La señal fue estable en esta segunda derivada, con una frecuencia cardíaca normal (70 a 80 latidos por minuto). Sin embargo, es notable que los picos no fueron tan intensos como la señal obtenida con el generador de señales fisiológicas. Se sospecha que esto puede deberse a la falta de uso de gel conductor, el cual reduce la resistencia entre la piel y el electrodo, o a una colocación imprecisa de los electrodos en el cuerpo.

* Ciclo de respiración: Se procuró comenzar la medición desde un punto neutral, iniciando la inhalación justo al comienzo. Después de aproximadamente 20 segundos, se realizó la exhalación para observar la reacción de la señal. Durante la fase de inhalación y alrededores, se observó un ligero aumento en la frecuencia cardíaca, lo cual coincide con lo que se estipula en [6]. Durante la fase de contención de la respiración, se comenzó a observar un comportamiento ligeramente sinusoidal entre las zonas T y P de la señal (correspondiente a la repolarización ventricular), que también se expandió hacia algunas ondas QRS, causando una deformación. Este comportamiento sinusoidal podría deberse a que en ocasiones la persona tenía que hacer un esfuerzo adicional al contener la respiración, lo que produciría un resultado similar a la disnea con esfuerzo, y esta característica puede generar sinusoidalidad en la señal.

* Después del ejercicio: La característica principal fue la aceleración del ritmo cardíaco, aproximadamente a más de 120 latidos por minuto (60 por medio minuto, que fue la duración de la adquisición). Este ritmo fue disminuyendo gradualmente, ya que después del ejercicio vigoroso se tomó un tiempo para volver a conectar los electrodos del "Bitalino". Nuevamente, la señal fue similar en frecuencia a la observada con el generador de señales, pero con menor intensidad, atribuida a las mismas causas que en el caso del reposo [8].



Comparamos estos resultados teóricos con nuestros resultados: 







## Bibliografía
[1] American Heart Association [Internet]. Dallas (TX): American Heart Association Inc.; c2022. Electrocardiogram (ECG or EKG); [Consultado: 19-abr-2024]. Available from: http://www.heart.org/en/health-topics/heart-attack/diagnosing-a-heart-attack/electrocardiogram-ecg-or-ekg

[2] Cleveland Clinic: Health Library: Diagnostics & Testing [Internet]. Cleveland (OH): Cleveland Clinic; c2022. Electrocardiogram (EKG); [Consultado: 19-abr-2024]. Available from: https://my.clevelandclinic.org/health/diagnostics/16953-electrocardiogram-ekg

[3] “BITalino Lab Guides (Home Guides) – Support PLUX Biosignals official,” support.pluxbiosignals.com. https://support.pluxbiosignals.com/knowledge-base/bitalino-lab-guides/. [Accessed: 19-Apr-2024].

[4] “BITalino Lab Guides (Home Guides) – Support PLUX Biosignals official,” support.pluxbiosignals.com. https://support.pluxbiosignals.com/knowledge-base/bitalino-lab-guides/ [Accessed: 19-Apr-2024].

[5]	Y. Sattar y L. Chhabra, Electrocardiogram. StatPearls Publishing, 2023.

[6]	Facultad de Medicina de la Universidad complutense, Guiones para la práctica clínica: Electrocaargiografía Básica. Ucm.es. [En línea]. Disponible en: https://medicina.ucm.es/data/cont/media/www/pag-17227/Electrocardiograf%C3%ADa%20B%C3%A1sica.pdf. [Consultado: 20-abr-2024].

[7]	“Asistolia”, https://www.cun.es. [En línea]. Disponible en: https://www.cun.es/diccionario-medico/terminos/asistolia. [Consultado: 20-abr-2024].

[8]	M. L. Simoons y P. G. Hugenholtz, “Gradual changes of ECG waveform during and after exercise in normal subjects”, Circulation, vol. 52, núm. 4, pp. 570–577, 1975.



