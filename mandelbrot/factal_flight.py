import os
import sys
import time
import math


if os.name == 'nt':
    import ctypes
    os.system("mode con: cols=200 lines=70")
    ctypes.windll.user32.SetWindowPos(ctypes.windll.kernel32.GetConsoleWindow(), None, 100, 5, 0, 0, 0x0001)


# Configuration
height, width = 60, 200
chars = ' .,:;irsXA253hMHGS#9B&@'

# Spiral center anchor (static orbit base)
base_x = -0.102
base_y =  0.652
initial_scale = 0.005

# Flight behavior
max_iter = 10
max_allowed_iter = 400
orbit_speed = 0.00
orbit_radius = 0.0025
zoom_speed = .97
frame_delay = 0.05

# Internal orbit tracker
angle = 0.0
center_x = base_x
center_y = base_y

# Buffers
iter_grid = [[0 for _ in range(width)] for _ in range(height)]
value_grid = [[' ' for _ in range(width)] for _ in range(height)]
last_render = [[' ' for _ in range(width)] for _ in range(height)]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def move_cursor_top():
    sys.stdout.write("\033[H")

def mandelbrot(cx, cy, depth):
    z = 0
    for i in range(depth):
        z = z * z + complex(cx, cy)
        if abs(z) > 2:
            return i
    return depth

def get_color(i, max_iter):
    if i == max_iter:
        return "\033[38;5;16m"  # black
    color_idx = 16 + int(i * 215 / max_iter)
    return f"\033[38;5;{color_idx}m"

def update_camera():
    global center_x, center_y, initial_scale, angle
    angle += orbit_speed
    center_x = base_x + math.cos(angle) * orbit_radius
    center_y = base_y + math.sin(angle) * orbit_radius
    initial_scale *= zoom_speed

def fractal_flight():
    global max_iter
    clear()
    move_cursor_top()

    for step in range(1, max_allowed_iter + 1):
        if max_iter < max_allowed_iter:
            max_iter += 1

        update_camera()
        move_cursor_top()
        output = []

        for y in range(height):
            row = []
            for x in range(width):
                dx = (x - width / 2) * initial_scale
                dy = (y - height / 2) * initial_scale * 1.0  # spiral-preserving
                cx = center_x + dx
                cy = center_y + dy

                if iter_grid[y][x] < max_iter:
                    i = mandelbrot(cx, cy, max_iter)
                    iter_grid[y][x] = max_iter
                    ch = chars[min(i * len(chars) // max_iter, len(chars) - 1)]
                    value_grid[y][x] = ch

                ch = value_grid[y][x]
                prev = last_render[y][x]
                last_render[y][x] = ch

                if ch != prev and prev != ' ':
                    display = "\033[38;5;229m*\033[0m"
                else:
                    color = get_color(chars.index(ch), len(chars))
                    display = f"{color}{ch}\033[0m"

                row.append(display)
            output.append(''.join(row))

        sys.stdout.write('\n'.join(output))
        sys.stdout.write(
            f"\n\n[step: {step}, iter: {max_iter}, scale: {initial_scale:.10f}, cx: {center_x:.10f}, cy: {center_y:.10f}]"
        )
        sys.stdout.flush()
        time.sleep(frame_delay)

fractal_flight()
