suppressMessages(library(readr))
suppressMessages(library(dplyr))
suppressMessages(library(ranger))

# lectura de los archivos
data_train <- readr::read_csv("./data/arbolado-mza-dataset.csv",
                              col_types = cols(
                                id = col_integer(),
                                especie = col_character(),
                                ultima_modificacion = col_character(),
                                altura = col_character(),
                                circ_tronco_cm = col_double(),
                                diametro_tronco = col_character(),
                                long = col_double(),
                                lat = col_double(),
                                seccion = col_integer(),
                                nombre_seccion = col_character(),
                                area_seccion = col_double(),
                                inclinacion_peligrosa = col_integer()
                              ))

data_test <-  readr::read_csv("./data/arbolado-mza-dataset-test.csv",col_types = cols(
                              id = col_integer(),
                              especie = col_character(),
                              ultima_modificacion = col_character(),
                              altura = col_character(),
                              circ_tronco_cm = col_double(),
                              diametro_tronco = col_character(),
                              long = col_double(),
                              lat = col_double(),
                              seccion = col_integer(),
                              nombre_seccion = col_character(),
                              area_seccion = col_double()
                              ))

# división y modificación de los datos y entrenamiento del modelo
data_train <- subset(data_train, select = -c(id,ultima_modificacion))
data_train$inclinacion_peligrosa <-as.factor(data_train$inclinacion_peligrosa)
set.seed(123)

train_indexes <- sample(1:nrow(data_train), size=0.03*nrow(data_train))
training_data <- data_train[train_indexes, ]
testing_data <- data_train[-train_indexes, ]

train_formula<-formula(inclinacion_peligrosa~especie+altura+circ_tronco_cm+diametro_tronco+long+lat+seccion+area_seccion)
forest <- ranger::ranger(formula = train_formula, data = training_data, num.trees = 100, mtry = 4, importance = "impurity", replace = TRUE, probability = TRUE)

# test con testing_data
predictions_rand_forest <- predict(forest,data=testing_data)$predictions
accuracy <- mean(predictions_rand_forest == testing_data$inclinacion_peligrosa)
print(paste("La precisión del modelo es de:", accuracy))
head(predictions)

# test final con data_test y creación del archivo csv
predictions <- predict(forest, data = data_test)$predictions
head(predictions)
submission <- data.frame(id = data_test$id, inclinacion_peligrosa = predictions[,'1'])
head(submission)
readr::write_csv(submission,"./arbolado-mza-dataset-envio-rf-castinelli7.csv")
