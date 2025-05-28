# Coming Soon: Neural Rain Evolution Roadmap

![Neural Rain Demo](neural_rain/demo.gif)

## Planned Features

We're just getting started. Here’s what’s cooking for future updates to Neural Rain:

---

### Smarter Glyph Dynamics

- Entire strings may **randomly mutate** over time.
- Or, **individual characters** may change within a string for glitchy, alive behavior.

---

### Pulse Effects

- Random **single**, **double**, or **triple** character pulses will flash on screen.
- Adds a sense of glow, interactivity, and breathing motion across the matrix.

---

### String Collision Logic

- Multiple streams may **spawn in the same column**.
- Strings will:
  - **Catch up** to other strings and collide.
  - Either **override**, **blend**, or **get rejected** based on context.
  - Introduce **competition**, **domination**, and **persistence** into flow mechanics.

---

## Performance Optimization (Inspired by DOM Timewarp, coming soon!)

Eventually, we plan to **break the ANSI bottleneck** the same way we can decouple DOM bottlenecks in advanced visualizations.

We’ll build a **pre-rendered canvas state engine** where:
- Every frame is **calculated in advance** and **stored in a virtual buffer**, not rendered directly to screen until needed.
- This means:
  - All string logic and glyph states are solved **off-screen**.
  - The console output becomes a pure **render shell**, only displaying the pre-solved visuals.
  - We can inject frames **as batches**, bypassing laggy real-time computations.

Think of it like:

> "Freezing the frame logic in time, so the terminal just plays catch-up."

This lays the groundwork for:

- **Fullscreen support**
- **Smooth motion math**
- **Huge glyph counts**
- **Zero performance compromise**

---

### Call for Suggestions

Got a crazy idea? Visual glitch? Edge effect?  

**Submit it.**

> I will ABSOLUTELY spend days rabbit-holing to make it real.

Let’s push terminal animation to its aesthetic and technical limits.

— Stay tuned.  
