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
Un electrocardiograma (ECG) es una prueba común que registra la actividad eléctrica del corazón a través de electrodos colocados en el cuerpo. Es una herramienta valiosa para diagnosticar una variedad de enfermedades cardíacas. [1]

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
Como mencionamos anteriormente, utilizaremos BITalino el cual es una plataforma de hardware y software de bajo costo y código abierto que permite la adquisición de señales biomédicas, incluyendo ECG. La plataforma BITalino está compuesta por una placa de desarrollo, varios sensores y un software de adquisición y análisis de datos. La placa de desarrollo cuenta con un microcontrolador, conectividad Bluetooth y varios canales analógicos y digitales que permiten conectar una variedad de sensores. Los sensores BITalino incluyen sensores de ECG, EMG, EEG, acelerometría, fotopletismografía (PPG), temperatura, respiración y actividad electrodermal. El software de adquisición y análisis de datos permite visualizar las señales en tiempo real, guardar los datos para su posterior análisis y exportar los datos a diferentes formatos [3]. 

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
Se utilizo el cable de 3 hilos con sus respectivos electrodos. Cada uno de estos electrodos representa positivo (rojo), tierra (negro) y referencia (blanco). Para realizar las conexiones, nos basamos en el protocolo BITalino (r)evolution Home Guide EXPERIMENTAL GUIDES TO MEET & LEARN YOUR BIOSIGNALS for ECG [4].

Para iniciar, colocamos el electrodo positivo (color rojo) en el brazo izquierdo (LA), el electrodo de tierra (color negro) en el brazo derecho (RA) y el electrodo de referencia (color blanco) en la cresta ilíaca. Así como observamos en la Figura 3.

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/2fa317490d28b054b08d5514ffaf15fa897ba176/ISB/imagenes_multimedia/Multimedia-Lab4/electrodos_posicion.jpeg" align="center" width="500" height="300"/>
<div align="center"> <i>Figura 3: Conexiones de los electrodos [4]</i></div>
<p>


### Videos de las señales
En los próximos videos se exhiben las conexiones entre los electrodos y el cuerpo, así como la visualización de la señal en OpenSignals.

En el primer video, podemos ver la toma de datos mientras el voluntario se encuentra en reposo:

https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/74bf5743-b49f-42ba-a7a9-069db939b2e3

En el segundo video, podemos ver la toma de datos mientras el voluntario inhala, retiene el aire y exhala en intervalos de 5 segundos y repitiendo el ciclo 3 veces.

https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/08f5c110-b067-41a3-b808-52e580c174cb

En el tercer video, podemos ver la toma de datos mientras el voluntario realiza actividad física por 3 minutos.

https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/c8472407-25ef-414d-acdf-0da7afba72b0

En el cuarto video, podemos ver la toma de datos 30 segundos después de que el voluntario terminara de realizar la actividad física.

https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/a67f14d2-20e0-4fd5-a7d9-8645a3a4b376

En el quinto video, podemos ver  la señal en OpenSignalsFluke resultante del dispositivo ProSim 4 Vital Signs Patient Simulator l mientras simula una parada cardíaca con las siguientes características:

* ECG 80 lpm
* CYP (VI)
* Taquicardia ventricular 160 lpm
* Fibrilación ventricular severa
* Asistolia

https://github.com/sofia-is-a-panda/ISB_2024_G3/assets/111579919/a93f4b83-0696-41df-8bf7-1c22f4d6ab00

