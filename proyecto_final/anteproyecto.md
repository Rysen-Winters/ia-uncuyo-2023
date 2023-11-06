# UNCUYO - Inteligencia Artificial I - 2023:
## Proyecto Final.


## Modelo para detectar cuentas falsas de Instagram.

**Nombre código del proyecto:** Heartbreak.

**Integrantes:** Nahuel Arrieta (13729) y Leonel Castinelli (13198).

### Descripción.

El proyecto consta  de generar un modelo que pueda predecir si una cuenta de la red social Instagram es falsa (ya sea un bot o tenga seguidores comprados). Se utilizará un algoritmo de machine learning entrenado con un dataset de 
la plataforma kaggle (https://www.kaggle.com/datasets/krpurba/fakeauthentic-user-instagram) el cuál ha recopilado datos de 65326 usuarios reales o auténticos y falsos desde el 1 al 20 de septiembre de 2019, lo cual prueba ser de grán 
utilidad ya que contiene muchas métricas de cada usuario. Además de ser muy extensa.  

### Objetivos, alcances y limitaciones.

Nuestro  objetivo principal es desarrollar un modelo con machine learning que logre clasificar efectivamente un perfil falso de Instagram, llamaremos “falso” a una cuenta que sea un bot o tenga seguidores comprados, ya que estas no son cuentas de usuario “normales”, “reales” o “auténticas”. 

El alcance de este proyecto se va a centrar únicamente en detectar cuentas falsas de Instagram. No sé abordarán otras redes sociales ni otro tipo de interacción dentro de la plataforma.

Las limitaciones de este proyecto se deben a que está restringido a la red social de Instagram, y perfiles de la misma del año 2019, y los cambios sociales y tecnológicos a lo largo de los años podrían determinar una diferencia de las características que se usan para determinar si una cuenta es de un bot o spammer

### Formas de evaluación.

Se utilizarán las siguientes métricas:
  - **Exactitud (Accuracy):** Cantidad de cuentas identificadas correctamente como falsas en comparación con todas las cuentas clasificadas.
  - **Sensibilidad (Recall):** Proporción de cuentas falsas reales son detectadas por el modelo.
  - **Precisión (Precisión):** Cuántas de las cuentas que el modelo etiqueta como falsas son verdaderamente falsas.
  - **Especificidad (Specificity):** Cuántas de las cuentas que el modelo etiqueta como falsas son verdaderamente falsas.

### Justificación.

Consideramos que un modelo de machine learning es un enfoque correcto para el problema planteado porque estos pueden detectar patrones y relaciones complejas entre las características de las cuentas.

La detección de cuentas falsas requiere un gran análisis estadístico que un modelo de ML puede realizar en tiempo real y de manera eficiente. Especialmente, teniendo la posibilidad de entrenarlo con un dataset de 65.000 datos ya etiquetados, además de poder encontrar relaciones entre las columnas del dataset que pasarían inadvertidas ante un humano.

### Listado de actividades a realizar:

  - **Actividad 1:** Recopilar información. **[1 día]**
  - **Actividad 2:** Limpiar la información. **[3 días]**
  - **Actividad 3:** Preprocesamiento de datos. **[3 días]**
  - **Actividad 4:** Selección de los conjuntos de entrenamiento y prueba. **[2 días]**
  - **Actividad 5:** Entrenamiento del modelo. **[5 días]**
  - **Actividad 6:** Validación del modelo y análisis de las métricas resultantes. **[2 días]** 
  - **Actividad 7:** Ajustes al modelo. **[4 días]**
  - **Actividad 8:** Elaboración del informe final. **[4 días]**
