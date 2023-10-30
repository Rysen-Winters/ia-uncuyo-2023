# **Inteligencia Artificial I**
## **UNCuyo - Facultad de Ingeniería**

**Resultados de los agentes:**

    library(readr)
    path<-"local_search_results.csv"
    lsearch_df <- read_csv(path)

    ## Rows: 450 Columns: 5
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (1): Algoritmo
    ## dbl (3): Cantidad de reinas, Tiempo de ejecucion, Numero de soluciones explo...
    ## lgl (1): Solucion encontrada
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

    lsearch_df

    ## # A tibble: 450 × 5
    ##    Algoritmo   `Cantidad de reinas` `Tiempo de ejecucion` Numero de soluciones…¹
    ##    <chr>                      <dbl>                 <dbl>                  <dbl>
    ##  1 Hill Climb…                    4                     0                      3
    ##  2 Hill Climb…                    4                     0                      1
    ##  3 Hill Climb…                    4                     0                      3
    ##  4 Hill Climb…                    4                     0                      3
    ##  5 Hill Climb…                    4                     0                      2
    ##  6 Hill Climb…                    4                     0                      3
    ##  7 Hill Climb…                    4                     0                      3
    ##  8 Hill Climb…                    4                     0                      4
    ##  9 Hill Climb…                    4                     0                      2
    ## 10 Hill Climb…                    4                     0                      2
    ## # ℹ 440 more rows
    ## # ℹ abbreviated name: ¹​`Numero de soluciones exploradas`
    ## # ℹ 1 more variable: `Solucion encontrada` <lgl>

    hc_df <- subset(lsearch_df, Algoritmo == "Hill Climbing")
    sa_df <- subset(lsearch_df, Algoritmo == "Simulated Annealing")
    ga_df <- subset(lsearch_df, Algoritmo == "Genetic Algorithm")
    path2<-"local_search_variability.csv"
    variability_df <- read_csv(path2)

    ## Rows: 50249 Columns: 3
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (1): Algoritmo
    ## dbl (2): Numero de estado, Valores de h
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

    hc_var_df <- subset(variability_df, Algoritmo == "Hill Climbing")
    sa_var_df <- subset(variability_df, Algoritmo == "Simulated Annealing")
    ga_var_df <- subset(variability_df, Algoritmo == "Genetic Algorithm")
    variability_df

    ## # A tibble: 50,249 × 3
    ##    Algoritmo           `Numero de estado` `Valores de h`
    ##    <chr>                            <dbl>          <dbl>
    ##  1 Hill Climbing                        0             15
    ##  2 Hill Climbing                        1             10
    ##  3 Hill Climbing                        2              7
    ##  4 Hill Climbing                        3              5
    ##  5 Hill Climbing                        4              3
    ##  6 Hill Climbing                        5              3
    ##  7 Simulated Annealing                  0             15
    ##  8 Simulated Annealing                  1             16
    ##  9 Simulated Annealing                  2             13
    ## 10 Simulated Annealing                  3             16
    ## # ℹ 50,239 more rows

-   Hill Climbing:

Porcentaje de veces que encontró la solución final

    porcentaje_true_hc <- mean(hc_df$'Solucion encontrada') * 100
    porcentaje_true_hc

    ## [1] 14

Media de tiempo de ejecucion:

    media_exec_hc <- mean(hc_df$`Tiempo de ejecucion`, na.rm = TRUE)
    media_exec_hc

    ## [1] 0.004822159

Desviación estándar del tiempo de ejecucion:

    sd_exec_hc <- sd(hc_df$`Tiempo de ejecucion`, na.rm = TRUE)
    sd_exec_hc

    ## [1] 0.006641131

Media de estados explorados:

    media_states_hc <- mean(hc_df$`Numero de soluciones exploradas`, na.rm = TRUE)
    media_states_hc

    ## [1] 5.006667

Desviación estándar de los estados explorados:

    sd_states_hc <- sd(hc_df$`Numero de soluciones exploradas`, na.rm = TRUE)
    sd_states_hc

    ## [1] 1.961018

    # Supongamos que tienes un vector de valores discretos

    valores_hc <- hc_var_df$`Valores de h`
    # Crea un vector de índices para el eje x
    indices_hc <- seq_along(valores_hc)

    # Grafica los valores
    plot(indices_hc, valores_hc, type = "b", main = "Variación de los valores de h (Hill Climbing)", xlab = "Índice", ylab = "Valor")

![](tp5-reporte_files/figure-markdown_strict/unnamed-chunk-7-1.png)

Cuadro total:

    hc_df

    ## # A tibble: 150 × 5
    ##    Algoritmo   `Cantidad de reinas` `Tiempo de ejecucion` Numero de soluciones…¹
    ##    <chr>                      <dbl>                 <dbl>                  <dbl>
    ##  1 Hill Climb…                    4                     0                      3
    ##  2 Hill Climb…                    4                     0                      1
    ##  3 Hill Climb…                    4                     0                      3
    ##  4 Hill Climb…                    4                     0                      3
    ##  5 Hill Climb…                    4                     0                      2
    ##  6 Hill Climb…                    4                     0                      3
    ##  7 Hill Climb…                    4                     0                      3
    ##  8 Hill Climb…                    4                     0                      4
    ##  9 Hill Climb…                    4                     0                      2
    ## 10 Hill Climb…                    4                     0                      2
    ## # ℹ 140 more rows
    ## # ℹ abbreviated name: ¹​`Numero de soluciones exploradas`
    ## # ℹ 1 more variable: `Solucion encontrada` <lgl>

