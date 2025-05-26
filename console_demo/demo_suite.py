import os
import time
import math
import numpy as np
import sounddevice as sd
import sys  

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    sys.stdout.write("\033[H\033[J")
    sys.stdout.flush()

def visual_tunnel():
    frames = ["[    ]", "[==  ]", "[====]", "[  ==]", "[    ]", "[ >> ]", "[>>>>]", "[ >> ]", "[    ]"]
    height = 24

    print('\n'.join([' ' * 80 for _ in range(height)]))

    for _ in range(4):
        for frame in frames:
            for i in range(height):
                sys.stdout.write(f"\033[{i+1};1H{frame * 18}")
            sys.stdout.flush()
            time.sleep(0.1)

    sys.stdout.write('\033[H')
    sys.stdout.flush()


def wiggle_matrix():
    charset = '#$@%&=+-_<>!?~'
    height = 24
    width = 100
    frames = 100

    print('\n'.join([' ' * width for _ in range(height)]))
    
    for _ in range(frames):
        for i in range(height):
            line = ''.join(np.random.choice(list(charset)) for _ in range(width))
            sys.stdout.write(f"\033[{i+1};1H{line}")
        sys.stdout.flush()
        time.sleep(0.02)

    sys.stdout.write('\033[H' + '\n'.join([' ' * width for _ in range(height)]))
    sys.stdout.flush()


def ascii_fractal():
    chars = '.:=+*#%@'
    height, width = 24, 80
    frame = []

    for y in range(-height//2, height//2):
        row = ''
        for x in range(-width//2, width//2):
            c = complex(x / 20.0, y / 10.0)
            z = 0
            i = 0
            while abs(z) <= 2 and i < 30:
                z = z * z + c
                i += 1
            row += chars[i % len(chars)]
        frame.append(row)

    clear_screen()
    sys.stdout.write('\n'.join(frame))
    sys.stdout.flush()
    time.sleep(3.8)


def radial_hypnoscan(frames=40):
    charset = ' .:-=+*#%@'
    clear_screen() 

    for _ in range(frames):
        out = []
        for y in range(-22, 22):
            row = ''.join([
                charset[int(((math.sin((x**2 + y**2)**0.5 * 0.15 - time.time() * 4) + 1) * 5) % len(charset))]
                for x in range(-44, 44)
            ])
            out.append(row)

        clear_screen()
        sys.stdout.write('\n'.join(out))
        sys.stdout.flush()
        time.sleep(.07)


def chaotic_string_reactor(frames=40):
    charset = '-~=#%$@'
    for _ in range(frames):
        out = []
        for y in range(-22, 22):
            row = ''.join([charset[int(((math.sin(x*0.1 + time.time()*1.5) + math.sin(y*0.1 - time.time()*2.1)) * 3.5 + 4) % len(charset))] for x in range(-44, 44)])
            out.append(row)
        sys.stdout.write("\033[H" + '\n'.join(out))
        sys.stdout.flush()
        time.sleep(0.1)

def temporal_stream_echo():
    try:
        width, height = 88, 32
        buffer = [' ' * width for _ in range(height)]
        charset = ' .:-=+*#%@'
        for frame in range(75):
            new_buffer = []
            for y in range(height):
                line = ''
                for x in range(width):
                    t = time.time()
                    val = math.sin((x - frame) * 0.1 + t) + math.cos((y + frame) * 0.1 - t)
                    idx = int(abs(val * 4.5)) % len(charset)
                    line += charset[idx]
                new_buffer.append(line)
            for y in range(height):
                echo = buffer[y]
                fresh = new_buffer[y]
                merged = ''.join(
                    fresh[i] if frame % 2 == 0 or echo[i] == ' ' else echo[i]
                    for i in range(width)
                )
                buffer[y] = merged
            sys.stdout.write("\033[H" + '\n'.join(buffer))
            sys.stdout.flush()
            time.sleep(0.05)
    except Exception as e:
        print("[Error in temporal_stream_echo]:", e)

def terminal_gravity_well():
    try:
        w, h = 88, 44
        cx, cy = w // 2, h // 2
        charset = ' .:-=+*#%@'
        for frame in range(150):
            out = []
            for y in range(h):
                line = ''
                for x in range(w):
                    dx = x - cx + math.sin(frame * 0.1) * 5
                    dy = y - cy + math.cos(frame * 0.1) * 5
                    r = math.sqrt(dx**2 + dy**2) + 0.001
                    theta = math.atan2(dy, dx)
                    warped = math.sin(r * 0.15 - frame * 0.1 + math.sin(theta * 3) * 0.5)
                    idx = int(abs(warped * 5)) % len(charset)
                    line += charset[idx]
                out.append(line)
            sys.stdout.write("\033[H" + '\n'.join(out))
            sys.stdout.flush()
            time.sleep(0.04)
    except Exception as e:
        print("[Error in terminal_gravity_well]:", e)

def console_demo_suite():
    print("\n[Console Demo Suite] Initializing...\n")

    sample_rate = 44100
    max_time = 60
    t = np.linspace(0, max_time, int(sample_rate * max_time), endpoint=False)

    def layered_audio(t):
        def kick(t, interval=0.5):
            out = np.zeros_like(t)
            for i in np.arange(0, t[-1], interval):
                idx = (t >= i) & (t < i + 0.5)
                env = np.exp(-60 * (t[idx] - i))
                osc = np.sin(2 * np.pi * 60 * (1 + 6 * (t[idx] - i)) * (t[idx] - i))
                out[idx] += env * osc
            return out

        def bass(t):
            f = 55 * (2 ** (np.floor(t * 2) % 2))
            base = 0.5 * (np.sin(2 * np.pi * f * t) + np.sin(2 * np.pi * (f + 0.8) * t))
            env = np.clip(np.sin(np.pi * t / t[-1]), 0, 1)
            return base * env * 0.6

        def pad(t):
            freqs = [220, 277.18, 329.63]
            chord = sum(np.sin(2 * np.pi * f * t) for f in freqs) / len(freqs)
            slow_env = np.clip((t - 2) / 8, 0, 1) * np.exp(-0.05 * t)
            lfo = 0.8 + 0.2 * np.sin(0.25 * 2 * np.pi * t)
            return chord * slow_env * lfo * 0.5

        def lead(t):
            melody = np.sin(2 * np.pi * 440 * t + 5 * np.sin(2 * np.pi * 0.5 * t))
            gate = ((np.sin(2 * np.pi * 2 * t) > 0).astype(float)) * np.clip((t - 4) / 4, 0, 1)
            return melody * gate * 0.3

        return np.clip(kick(t) + bass(t) + pad(t) + lead(t), -1, 1)

    audio = layered_audio(t)

    print("[Console Demo Suite] Launching audio + visuals...\n")
    sd.play(audio, samplerate=sample_rate)

    start = time.time()

    clear_screen(); visual_tunnel()
    clear_screen(); wiggle_matrix()
    clear_screen(); ascii_fractal()
    clear_screen(); radial_hypnoscan()
    clear_screen(); chaotic_string_reactor()
    clear_screen(); temporal_stream_echo()
    clear_screen(); terminal_gravity_well()

    sd.stop()
    elapsed = time.time() - start
    print(f"\n[Console Demo Suite] Complete. Runtime: {elapsed:.2f}s\n")

console_demo_suite()

