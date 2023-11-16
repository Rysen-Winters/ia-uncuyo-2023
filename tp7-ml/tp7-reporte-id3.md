# UNCuyo - Inteligencia Artificial - 2023
## Trabajo Práctico 7 - Machine Learning

### Id3

## Resultados de la ejecución del código:

Este es el árbol devuelto por el algoritmo, cada nodo está representado por (padre, arco_padre, atributo). El valor de padre, es el valor de atributo para el padre del nodo, el valor de arco_padre es el valor que debe tomar el atributo del padre para llegar hasta este nodo, y atributo es el atributo que representa este nodo. En cada línea se representa cada nivel del árbol

(p:None, a:temp), 

(p:temp, p_arcv:mild, a:outlook), (p:temp, p_arcv:cool, a:humidity), (p:temp, p_arcv:hot, a:humidity), 

(p:outlook, p_arcv:overcast, a:yes), (p:outlook, p_arcv:sunny, a:humidity), (p:outlook, p_arcv:rainy, a:humidity), (p:humidity, p_arcv:normal, a:play), (p:humidity, p_arcv:high, a:outlook), (p:humidity, p_arcv:normal, a:yes), 

(p:humidity, p_arcv:high, a:no), (p:humidity, p_arcv:normal, a:yes), (p:humidity, p_arcv:high, a:windy), (p:humidity, p_arcv:normal, a:yes), (p:play, p_arcv:no, a:no), (p:play, p_arcv:yes, a:yes), (p:outlook, p_arcv:overcast, a:yes), (p:outlook, p_arcv:sunny, a:no), 

(p:windy, p_arcv:False, a:yes), (p:windy, p_arcv:True, a:no), 


## Investigación de las estrategias de árboles de decisión para valores reales