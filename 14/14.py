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
    positions = {}
    for x, y, v_x, v_y in robots:
        new_x = (x + v_x * time) % width
        new_y = (y + v_y * time) % height
        if (new_x, new_y) not in positions:
            positions[(new_x, new_y)] = 0
        positions[(new_x, new_y)] += 1
    return positions

def split_and_count(positions):
    quadrants = {
        "top_left": 0,
        "top_right": 0,
        "bottom_left": 0,
        "bottom_right": 0
    }

    for (x, y), count in positions.items():
        if x == 50 or y == 51:  # Filter out middle positions
            continue
        if x < 50 and y < 51:
            quadrants["top_left"] += count
        elif x < 50 and y > 51:
            quadrants["bottom_left"] += count
        elif x > 50 and y < 51:
            quadrants["top_right"] += count
        elif x > 50 and y > 51:
            quadrants["bottom_right"] += count

    return quadrants

def calculate_safety_factor(file_name):
    robots = read_input(file_name)
    positions = calculate_positions(robots, 100, 101, 103)  # 100 seconds, width=101, height=103
    quadrants = split_and_count(positions)
    safety_factor = (quadrants["top_left"] * quadrants["top_right"] *
                     quadrants["bottom_left"] * quadrants["bottom_right"])
    return safety_factor

if __name__ == "__main__":
    input_file = "input.txt"
    safety_factor = calculate_safety_factor(input_file)
    print(f"Safety Factor: {safety_factor}")
