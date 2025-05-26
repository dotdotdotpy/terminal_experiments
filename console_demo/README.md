# Console Demo Suite

A terminal-native audiovisual demo.  
Contains a sequence of animations rendered entirely with ASCII, synced to layered procedural audio.  
Built with no external UI dependencies. Output is confined to the terminal surface.

---

## Overview

This script generates a synchronized audio-visual experience directly in the terminal.  
Each function represents a self-contained animation system or audio component, triggered in sequence.  
Frame control is handled via ANSI escape codes to avoid log clutter or scrollback pollution.

---

## Requirements

- Python 3.7+
- `numpy`
- `sounddevice`


pip install numpy sounddevice
Running the Demo

python demo_suite.py
Terminal must support ANSI escape codes. Audio output will play immediately using default output device.

Function Descriptions:

visual_tunnel()

24-line horizontal animation loop.
Cycles through a predefined sequence of progress-bar styled segments.
Each line is updated independently using ANSI line targeting (\033[{line};1H).

Purpose: Intro calibration / early sync check

Duration: 4 full cycles of 9 frames each

wiggle_matrix()

Generates 24 simultaneous streams of randomized character noise (#$@%&=+-_<>!?~).
Each line independently replaces itself with fresh random characters at every frame.

Purpose: Density test for scroll-safe vertical chaos

Uses: Rapid redraw with no terminal overflow

ascii_fractal()

Renders a static Mandelbrot-like structure using a character ramp.
Executes a fixed-resolution scan over a 2D complex space.

Characters selected based on escape depth from z = z² + c

Renders once, holds for ~3.8s

No animation, just a resolution snapshot

radial_hypnoscan(frames=40)

Draws a real-time circular sine pulse across a 2D matrix.
Each character’s brightness is determined by distance from origin and global time offset.

Effect: Expanding and collapsing concentric rings

Fully rebuilt each frame

Frame delay: 70ms

chaotic_string_reactor(frames=40)

Uses sine-on-sine interference to generate stringy distortions.
Each character is selected by combining phase offsets across X and Y axes.

Feels organic and tangled

Good for showing interaction between waveforms

Uses inline ANSI frame resets for performance

temporal_stream_echo()

Implements a framebuffer-based echo using additive time evolution.
Each new frame is merged into a buffer that keeps select characters from past frames.

Simulates fading trails and ghosting

Alternates between preserving and overwriting pixels

Uses a character ramp for continuous feedback visuals

terminal_gravity_well()

Simulates a radial distortion using polar coordinates.
Each character is placed based on a warped sine of its radius and angular position.

Center spirals inwards

Warping adjusts per frame to simulate collapse

Highest CPU load in the suite

Audio Layer
layered_audio(t)
Produces a real-time waveform built from 4 synchronized components:

kick() – decaying low-end impact every 0.5s

bass() – alternating frequencies every beat, filtered with a sine window

pad() – slow chordal wash with LFO-based brightness

lead() – sine wave lead with vibrato and gated phrasing

Output is streamed at 44100Hz through sounddevice.

Architecture

All frame transitions use ANSI cursor control (\033[{line};1H)

Redraws are line-accurate and do not clear the terminal buffer

Audio is generated as a NumPy waveform and streamed in real time

Script does not rely on any graphical backend or GUI system

Design Goals

Fully terminal-contained visual presentation

Minimal dependencies: no curses, no ncurses, no graphics libraries

Audio synchronized with visuals using procedural timing only

Functions are individually callable and testable in isolation

License

MIT — use freely, adapt as needed.







