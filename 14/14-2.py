from itertools import product
import re
from sympy import symbols, Eq, solve

def read_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    robots = []
    for line in lines:
        match = re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line.strip())
        if match:
            x, y, v_x, v_y = map(int, match.groups())
            robots.append((x, y, v_x, v_y))
    return robots
def calculate_positions(robots, time, width, height):
    positions = set()
    for x, y, v_x, v_y in robots:
        new_x = (x + v_x * time) % width
        new_y = (y + v_y * time) % height
        positions.add((new_x, new_y))
    return positions

def display_positions(positions, width, height):
    grid = [["." for _ in range(width)] for _ in range(height)]
    for x, y in positions:
        grid[y][x] = "$"

    tree_detected = False
    for row in grid:
        line = "".join(row)
        if "$$$$$$$$$$" in line:  # Look for a pattern of 10 consecutive $
            tree_detected = True
        print(line)
    return tree_detected

def find_tree(file_name):
    robots = read_input(file_name)
    width, height = 101, 103
    smallest_area = float("inf")
    best_time = 0

    for time in range(1000000):  # Large upper bound for time
        positions = calculate_positions(robots, time, width, height)
        if display_positions(positions, width, height):
            print(f"Tree found at time: {time}")
            break

if __name__ == "__main__":
    input_file = "input.txt"
    find_tree(input_file)