### Gráficos OpenSignals
En las gráficas obtenidas, se aprecia la disposición espacial de las ondas PQRST, el intervalo QT, el segmento ST y el complejo QRS. Hemos indicado en cada imágen dónde empieza cada onda para un mejor análisis. En la Figura 4, 5 y 7 se pueden apreciar mejor los segmentos de las ondas PQRST a comparación de la Figura 6, donde el voluntario estaba haciendo ejercicio y esto puede deberse al ruido causado por el movimiento del BITalino.

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/8eff27c4180e70eeab2fd06f877e03ae0a7fd0ea/ISB/imagenes_multimedia/Multimedia-Lab4/reposo_os.png" align="center" width="900" height="300"/>
<div align="center"> <i>Figura 4: Señal en reposo OpenSignal</i></div>
<p>

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/8eff27c4180e70eeab2fd06f877e03ae0a7fd0ea/ISB/imagenes_multimedia/Multimedia-Lab4/ciclo_respiraci%C3%B3n_os.png" align="center" width="900" height="300"/>
<div align="center"> <i>Figura 5: Señal en los ciclos de respiración OpenSignal</i></div>
<p>

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/8eff27c4180e70eeab2fd06f877e03ae0a7fd0ea/ISB/imagenes_multimedia/Multimedia-Lab4/ejercicio_os.png" align="center" width="900" height="300"/>
<div align="center"> <i>Figura 6: Señal mientras el voluntario hace ejercicio OpenSignal</i></div>
<p>

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/8eff27c4180e70eeab2fd06f877e03ae0a7fd0ea/ISB/imagenes_multimedia/Multimedia-Lab4/post_ejercicio_os.png" align="center" width="900" height="300"/>
<div align="center"> <i>Figura 7: Señal 30 segundos después del ejercicio OpenSignal</i></div>
<p>

Es importante destacar qué significa cada uno de los segmentos de la onda que estamos viendo:
* Onda P: Representa la despolarización auricular en el ECG. La primera mitad muestra la despolarización de la aurícula derecha, seguida de la despolarización de la aurícula izquierda suele  tener una duración menor a 100ms y una amplitud maxima de 0.25mV. [5]
* Intervalo PR: Representa el tiempo desde el inicio de la despolarización auricular hasta el comienzo de la despolarización ventricular e incluye el retraso en el nodo AV. Su duración promedio es de 120 a 200 ms. Variaciones en el intervalo PR pueden indicar diversos trastornos. [5]
* Complejo QRS: Representa la despolarización ventricular a medida que la corriente pasa por el nodo AV. Un complejo QRS estándar tiene una duración generalmente de 60 a 100 ms. [5]
  * Onda Q: Representa la despolarización del tabique interventricular. Su duración no debe ser mayor a 40 milisegundos. [5]
  * Onda R:Es la onda más alta del complejo QRS, representando el estímulo eléctrico a medida que pasa por los ventrículos durante la despolarización. [5]
  * Onda S: Representa la despolarización final de las fibras de Purkinje. Es cualquier deflexión hacia abajo después de la onda R. [5]
 * Onda T: Representa la repolarización ventricular. Su morfología es altamente susceptible a influencias cardíacas y no cardíacas. Usualmente es positiva en derivaciones con ondas R altas (deflexión hacia arriba). [5]
* Segmento ST: Representa el final de la despolarización ventricular y el comienzo de la repolarización ventricular. La elevación o depresión del segmento ST por 1 mm o más, medido en el punto J, es anormal. [5]
* Intervalo QT: Representa el inicio de la despolarización hasta el final de la repolarización de los ventrículos. La duración normal del intervalo QT es menos de 400 a 440 milisegundos. Un intervalo QT prolongado presenta un riesgo inminente de arritmias ventriculares graves. [5]

Ahora plotearemos los datos recopilados en Python para poder obtener un mejor analisis. 

### Gráficos en Python

Después de recopilar los datos, ploteamos en Python para poder analizar mejor las señales obtenidas.

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/62b2c775246810dce0b9eafbf1d66b164a0f14ac/ISB/imagenes_multimedia/Multimedia-Lab4/reposo_py.png" align="center" width="900" height="300"/>
<div align="center"> <i>Figura 8: Señal en reposo ploteada en Python</i></div>
<p>

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/62b2c775246810dce0b9eafbf1d66b164a0f14ac/ISB/imagenes_multimedia/Multimedia-Lab4/respiraci%C3%B3n_py.png" align="center" width="900" height="300"/>
<div align="center"> <i>Figura 9: Señal en los ciclos de respiración ploteada en Python</i></div>
<p>

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/62b2c775246810dce0b9eafbf1d66b164a0f14ac/ISB/imagenes_multimedia/Multimedia-Lab4/ejercicio_py.png" align="center" width="900" height="300"/>
<div align="center"> <i>Figura 10: Señal mientras el voluntario hace ejercicio ploteada en Python</i></div>
<p>

