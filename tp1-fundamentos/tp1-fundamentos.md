# **Inteligencia Artificial I**
## **UNCuyo - Facultad de Ingeniería**
## **Trabajo Práctico 1 - Fundamentos**
Leonel Castinelli

### _Ejercicio 1: Resumen capítulo 26 (Philosophical foundations) de Artificial Intelligence: A Modern Approach._

"Cada aspecto del aprendizaje o cualquier otra característica de inteligencia está tan precisamente descrita que se puede crear una máquina que lo simule" - McCarthy, esto se le conoce como Weak AI, que es la característica de que una máquina actúe como si fuera inteligente, bajo este precepto fue fundada la Inteligencia Artificial. En contraste, otra definición, Strong AI, es que la máquina sea realmente capaz de pensar.

### **Weak AI: ¿Pueden las máquinas actuar inteligentemente?**

Comenzemos por lo importante, ¿Es la IA posible? Es posible si definimos a la Inteligencia Artificial como la búsqueda del mejor programa agente en una arquitectura dada.
Los filósofos se centran en la comparación de dos arquitecturas, el humano y la máquina. Y también se preocupan por la pregunta "¿Pueden las máquinas pensar?".
"La pregunta de si las máquinas pueden pensar, es tan relevante como preguntarse si los submarinos pueden nadar." - Edsger Dijkstra (1984). Las definiciones de un idioma para capacidades como
volar o nadar, están atadas a las capacidades expresivas del idioma en el que están siendo expresadas. Por ejemplo, si para nadar lo definimos como "Navegar a través del agua por medio de extremidades,
aletas o cola" como se define en el diccionario inglés, podemos afirmar que un submarino no puede nadar. Sin embargo para volar: "Moverse a través del aire por medio de alas o partes similares a alas",
con esta definición podemos afirmar que los aviones vuelan ya que tienen "partes similares a alas". 

Alan Turing en su paper *Computing machinery and Intelligence* sugirió que en lugar de preguntarnos si una máquina puede pensar, deberíamos preguntar si las máquinas pueden pasar una prueba de inteligencia 
conductual, a la cual se la ha llamado *Test de Turing*. En dicho test, se pone a un Interrogador, el cual es humano, a conversar por mensajes escritos en línea con un programa, el Interrogador debe adivinar si estuvo conversando con una persona o un programa. Si el Interrogador es engañado por el programa el 30% de las veces. Esto varía los resultados según el interrogador, ya que un Interrogador experimentado podría ser más dificil de engañar, y otros Interrogadores podrían ser más fáciles de engañar, este último ha sido el caso de personas que han sido engañadas por distintos Chatbots a lo largo del tiempo.

**El argumento de las limitaciones.**

¿Que no puede hacer una máquina? Turing expresó que "una máquina nunca podria hacer X" y reemplazó X con: "Disfrutar las frutillas con crema", "Enamorarse", "Enamorar a alguien", "Ser el sujeto de su propio pensamiento", "Usar palabras apropiadamente", "hacer algo realmente nuevo", "Aprender de la experiencia" y más opciones imposibles para una máquina. Y los programas hoy en día son aún increíbles en el sentido de que asisten, automatizan y realizan tareas que son realizadas por humanos expertos en variedades de campos profesionales. Aunque tambíen han sido capaces de cosas que se creía que era imposible como Aprender de la experiencia y Diferenciar el bien del mal. Gracias a Meehl que descubrió que algoritmos sencillos de aprendizaje estadístico (regresión lineal o naive Bayes) predecían mejor que los expertos. Con esta información podemos afirmar que las máquinas pueden hacer cosas tan bien o incluso mejor que los humanos.

**La objeción matemática.**

Se argumenta que según el Teorema de la incompletitud de Gödel las máquinas tienen ciertas limitaciones debido a su naturaleza matemática (Demostrado por el trabajo de Alan Turing), para cualquier sistema axiomático formal F, lo suficientemente potente para realizar Aritmética, es posible construir una "frase de Gödel" con las siguientes propiedades:
- G(F) es una frase de F, pero no puede ser demostrada dentro de F.
- Si F es consistente, entonces G(F) es verdadero.

