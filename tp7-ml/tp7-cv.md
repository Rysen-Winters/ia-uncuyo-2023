# UNCuyo - Inteligencia Artificial I - 2023
## Trabajo Práctico 7 - Machine Learning

## Parte A

Funcion create_folds:

```{r}
create_folds <- function(df, k) {

  n <- nrow(df)
  s <- seq_len(n)
  set.seed(123)  # Para reproducibilidad
  s <- sample(s)
  folds <- split(s, cut(seq_along(s), breaks=k, labels=FALSE))
  folds <- setNames(folds, paste0("Fold", seq_along(folds)))

  return(folds)
}
```

Funcion cross_validation:

```{r}
library(rpart)
library(caret)

cross_validation <- function(df, k) {
  accuracy <- precision <- sensitivity <- specificity <- list()
  
  folds <- create_folds(df, k)
  
  for(i in seq_along(folds)) {
    # Crear los conjuntos de entrenamiento y prueba
    train_indices <- unlist(folds[-i])
    test_indices <- folds[[i]]
    train_df <- df[train_indices, ]
    test_df <- df[test_indices, ]
    
    train_df$especie <- factor(train_df$especie, levels = levels(df$especie))
    test_df$especie <- factor(test_df$especie, levels = levels(df$especie))
    
    train_formula <- formula(inclinacion_peligrosa~altura+circ_tronco_cm+lat+long+seccion+especie)
    tree_model <- rpart(train_formula, data = train_df, method = "class")
    
    predictions <- predict(tree_model, newdata = test_df, type = "class")
    
    cm <- confusionMatrix(predictions, as.factor(test_df$inclinacion_peligrosa))
    accuracy[[i]] <- cm$overall["Accuracy"]
    precision[[i]] <- cm$byClass["Pos Pred Value"]
    sensitivity[[i]] <- cm$byClass["Sensitivity"]
    specificity[[i]] <- cm$byClass["Specificity"]
  }
  
  metrics <- list(
    mean_accuracy = mean(unlist(accuracy)),
    sd_accuracy = sd(unlist(accuracy)),
    mean_precision = mean(unlist(precision)),
    sd_precision = sd(unlist(precision)),
    mean_sensitivity = mean(unlist(sensitivity)),
    sd_sensitivity = sd(unlist(sensitivity)),
    mean_specificity = mean(unlist(specificity)),
    sd_specificity = sd(unlist(specificity))
  )
  
  return(metrics)
}
```

Y obtengo los siguientes resultados:

| media accuracy | media precision | media sensitivity | media specificity|
|----------------|-----------------|-------------------|------------------|
|0.8891849       |0.8891849        |1                  |0                 |

| sd accuracy | sd precision | sd sensitivity | sd specificity|
|-------------|--------------|----------------|---------------|
|0.006481041  |0.006481041   |0               |0              |