<p align="center" style="margin-bottom:0">
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/62b2c775246810dce0b9eafbf1d66b164a0f14ac/ISB/imagenes_multimedia/Multimedia-Lab4/post_ejercicio_py.png" align="center" width="900" height="300"/>
<div align="center"> <i>Figura 11: Señal 30 segundos después del ejercicio ploteada en Python</i></div>
<p>

En las gráficas obtenidas después de plotear en Python, podemos apreciar con más claridad la disposición espacial de las ondas PQRST, el intervalo QT, el segmento ST y el complejo QRS. Hemos indicado en cada imagen donde empieza cada onda para un mejor análisis. Al igual que con las gráficas de OpenSignal en los ploteos de las señales en reposo, en el ciclo de respiración se pueden notar mejor los segmentos y en la recuperación después del ejercicio (Figura 8,9,11). A comparación de la Figura 10, donde el voluntario estaba haciendo ejercicio y no se pueden apreciar de manera correcta los segmentos, esto puede deberse al ruido causado por el movimiento del BITalino.

Ahora plotearemos también las señales que obtuvimos del simulador de señales biomédicas *ProSim 4 Vital Signs Patient Simulator l* mientras se encontraba en la opción de parada cardíaca.

<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/main/ISB/imagenes_multimedia/Multimedia-Lab4/NIVEL1.png" align="center" width="900" height="300"/>
<div align="center"> <i>Figura 12: Nivel 1 - ECG 80 lpm</i></div>
<p>

&nbsp;
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/main/ISB/imagenes_multimedia/Multimedia-Lab4/nivel2_py.png" align="center" width="900" height="300"/>

<div align="center"> <i>Figura 13: Nivel 2 - CYP (VI) </i></div>
<p>
&nbsp;

<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/main/ISB/imagenes_multimedia/Multimedia-Lab4/NIVEL3.png" align="center" width="900" height="300"/>

<div align="center"> <i>Figura 14: Nivel 3 - Taquicardia Ventricular 160 lpm</i></div>
<p>
&nbsp;

<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/main/ISB/imagenes_multimedia/Multimedia-Lab4/NIVEL4.png" align="center" width="900" height="300"/>

<div align="center"> <i>Figura 15: Nivel 4 - Fibrilación Ventricular Severa</i></div>
<p>
&nbsp;
<img src="https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/main/ISB/imagenes_multimedia/Multimedia-Lab4/NIVEL%205.png" align="center" width="900" height="300"/>
<div align="center"> <i>Figura 16: Nivel 5 - Asistolia </i></div>
<p>

Podemos notar que la primera gráfica presenta una alta precisión de la disposición espacial de las ondas P y T, así como del complejo QRS. Ahora procedemos a analizar cada fase:

* Fase 1: ECG 80 lpm: En esta fase, podemos decir que el paciente presenta una frecuencia cardíaca normal de 80 latidos por minuto (lpm). Ya que es menor a 100 lpm y mayor a 60 lpm. [6]
  * Onda P: La onda P parece ser normal.
  * Complejo QRS: El complejo QRS parece ser normal.
  * Onda T: La onda T parece ser normal.
&nbsp;
* Fase 2: CYP (VI): En esta fase, el paciente presenta una contracción ventricular prematura (CYP) en el ventrículo izquierdo (VI). Una CYP es un tipo de latido cardíaco anormal que se origina fuera del marcapasos natural del corazón. Las CYP pueden ser benignas o pueden ser un signo de una enfermedad cardíaca más grave.[6]
  * Onda P: La onda P parece ser normal.
  * Complejo QRS: Podemos distinguir el complejo QRS pero tiene una morfología diferente a la de un latido normal.
  * Onda T: La onda T no se puede distinguir muy bien.
&nbsp;
* Fase 3: Taq. Ventricular 160 lpm: En esta fase, el paciente presenta una taquicardia ventricular (TV), que es un ritmo cardíaco rápido y anormal que se origina en los ventrículos. La TV puede ser una condición grave que puede conducir a un paro cardíaco. [6]
  * Onda P: Notamos que las ondas P son difíciles de distinguir debido a la frecuencia cardíaca rápida.
  * Complejo QRS: Los complejos QRS son estrechos y regulares y la frecuencia cardíaca es muy alta.
  * Onda T: Las ondas T son difíciles de distinguir debido a la frecuencia cardíaca rápida.
