# **Inteligencia Artificial I**

## **UNCuyo - Facultad de Ingeniería**

## **Trabajo Práctico 2 - Agentes Racionales.**

**Resultados de los agentes:**

    library(readr)
    path<-"agent_results.csv"
    agents_df <- read_csv(path)

    ## Rows: 120 Columns: 2
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (1): Agente
    ## dbl (1): Nodos explorados
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

    agents_df

    ## # A tibble: 120 × 2
    ##    Agente     `Nodos explorados`
    ##    <chr>                   <dbl>
    ##  1 Agente BFS               3385
    ##  2 Agente BFS               3390
    ##  3 Agente BFS               3370
    ##  4 Agente BFS               3397
    ##  5 Agente BFS               3351
    ##  6 Agente BFS               3386
    ##  7 Agente BFS               3377
    ##  8 Agente BFS               3386
    ##  9 Agente BFS               3358
    ## 10 Agente BFS               3353
    ## # ℹ 110 more rows

    bfs_df <- subset(agents_df, Agente == "Agente BFS")
    dfs_df <- subset(agents_df, Agente == "Agente DFS")
    lds_df <- subset(agents_df, Agente == "Agente LDS")
    ucs_df <- subset(agents_df, Agente == "Agente UCS")

-   Agente BFS:

Media:

    media_bfs <- mean(bfs_df$`Nodos explorados`, na.rm = TRUE)
    media_bfs

    ## [1] 3381.233

Desviación estándar:

    sd_bfs <- sd(bfs_df$`Nodos explorados`, na.rm = TRUE)
    sd_bfs

    ## [1] 67.48828

Cuadro total:

    bfs_df

    ## # A tibble: 30 × 2
    ##    Agente     `Nodos explorados`
    ##    <chr>                   <dbl>
    ##  1 Agente BFS               3385
    ##  2 Agente BFS               3390
    ##  3 Agente BFS               3370
    ##  4 Agente BFS               3397
    ##  5 Agente BFS               3351
    ##  6 Agente BFS               3386
    ##  7 Agente BFS               3377
    ##  8 Agente BFS               3386
    ##  9 Agente BFS               3358
    ## 10 Agente BFS               3353
    ## # ℹ 20 more rows

-   Agente DFS:

Media:

    media_dfs <- mean(dfs_df$`Nodos explorados`, na.rm = TRUE)
    media_dfs

    ## [1] 2448.467

Desviación estándar:

    sd_dfs <- sd(dfs_df$`Nodos explorados`, na.rm = TRUE)
    sd_dfs

    ## [1] 2010.73

Cuadro total:

    dfs_df

    ## # A tibble: 30 × 2
    ##    Agente     `Nodos explorados`
    ##    <chr>                   <dbl>
    ##  1 Agente DFS                215
    ##  2 Agente DFS               2925
    ##  3 Agente DFS               3776
    ##  4 Agente DFS               3901
    ##  5 Agente DFS                467
    ##  6 Agente DFS               3012
    ##  7 Agente DFS               3931
    ##  8 Agente DFS                 53
    ##  9 Agente DFS                139
    ## 10 Agente DFS                 73
    ## # ℹ 20 more rows

-   Agente LDS:

Media:

    media_lds <- mean(lds_df$`Nodos explorados`, na.rm = TRUE)
    media_lds

    ## [1] 3364.367

Desviación estándar:

    sd_lds <- sd(lds_df$`Nodos explorados`, na.rm = TRUE)
    sd_lds

    ## [1] 2381.938

Cuadro total:

    lds_df

    ## # A tibble: 30 × 2
    ##    Agente     `Nodos explorados`
    ##    <chr>                   <dbl>
    ##  1 Agente LDS               6084
    ##  2 Agente LDS               4257
    ##  3 Agente LDS               3866
    ##  4 Agente LDS               3654
    ##  5 Agente LDS               3699
    ##  6 Agente LDS               3908
    ##  7 Agente LDS               4045
    ##  8 Agente LDS                 57
    ##  9 Agente LDS               3986
    ## 10 Agente LDS                 73
    ## # ℹ 20 more rows

-   Agente UCS:

Media:

    media_ucs <- mean(ucs_df$`Nodos explorados`, na.rm = TRUE)
    media_ucs

    ## [1] 3495.367

Desviación estándar:

    sd_ucs <- sd(ucs_df$`Nodos explorados`, na.rm = TRUE)
    sd_ucs

    ## [1] 62.00472

Cuadro total:

    ucs_df

    ## # A tibble: 30 × 2
    ##    Agente     `Nodos explorados`
    ##    <chr>                   <dbl>
    ##  1 Agente UCS               3489
    ##  2 Agente UCS               3490
    ##  3 Agente UCS               3470
    ##  4 Agente UCS               3514
    ##  5 Agente UCS               3469
    ##  6 Agente UCS               3495
    ##  7 Agente UCS               3481
    ##  8 Agente UCS               3484
    ##  9 Agente UCS               3462
    ## 10 Agente UCS               3459
    ## # ℹ 20 more rows
