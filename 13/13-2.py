from itertools import product
import re
from sympy import symbols, Eq, solve

def read_input(file_name):
    with open(file_name, 'r') as file:
        blocks = file.read().strip().split('\n\n')  # Split on double newlines
    machines = []
    for block in blocks:
        lines = block.split('\n')
        button_a = list(map(int, re.findall(r"[-\d]+", lines[0]))) # + indicates that the preceding pattern (the character set [-\d]) must appear one or more times.
        button_b = list(map(int, re.findall(r"[-\d]+", lines[1])))
        prize = list(map(int, re.findall(r"[-\d]+", lines[2])))
        machines.append((button_a, button_b, prize))
    return machines

def solve_linear_equations(a_x, a_y, b_x, b_y, p_x, p_y):
    A, B = symbols('A B', integer=True)
    eq1 = Eq(a_x * A + b_x * B, 10000000000000+p_x)
    eq2 = Eq(a_y * A + b_y * B, 10000000000000+p_y)

    solutions = solve((eq1, eq2), (A, B), dict=True)
    valid_costs = []
    for sol in solutions:
        a_presses = sol[A]
        b_presses = sol[B]
        if a_presses >= 0 and b_presses >= 0:  # Ensure non-negative solutions
            cost = 3 * a_presses + b_presses
            valid_costs.append(cost)

    return min(valid_costs) if valid_costs else None

def calculate_total_min_cost(file_name):
    machines = read_input(file_name)
    total_cost = 0
    prizes_won = 0

    for button_a, button_b, prize in machines:
        a_x, a_y = button_a
        b_x, b_y = button_b
        p_x, p_y = prize

        min_cost = solve_linear_equations(a_x, a_y, b_x, b_y, p_x, p_y)
        if min_cost is not None:
            total_cost += min_cost
            prizes_won += 1

    return prizes_won, total_cost

if __name__ == "__main__":
    input_file = "input.txt"
    prizes, total_cost = calculate_total_min_cost(input_file)
    print(f"Maximum prizes won: {prizes}")
    print(f"Minimum total cost: {total_cost}")
