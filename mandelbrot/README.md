fractal_flight.py

Stress-test logic. Pressure-test memory. Expose terminal truth.

This file renders a full-frame animated Mandelbrot zoom using nothing but Python, ANSI escape codes, and raw math. Designed to simulate a floating orbital dive into the complex plane — one character at a time.

It’s not just a visualization.
It’s a testbed for diagnostic tools that validate memory safety, loop performance, and rendering consistency under increasing algorithmic pressure.

Engineering Context:
This demo was engineered to validate components from the edgesight suite, specifically:

▸ Loop-Jammer

Detects infinite or slow-burning logic in loops. Use this demo to trap edge cases like:

non-terminating conditionals under extreme precision

stackless render paths that degrade over time

▸ StackWhisper

Reveals live memory drift across high-framecount cycles. This fractal renderer runs a complex deterministic loop with floating-point sensitivity — ideal for identifying:

frame-by-frame memory leaks

sub-byte divergence in grid buffers

feedback state inconsistencies in terminal overlays

Core Features:

Dynamic center drift: Simulates camera float via sinusoidal orbiting

Exponential zoom: Pressurizes float math over time (deep-zoom stress)

Color + char encoding: Pushes ANSI depth with adaptive brightness

Residual buffer echo: Compares frame-to-frame symbols to expose volatility

No dependencies: Just Python 3.9+ and your terminal


Function Breakdown & Justification:

Every function in fractal_flight.py serves a precise debugging or diagnostic role, chosen specifically to expose behavior under memory strain, logic decay, and frame-to-frame computation.

mandelbrot(cx, cy, depth)
Purpose:
Executes the canonical Mandelbrot iteration loop per pixel.

Why it's here:

Acts as a deterministic, recursive stress loop

Ideal for evaluating how long-term float math evolves in non-linear systems

Exposes edge-case performance drops as depth increases under zoom pressure

This is the core pressure surface for Loop-Jammer.

get_color(i, max_iter)

Purpose: Maps the character density to ANSI 256-color codes based on iteration count.

Why it's here: Converts numerical stress data into visual anomalies

Verifies color rendering consistency across frame deltas

Ensures terminal rendering doesn't drift or bleed due to dirty buffer overlays

Useful for StackWhisper to identify visual-memory misalignment.

update_camera()

Purpose: Moves the fractal center smoothly in a circular orbit.

Why it's here: Simulates motion over time, triggering more reallocation and redraw

Tests whether float-state memory updates leak precision

Ensures buffer-based animation logic doesn’t collapse under trigonometric drift

This is the synthetic motion feed that amplifies rendering instability.

clear() + move_cursor_top()

Purpose:
Manages terminal state without redrawing the whole screen on every frame.

Why it's here: Tracks whether terminal output responds predictably under partial redraw

Tests escape code consistency across 1000+ writes

Simulates "true real-time" redraw without full clears — useful in embedded terminals

Critical for testing rendering performance with minimal flush overhead.

fractal_flight()
Purpose:
Ties everything together — camera control, iterative rendering, and progressive zoom.

Why it's here: This is the loop under test.

It simulates a deep zoom, while increasing iteration depth, mutating scale, and adjusting orbit angle — all while keeping ANSI rendering aligned to buffer state.

If something breaks in:

precision

redraw flicker

symbol density

loop decay

…you’ll see it.

Buffers: iter_grid, value_grid, last_render

Purpose: Three-layer grid system:

iter_grid: tracks when a cell was last iterated

value_grid: stores what character belongs at each cell

last_render: stores what was actually printed last frame

Why it matters: This lets us test residual memory — “did that cell really change?”

Prevents redundant rendering

Perfect for validating delta-print loops (i.e. optimized frame output logic)

These buffers are ground truth for detecting frame mutation vs. frame replacement bugs.

By pushing a Python terminal to zoom, orbit, adapt, and render under pressure, fractal_flight.py forces any debugger or runtime tool to show its hand. If your loop scanner can’t track this, it’s not ready.


Usage

python fractal_flight.py

Works best on Unix terminals or Windows CMD (via os.system('mode'))

You can adjust orbit_speed, zoom_speed, or max_iter to modify complexity

chars is a density string used for mapping escape patterns, tune for resolution fidelity

Application

This is not a game. It’s an interactive runtime analysis tool for verifying:

long-term floating point drift

recursive character mutation

rendering loop safety

Use it to validate whether your tooling survives a real stress loop — not just a clean test suite.