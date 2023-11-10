

def in_danger(row, column, solution):
    for i in range(column):
        
        if solution[i] == None:
            return False
        
        if solution[i] == row or abs(solution[i] - row) == abs(i - column):
            return True # Hay amenaza
    return False # No hay amenaza


states_explored = 0

def n_queens_backtracking(n, column, solution):
  
    global states_explored

    if column == n:

        final_states_explored = states_explored
        states_explored = 0
        return solution, final_states_explored
  
    else:

        for row in range(n):
            states_explored += 1
            if not in_danger(row, column, solution):
                solution[column] = row
                results = n_queens_backtracking(n, column + 1, solution)
                if results is not None:
                    return results
    return None


def n_queens_forward_checking(n, column, solution, domains):
    global states_explored

    if column == n:
        final_states_explored = states_explored
        states_explored = 0
        return solution, final_states_explored
    else:
        for value in domains[column]:
            states_explored += 1
            if not in_danger(value, column, solution):
                solution[column] = value

                # Reduce domains for future columns
                new_domains = reduce_domains(n, column, solution, domains)

                # Use forward checking for the next column
                result = n_queens_forward_checking(n, column + 1, solution, new_domains)

                if result is not None:
                    return result

                # If no solution is found for the current value, backtrack
                solution[column] = None

    return None

def reduce_domains(n, column, solution, domains):
    new_domains = domains.copy()

    for i in range(column + 1, n):
        possible_values = []

        for value in new_domains[i]:
            if not in_danger(value, i, solution):
                possible_values.append(value)

        new_domains[i] = possible_values

    return new_domains