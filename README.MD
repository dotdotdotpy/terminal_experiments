# terminal_experiments

A curated suite of logic-dense terminal demos — visual algorithms, waveform renderers, and stress-tested diagnostics built in raw Python.

Minimal dependencies. Maximal entropy.  
Experimental. Clean. Weird on purpose.

---

## Overview

This repo contains three specialized submodules:

### ▸ `console_demo/`

**Interactive audiovisual demo suite.**  
Terminal-native animations synced to live procedural audio. Each function is a standalone visual effect rendered entirely in ASCII, paired with a waveform synthesized in real time.

**Highlights:**

- Frame-accurate audio-visual sync
- Procedural rendering (no external assets)
- Uses ANSI cursor targeting for clean redraw

See [`console_demo/demo_suite.py`](console_demo/demo_suite.py)

---

### ▸ `longform/`

**Minimal-line density studies.**  
Each function is designed to compress complex logic — fractal math, waveform simulation, and recursive symmetry — into an atomic render unit, often in one line or less.

These are not animations. These are field equations rendered in characters.

**Key functions:**

- `plasma_bloom_vortex()`
- `reactor_burst()`
- `waveform_glitch()`
- `electromagnetic_bloomwave()`

See [`longform/longform_one_liners.py`](longform/longform_one_liners.py)

---

### ▸ `mandelbrot/`

**Fractal stress testing for loop safety and memory volatility.**  
This script renders a full-frame Mandelbrot zoom with orbital camera drift and exponential float pressure — designed to validate stack-aware diagnostic tooling like `Loop-Jammer` and `StackWhisper`.

Use it to track:

- Frame-to-frame terminal fidelity  
- Recursive loop stability under zoom pressure  
- Character buffer misalignment or residual overwrites  
- Runtime float decay and redraw precision

See [`mandelbrot/factal_flight.py`](mandelbrot/factal_flight.py)

### ▸ `neural_rain.py`

**Matrix-style curses engine with ghost trails and entropy logic.**  
This one-script renderer simulates glyph decay, head pulses, blinking trails, and probabilistic ghost glyphs — all while using zero shaders and full configurability.

Key features:
- Weight-driven trail and ghost lengths
- Flash and fade logic tied to frame intervals
- Ghost glyphs linger and are purged by active stream heads
- Pure terminal, no graphics — just logic, spacing, and entropy

See [`neural_rain/neural_rain.py`](neural_rain/neural_rain.py)

![Neural Rain Demo](neural_rain/demo.gif)


---

## Dependencies


pip install numpy sounddevice


Sound playback is used in console_demo for real-time waveform feedback. All rendering is performed via standard output — no GUI framework required.

Run Examples

python console_demo/demo_suite.py
python longform/longform_one_liners.py
python mandelbrot/factal_flight.py

Use Cases

Terminal-based audio-visual synthesis

Loop pressure diagnostics

Memory visualization experiments

Runtime stability testing

Code obfuscation art / one-liner compression challenges

Philosophy
This project was built as an engineering playground — a place to test terminal performance, rendering math, buffer feedback systems, and the boundaries of what's possible with ASCII and print().

Each file stands on its own. Each function has intention.

This isn’t a product. It’s a toolkit for understanding the machine.

License
MIT — use freely, break beautifully, contribute if you build something weirder.