-   Simulated Annealing:

Porcentaje de veces que encontró la solución final

    porcentaje_true_sa <- mean(sa_df$'Solucion encontrada') * 100
    porcentaje_true_sa

    ## [1] 24

Media del tiempo de ejecucion:

    media_exec_sa <- mean(sa_df$`Tiempo de ejecucion`, na.rm = TRUE)
    media_exec_sa

    ## [1] 0.0008938583

Desviación estándar del tiempo de ejecucion:

    sd_exec_sa <- sd(sa_df$`Tiempo de ejecucion`, na.rm = TRUE)
    sd_exec_sa

    ## [1] 0.002099027

Media de estados explorados:

    media_states_sa <- mean(sa_df$`Numero de soluciones exploradas`, na.rm = TRUE)
    media_states_sa

    ## [1] 142

Desviación estándar de los estados explorados:

    sd_states_sa <- sd(sa_df$`Numero de soluciones exploradas`, na.rm = TRUE)
    sd_states_sa

    ## [1] 0

    # Supongamos que tienes un vector de valores discretos

    valores_sa <- sa_var_df$`Valores de h`
    # Crea un vector de índices para el eje x
    indices_sa <- seq_along(valores_sa)

    # Grafica los valores
    plot(indices_sa, valores_sa, type = "b", main = "Variación de los valores de h (Simulated Annealing)", xlab = "Índice", ylab = "Valor")

![](tp5-reporte_files/figure-markdown_strict/unnamed-chunk-14-1.png)

Cuadro total:

    sa_df

    ## # A tibble: 150 × 5
    ##    Algoritmo   `Cantidad de reinas` `Tiempo de ejecucion` Numero de soluciones…¹
    ##    <chr>                      <dbl>                 <dbl>                  <dbl>
    ##  1 Simulated …                    4              0.000999                    142
    ##  2 Simulated …                    4              0                           142
    ##  3 Simulated …                    4              0.00100                     142
    ##  4 Simulated …                    4              0                           142
    ##  5 Simulated …                    4              0                           142
    ##  6 Simulated …                    4              0.00100                     142
    ##  7 Simulated …                    4              0                           142
    ##  8 Simulated …                    4              0                           142
    ##  9 Simulated …                    4              0                           142
    ## 10 Simulated …                    4              0                           142
    ## # ℹ 140 more rows
    ## # ℹ abbreviated name: ¹​`Numero de soluciones exploradas`
    ## # ℹ 1 more variable: `Solucion encontrada` <lgl>

-   Algoritmo Genético:

Porcentaje de veces que encontró la solución final

    porcentaje_true_ga <- mean(ga_df$'Solucion encontrada') * 100
    porcentaje_true_ga

    ## [1] 62

Media:

    media_exec_ga <- mean(ga_df$`Tiempo de ejecucion`, na.rm = TRUE)
    media_exec_ga

    ## [1] 0.8491872

Desviación estándar:

    sd_exec_ga <- sd(ga_df$`Tiempo de ejecucion`, na.rm = TRUE)
    sd_exec_ga

    ## [1] 1.003862

Media de estados explorados:

    media_states_ga <- mean(ga_df$`Numero de soluciones exploradas`, na.rm = TRUE)
    media_states_ga

    ## [1] 21928.33

Desviación estándar de los estados explorados:

    sd_states_ga <- sd(ga_df$`Numero de soluciones exploradas`, na.rm = TRUE)
    sd_states_ga

    ## [1] 23114.92

    # Supongamos que tienes un vector de valores discretos

    valores_ga <- ga_var_df$`Valores de h`
    # Crea un vector de índices para el eje x
    indices_ga <- seq_along(valores_ga)

    # Grafica los valores
    plot(indices_ga, valores_ga, type = "b", main = "Variación de los valores de h (Genetic Algorithm)", xlab = "Índice", ylab = "Valor")

![](tp5-reporte_files/figure-markdown_strict/unnamed-chunk-21-1.png)

Cuadro total:

    ga_df

    ## # A tibble: 150 × 5
    ##    Algoritmo   `Cantidad de reinas` `Tiempo de ejecucion` Numero de soluciones…¹
    ##    <chr>                      <dbl>                 <dbl>                  <dbl>
    ##  1 Genetic Al…                    4              0                           100
    ##  2 Genetic Al…                    4              0.000999                    200
    ##  3 Genetic Al…                    4              0.00100                     150
    ##  4 Genetic Al…                    4              0.000998                    150
    ##  5 Genetic Al…                    4              0                           100
    ##  6 Genetic Al…                    4              0                           100
    ##  7 Genetic Al…                    4              0.00100                     100
    ##  8 Genetic Al…                    4              0.00101                     150
    ##  9 Genetic Al…                    4              0.00200                     250
    ## 10 Genetic Al…                    4              0.000997                    200
    ## # ℹ 140 more rows
    ## # ℹ abbreviated name: ¹​`Numero de soluciones exploradas`
    ## # ℹ 1 more variable: `Solucion encontrada` <lgl>

### Boxplot

    boxplot(lsearch_df$'Tiempo de ejecucion' ~ lsearch_df$Algoritmo,
            data = lsearch_df,
            main = "Boxplot de Tiempos de ejecucion por Algoritmo",
            xlab = "Algoritmo", ylab = "Tiempo de ejecucion (s)")

![](tp5-reporte_files/figure-markdown_strict/unnamed-chunk-23-1.png)
