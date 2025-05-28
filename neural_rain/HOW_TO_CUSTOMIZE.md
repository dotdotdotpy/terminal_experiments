# HOW TO CUSTOMIZE Neural Rain

![Neural Rain Demo](neural_rain/demo.gif)

This guide explains all tunable settings in the `config` dictionary and the script itself for customizing your Neural Rain terminal renderer.

---

## Config Dictionary Options

### `spacing`
Controls horizontal distance between stream columns. Default: `3`. Lower values = denser rain.

### `frame_rate`
Controls frames per second. Higher = smoother motion. Default: `45`.

### `linger_chance`
Percent chance (0–100) that a stream leaves behind ghost fragments instead of rendering. Default: `8`.

### `max_streams_per_column`
Limits the number of concurrent streams per column. Default: `1`.

### `trail_length_weights`
Weight-based random selection for stream trail lengths. Dict key = length, value = weight.

### `ghost_length_weights`
Same as above but for ghost fragment trails.

### `darter_chance`
Chance for a trail to be a “darter” (shorter, faster). Default: `0.08`.

### `darter_speed_range` / `normal_speed_range`
Defines update speed range (in seconds) for darters and regular trails respectively.

### `spawn_spacing_range`
Min and max vertical space required between new spawns in the same column. Default: `[4, 10]`.

### `glyphs`
String of characters that can be rendered in the rain. Customizable.

### `colors`
ANSI 256-color codes for:
- `tail` (longest faded end)
- `mid` (middle segments)
- `head` (brightest top character)

---

## Hardcoded Constants

### `mutation_chance`
Chance a glyph randomly changes each frame. Default: `0.004`.

### `blink_chance`
Chance that a mid-stream glyph skips rendering (to simulate glitch/flicker). Default: `0.08`.

### `head_blink_interval`
Interval (in seconds) used to pulse heads on/off. Default: `0.8`.

### `random_flash_chance`
Controls how often random glyphs flash. Default: `0.05`.

---

## Terminal Expansion Controls

### `EXTRA_COLUMNS`
Appends additional columns to the right side of the screen. Default: `5`. Raises horizontal capacity.

### `EXTRA_ROWS`
Adds more rows to the terminal height. Default: `5`. Expands vertical range.

> These are useful for stabilizing edge flicker or simulating overflow. Adjust with cuation.

---

## Summary

All of these can be tuned live in the script. For easy configuration, the `config` dictionary is placed at the top.

Have fun creating your own signature rain behavior.