&nbsp;
* Fase 4: FiB. Ventricular Severa: En esta fase, el paciente presenta una fibrilación ventricular (FV), que es un ritmo cardíaco caótico e irregular que se origina en los ventrículos. La FV es una condición mortal que requiere desfibsrilación inmediata. [6]
  * Onda P: Las ondas P no están presentes debido a la actividad eléctrica caótica en los ventrículos.
  * Complejo QRS: Tampoco hay complejos QRS discernibles, solo una línea ondulada que representa la actividad fibrilacionante.
  * Onda T: No hay ondas T debido a la actividad eléctrica caótica.
&nbsp;
* Fase 5: Asistolia: En esta fase, el paciente presenta asistolia, que es la ausencia de actividad eléctrica en el corazón. [7]
  * Onda P: No hay ondas P debido a la ausencia de actividad eléctrica en el corazón.
  * Complejo QRS: No hay complejos QRS debido a la ausencia de actividad eléctrica en el corazón.
  * Onda T: No hay ondas T debido a la ausencia de actividad eléctrica en el corazón.

### Discusión
Después de obtener las señales en cuatro condiciones diferentes: En reposo, durante el ciclo de respiración, durante y después de la actividad física, se procedió a buscar la literatura correspondiente para contrastar los resultados obtenidos. 
En un estudio realizado acerca de los cambios graduales en la forma de onda del ECG durante y después del ejercicio en sujetos normales, podemos encontrar que, durante el ejercicio, se observó una disminución en el intervalo entre el pico de la onda P y el inicio del complejo QRS, acompañada de un aumento en la magnitud de la onda P, lo que indica una sobrecarga auricular derecha predominante. No se registraron cambios significativos en la duración del complejo QRS, ni en la magnitud y orientación espacial de los vectores QRS máximos. Sin embargo, el intervalo entre el inicio del QRS y el pico de la onda T se acortó. Durante el ejercicio, los vectores terminales QRS y los vectores ST se desplazaron gradualmente hacia la derecha y hacia arriba. [8]

Comparamos estos resultados teóricos con nuestros resultados: 

* Descanso: Durante esta fase, podemos observar claramente el complejo QRS correspondiente a la despolarización ventricular. Aunque no se puede distinguir nuy bien la onda P debido al ruido pero sí logramos identificaarla. Teoricamnente estamos en una frecuencia cardíaca promedio de 70 a 80 lpm en promedio [9]. Sin embargo, es notable que los picos (casi 0.4 mV) no fueron tan intensos como la señal obtenida con el generador de señales fisiológicas (casi 0.6 mV). Se sospecha que esto puede deberse a una colocación imprecisa de los electrodos.
  * Onda P: La onda P parece ser normal.
  * Complejo QRS: El complejo QRS parece ser normal.
  * Onda T: La onda T parece ser normal.
&nbsp;
* Ciclo de respiración: Se procuró iniciar la inhalación justo al comienzo de la medición. Después de aproximadamente 5 segundos de retener el aire, se realizó la exhalación para observar la reacción de la señal. Durante este ciclo de respiración se observó un ligero aumento en la frecuencia cardíaca, lo cual coincide con lo que se estipula teoricamente [9]. 
  * Onda P: La onda P parece ser normal y podemos notarla con mayor claridad
  * Complejo QRS: El complejo QRS parece ser normal y se nota con claridad. El pico R es casi 0.4 mV y el S es un poco mayor a 0.2mV.
  * Onda T: La onda T parece ser normal, se puede distinguir con mayor precisión.
&nbsp;
* Durante el ejercicio: La principal diferencia que notamos en la aceleración del ritmo cardíaco. Además, no podemos distinguir muy bien los sectores debido al ruido producido por el mmovimiento del BITalino, lo cual está impidiendo que se tomen medidas más precisas.
  * Onda P: No podemos distinguir la onda P.
  * Complejo QRS: El complejo QRS se distingue con un poco de dificultad. El pico R es casi 0.4 mV y el S es mayor a 0.2mV.
  * Onda T: La onda T no se puede distinguir con precisión.
