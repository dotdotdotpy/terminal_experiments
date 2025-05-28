# Neural Rain - A Terminal Renderer That Went Too Far

What started as a quick experiment in curses-based terminal animation spiraled into a deeply optimized, surgically chaotic renderer—one that doesn't fake the Matrix rain effect, but **emulates the underlying logic of it**.

This isn't your average matrix.py script. This is glyph choreography.

---

## A Project That Escalated

The idea was simple: stream random characters down terminal columns. But the moment we treated the terminal like a **pixel shader** with spatial constraints, everything broke—and that’s where the obsession started.

How do you:
- Keep glyph spacing pixel-perfect on terminals that lie about their width?
- Prevent overdraw while spawning new trails unpredictably?
- Build glow, contrast, entropy, and emergent behavior **without using graphics**?

What you’re seeing is the result of going way too far down that rabbit hole.

---

## Feature Overview

### Pure Logic-Driven Trails

- Trail length is **weighted** using `trail_length_weights`
- Spacing is configurable per column
- Columns unlock gradually to prevent burst clumping

### Darter Streams

- Random short trails at high velocity
- Chaos without disrupting the flow

### Head Glow, Mid-Fade, Tail Decay

- Color values are tuned like a shader gradient
- The `head` isn’t just a character—it’s a **pulse**

### Ghost Fragments

- Trails that disappear sometimes leave behind **afterimages**
- These ghost glyphs decay on a timer or are erased by future streams
- Their length is weighted (`ghost_length_weights`) and variably aligned

### Blink & Flash Logic

- Heads flash on an interval
- Random flashes across the grid give life to mid sections
- Mutation chance simulates glyphs flickering or corrupting

### Full External Config

- All weights, glyphs, speeds, and colors are tweakable
- Easily shrink or expand view width for performance tuning
- Looks great even at 30fps, but defaults to 45 for fluidity

---

## The Terminal As Canvas

This isn’t "print a list of characters and clear the screen." This is stacked conditional logic wrapped around spacing-based rendering buffers.

The key innovations:

- **Ghost glyph collision checks** with active stream positions
- Streams only render if they haven’t recently spawned in the same column
- Ghosts persist based on TTL, but are erased if a stream passes over
- Stream heads flash, but the mid color fades into the tail smoothly

It’s all chaos—but tuned chaos. There’s no central controller. No render loop. It’s just entropy with probabilities and constraints. That’s what makes it beautiful.

---

## Want to Customize?

Open the embedded `config` dict at the top of the file and change:
- `trail_length_weights`: adjust probability curve of tail lengths
- `ghost_length_weights`: bias ghost fragments to be longer/shorter
- `darter_chance`: add more chaos
- `colors`: ANSI color codes (0–255) for tail, mid, head

---

## Final Words

This renderer was built for one thing: to feel **alive**.

Sometimes two ghost glyphs align by accident and look like memory artifacts. Sometimes a stream disappears just as it’s about to override a ghost, and a new one lingers in the same place. Sometimes the terminal isn’t a renderer—it’s a **machine that remembers**.

And when it all syncs up for just a second? 
It doesn't look coded. It looks **haunted.**

> **One script. No shaders. Pure control.**

---

Enjoy it. Break it. Fork it. Just don’t underestimate what a terminal can become.