Este teorema limita a las IA según J.R. Lucas y las hace inferiores a los humanos. Pero fuera de la formalidad matemática que tiene el anterior teorema, básicamente estamos diciendo que hay cosas indemostrables para una computadora debido a la falta de información. Pero el principal problema de este argumento de J. R. Lucas es que está suponiendo que estas limitaciones no afectan a los humanos. Un ser humano tampoco podría demostrar hechos sin la información adecuada.

**El argumento de la informalidad.**

El "problema de la cualificación" argumenta que el comportamiento humano es tan complejo, que al intentar capturar las reglas lógicas por las cuales se rigen los humanos para tener su comportamiento, las computadoras no podrían capturar todas las reglas ni lograr comportamiento humano. El que propone esta visión de la IA es Hubert Dreyfus.

Dreyfus argumenta que la experiencia humana, el humano experto en alguna materia, su conocimiento incluye un grupo de reglas, pero sólo en el "entorno" en el que operan los humanos. Que el proceso de tomar decisiones o reaccionar a situaciones es un proceso inconsciente para el humano. Pero el problemas de este argumento es que no niega la existencia del proceso que lleva a cabo esas actividades lo cual podemos realizar para desarrollar IA. Y proponen (En este caso Hubert Dreyfus teoriza con su hermano Stuart Dreyfus) una red neuronal organizada en una gran "librería de casos" y resaltan varios problemas de esta.

1. Una buena generalización de ejemplos no puede ser lograda sin conocimiento del trasfondo, es decir es imposible incorporar nuevo conocimiento al trasfondo y relacionarlo al proceso neuronal. Desde el punto de vista de los autores (Norvig y Russell) esto implica realizar un rediseño del proceso neuronal para poder aprovecharse de el conocimiento ya disponible de la forma en que otros algoritmos de aprendizaje lo hacen.
2. El aprendizaje de la red neuronal es una forma de aprendizaje supervisado, donde se requiere la identificación previa de entradas relevantes y salidas correctas, es decir se requiere un "maestro" humano. Pero sin embargo existen los métodos de aprendizaje no supervisado y aprendizaje por refuerzo.
3. Los algoritmos de aprendizaje no tienen buen rendimiento si tienen muchas funcionalidades y no se pueden añadir funcionalidades si el conjunto actual de hechos no prueba ser adecuado para dichas funcionalidades. Cuando realmente hay métodos y principios para generar nuevas funcionalidades aunque requiere una cierta cantidad de trabajo.
4. El cerebro puede enfocar sus sensores para buscar información relevante y las máquinas no. Cuando en realidad se han desarrollado sensores activos que realizan este tipo de filtración de información.

### **Strong AI: ¿Pueden las máquinas realmente pensar?**

"Hasta que una máquina no escriba una sonata o componga un concerto por sus pensamientos y emociones que sintió, y no por probabilidad de escritura de símbolos, entonces podremos decir que la máquina es igual al cerebro. Es decir, no sólo escribir sino saber que lo ha escrito." - Geoffrey Jefferson (1949).
Turing llama a este argumento de la consciencia: La máquina debe ser consciente de su estado mental y acciones. Pero el principal tema de este argumento es la fenomenología, o el estudio de la experiencia directa: la máquina debe realmente sentir emociones. Y la otra se enfoca en la intencionalidad, es decir, que la máquina demuestre tener convicciones, deseos y otras representaciones sobre las cosas del mundo real. Pero Turing argumenta que la pregunta de "¿Pueden las máquinas pensar?" no la hacemos con otros seres humanos, sencillamente tenemos "la 'cortesía' de pensar que los otros seres humanos piensan". 