&nbsp;
* Después del ejercicio: Al igual que durante el ejercicio la característica principal fue la aceleración del ritmo cardíaco, aproximadamente a más de 120 lpm segun la teoría [9]. Este ritmo fue disminuyendo gradualmente, ya que después del ejercicio el voluntario se tomó 30 segundos de descanso. Nuevamente, la señal fue similar en frecuencia a la observada con el generador de señales (casi 0.6mV), pero con menor intensidad (0.4mV), atribuida a las mismas causas que en el caso del reposo.
  * Onda P: La onda P no puede ser distinguida con claridad.
  * Complejo QRS: El complejo QRS parece ser normal y se nota con un poco de dificultad. El pico R es casi 0.4 mV y el S es un poco mayor a 0.4mV.
  * Onda T: La onda T no se puede distinguir con precisión.
 
## Archivos:

Se plotearon los datos en Python de un voluntario, como se mencionó anteriormente, cada uno realizó 4 mediciones:

* Medición en reposo.
* Medición durante un ciclo de respiración.
* Medición durante el ejercicio.
* Medición después del ejercicio.

Además ploteamos  las señales que obtuvimos del dispositivo ProSim 4 Vital Signs Patient Simulator l mientras simula una parada cardíaca.
  
Puede encontrar el código utilizado y los resultados [aquí](https://github.com/sofia-is-a-panda/ISB_2024_G3/blob/73cdda830ef0088f842043c9f554d41b80db1cde/ISB/Laboratorios/Laboratorio%204/Ploteo_se%C3%B1ales_Py.ipynb)

## Bibliografía
[1] American Heart Association [Internet]. Dallas (TX): American Heart Association Inc.; c2022. Electrocardiogram (ECG or EKG); [Consultado: 19-abr-2024]. Disponible en: http://www.heart.org/en/health-topics/heart-attack/diagnosing-a-heart-attack/electrocardiogram-ecg-or-ekg

[2] Cleveland Clinic: Health Library: Diagnostics & Testing [Internet]. Cleveland (OH): Cleveland Clinic; c2022. Electrocardiogram (EKG); [Consultado: 19-abr-2024]. Disponible en: https://my.clevelandclinic.org/health/diagnostics/16953-electrocardiogram-ekg

[3] “BITalino Lab Guides (Home Guides) – Support PLUX Biosignals official,” support.pluxbiosignals.com. Disponible en: https://support.pluxbiosignals.com/knowledge-base/bitalino-lab-guides/. 

[4] “BITalino Lab Guides (Home Guides) – Support PLUX Biosignals official,” support.pluxbiosignals.com. Disponible en: https://support.pluxbiosignals.com/knowledge-base/bitalino-lab-guides/ [Accessed: 19-Apr-2024].

[5]	Sattar Y, Chhabra L. Electrocardiogram. [Updated 2023 Jun 5]. In: StatPearls [Internet]. Treasure Island (FL): StatPearls Publishing; 2024 Jan-. Disponible en: https://www.ncbi.nlm.nih.gov/books/NBK549803/

[6]	Facultad de Medicina de la Universidad complutense, Guiones para la práctica clínica: Electrocaargiografía Básica. Ucm.es. [Internet]. Disponible en: https://medicina.ucm.es/data/cont/media/www/pag-17227/Electrocardiograf%C3%ADa%20B%C3%A1sica.pdf. 

[7]	“Asistolia”, https://www.cun.es. [Internet]. Disponible en: https://www.cun.es/diccionario-medico/terminos/asistolia. 

[8]	Simoons, M. L., & Hugenholtz, P. G. (1975). Gradual changes of ECG waveform during and after exercise in normal subjects. Circulation, 52(4), 570–577. Disponible en: https://doi.org/10.1161/01.cir.52.4.570

[9]	Relación del electrocardiograma con la respiración y el pulso. In: Garza N. eds. Manual de laboratorio de fisiología, 6e. McGraw-Hill Education; 2015. Disponible en: https://accessmedicina.mhmedical.com/content.aspx?bookid=1722&sectionid=116885435



