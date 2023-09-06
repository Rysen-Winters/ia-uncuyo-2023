# **Inteligencia Artificial I**
## **UNCuyo - Facultad de Ingeniería**
## **Trabajo Práctico 2 - Agentes Racionales.**

- 2.10 Consider a modified version of the vacuum environment in Exercise 2.8, in which the agent is penalized one point for each movement.
  - a. Can a simple reflex agent be perfectly rational for this environment? Explain.

Creo que puede diseñarse un agente perfectamente racional ya que solamente deberíamos reinterpretar la función de rendimiento para que se interprete que buscamos los valores más altos en cuanto a valores negativos y positivos o cero.  

  - b. What about a reflex agent with state? Design such an agent.

Este agente debe poder observar sus alrededores para determinar cuál es el siguiente movimiento que va a mejorar su medición de desempeño, debe preferir moverse a una celda que esté sucia ya que esta anularía el valor negativo del movimiento. Las acciones que puede realizar se mantienen de la misma manera.

  - c. How do your answers to a and b change if the agent’s percepts give it the clean/dirty status of every square in the environment?

Realmente no cambian ya que la implementación debería ser la misma, para evitar la disminución del parámetro de rendimiento.

- 2.11 Consider a modified version of the vacuum environment in Exercise 2.8, in which the geography of the environment—its extent, boundaries, and obstacles—is unknown, as is the initial dirt configuration. (The agent can go Up and Down as well as Left and Right.)
  - a. Can a simple reflex agent be perfectly rational for this environment? Explain.

Si se puede ya que si se implementa una función como "accept_action" para verificar la posibilidad de realizar una acción, entonces podemos evitar los obstaculos y continuar limpiando.
  
  - b. Can a simple reflex agent with a randomized agent function outperform a simple reflex agent? Design such an agent and measure its performance on several environments.

Si podría tener mejor performance en los casos en los que no se encuentre tan seguido con obstáculos como el agente reflexivo simple, pero para esto la función de movimiento aleatorio debería recordar el camino por el que viene para no "retroceder" y lograr una mejor performance que el agente simple en algunos casos, no en todos. Ya que en los casos en que se pudiera volver sobre sus pasos a donde ya limpió desperdiciaría movimientos.
  
  - c. Can you design an environment in which your randomized agent will perform poorly? Show your results.

Cualquier entorno el cual disponga de muchos obstáculos y el agente comienze a operar desde la cercanía a alguno de ellos, entonces el agente se encontraría contínuamente con obstáculos obligandolo a cambiar de dirección hacia lugares que ya limpió.
  
  - d. Can a reflex agent with state outperform a simple reflex agent? Design such an agent and measure its performance on several environments. Can you design a rational agent of this type?

Si puede tener una mejor performance, considerando que puede observar los estados de las celdas a su alrededor para "planificar" moverse de forma óptima para limpiar las celdas.