En 1848, se sintetizó urea artificial por Frederick Wöhler. Antes de esto la química orgánica e inorgánica eran en esencia empresas disjuntas y se pensaba que no habían procesos que podrían convertir químicos inorgánicos en material orgánico. Una vez que la síntesis se logró, los científicos acordaron que la urea artificial era urea, ya que tenía todas las propiedades físicas correctas. Esto nos lleva al problema mente-cuerpo, que básicamente es que el cuerpo tiene un estado cerebral a la vez que una persona tiene un estado mental, el estado cerebral representa físicamente al estado mental. 

El problema mente-cuerpo nos lleva rápidamente al problema de "el cerebro en un frasco", que argumenta sobre la realidad. ¿Cómo una persona puede saber qué es real? Si una persona tiene una experiencia subjetiva como "Estoy comiendo una hamburguesa", su estado mental es ese, y su estado cerebral representa la situación físicamente. Pero, si el cerebro de una persona se le extrae al nacer y se lo pone en un frasco con la tecnología suficiente para que este viva y crezca, y teniendo la tecnología para enviar y recibir señales del cerebro en cuestión, podríamos inducir artificialmente el estado mental y cerebral de "Estoy comiendo una hamburguesa". Esto lleva a dos corrientes de pensamiento: El de "vista amplia" donde nos consideramos un observador externo que comprende lo que es real y lo que es simulado, y comprendiendo la situación de la persona que está experimentando una simulación; y el de "vista estrecha" donde decimos que lo que experimenta el cerebro es la realidad. Donde si adoptamos la vista estrecha podríamos decir que el pensamiento simulado de una computadora realmente es pensamiento real.

**El funcionalismo y el experimento de reemplazo de cerebro.**

El funcionalismo argumenta que si una máquina simula la misma funcionalidad que un cerebro entonces es un cerebro sin importar la implementación específica de la funcionalidad. 
El experimento de reemplazo del cerebro se basa en lo siguiente, si ya estudiamos cada neurona del cerebro y comprendemos su funcionalidad, y creamos máquinas que replican exactamente lo que hace cada una de las neuronas del cerebro de una persona. Si cambiamos gradualmente el cerebro original de una persona por uno artificial que contiene la misma información, ¿Cómo podemos saber si la persona sigue siendo la misma tras el reemplazo?. ¿Por qué es importante esta pregunta? Porque si lograramos demostrar que es la misma persona, entonces el cerebro artificial es equivalente al normal y podríamos decir que las máquinas piensan realmente.

**La consciencia, qualia y la brecha explicativa.**

El problema de la conciencia, es que una máquina debe ser capaz de tener experiencias subjetivas, de que la máquina "perciba" que tiene estados mentales. La naturaleza intrínseca de las experiencias se lo conoce como "qualia". Estos conceptos presentar el problema de saber si las experiencias subjetivas son las mismas para todo el mundo, por ejemplo: ¿Cómo sabemos que todos percibimos de la misma forma el color rojo? Supongamos que una persona percibe el color rojo a través de sus ojos como el resto de nosotros percibimos el color verde. Esta persona aprende todo lo relacionado al color rojo, podrá expresar información con respecto a este color como cualquier otra persona ya que así es como lo aprendió, demostrando que es imposible demostrar que las experiencias subjetivas de cada persona es exactamente las mismas. A este problema se lo conoce como el problema del espectro invertido. Esta incapacidad de explicar incluso que una persona o máquina realmente tiene experiencias subjetivas, esta es la gran brecha explicativa.

### **Las éticas y riesgos del desarrollo de Inteligencia Artificial.**

El desarrollo de IA supone los siguientes problemas éticos:
- Las personas podrían perder sus trabajos por la automatización: Esto es un problema popularizado pero que en realidad es completamente distinto. Las personas temen que las IA los reemplaze en sus trabajos, cuando en realidad la IA automatizan procesos que no estaban incluidos en el trabajo de ninguna persona, además esta creando puestos de trabajos con mejores salarios y aunque en un futuro el desempleo quizá sea mayor, cada persona estará al mando de su propio grupo de robots trabajadores.
- Las personas podrían tener mucho o poco tiempo de ocio
