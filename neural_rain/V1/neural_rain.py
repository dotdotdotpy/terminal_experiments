import curses, time, random, os

# Embedded config
config = {
    "spacing": 3,
    "view_width": 82,
    "frame_rate": 45,
    "linger_chance": 8,
    "max_streams_per_column": 1,
    "trail_length_weights": {
        "2": 1, "4": 1, "7": 2, "10": 4, "14": 6,
        "18": 7, "22": 6, "26": 5, "30": 4,
        "34": 2, "38": 1
    },
    "ghost_length_weights": {
        "3": 1, "6": 3, "8": 4, "10": 6, "12": 2
    },
    "darter_chance": 0.08,
    "darter_speed_range": [0.03, 0.04],
    "normal_speed_range": [0.045, 0.075],
    "spawn_spacing_range": [4, 10],
    "glyphs": "01|!lI/\\\\-_=+<>[]{}()$%#&*@?~",
    "colors": {
        "tail": 22,
        "mid": 28,
        "head": 82
    }
}

# Base config
spacing = config["spacing"]
frame_time = 1 / config["frame_rate"]
glyphs = list(config["glyphs"])
trail_length_pool = [
    int(length)
    for length, weight in config["trail_length_weights"].items()
    for _ in range(weight)
]
ghost_length_pool = [
    int(length)
    for length, weight in config.get("ghost_length_weights", {}).items()
    for _ in range(weight)
]
spawn_spacing_min, spawn_spacing_max = config["spawn_spacing_range"]
darter_chance = config["darter_chance"]
darter_speed_range = config["darter_speed_range"]
normal_speed_range = config["normal_speed_range"]
colors = config["colors"]
linger_chance = config.get("linger_chance", 0) / 100.0

# Tuning
mutation_chance = 0.004
blink_chance = 0.08
head_blink_interval = 0.8
random_flash_chance = 0.05

# User-specified scale
EXTRA_COLUMNS = 5
EXTRA_ROWS = 10

def run(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(1, colors["tail"], -1)
    curses.init_pair(2, colors["mid"], -1)
    curses.init_pair(3, colors["head"], -1)

    stdscr.timeout(0)

    h, w = stdscr.getmaxyx()
    view_width = w - (w % spacing)
    start_x = (w - view_width) // 2
    cols = list(range(start_x, start_x + view_width, spacing))

    last_col_x = cols[-1] if cols else start_x
    for i in range(1, EXTRA_COLUMNS + 1):
        cols.append(last_col_x + i * spacing)

    view_width += EXTRA_COLUMNS * spacing
    view_height = h
    max_streams = max(1, int(h / 25))

    streams = {x: [] for x in cols}
    spacing_requirements = {x: random.randint(spawn_spacing_min, spawn_spacing_max) for x in cols}
    spawn_queue = cols.copy()
    random.shuffle(spawn_queue)
    unlocked_cols = set()
    unlock_interval = 0.1
    last_unlock_time = time.time()

    ghosts = []

    while True:
        now = time.time()
        stdscr.erase()
        head_blink_phase = int(now / head_blink_interval) % 2 == 0

        if spawn_queue and (now - last_unlock_time) >= unlock_interval:
            unlocked_cols.add(spawn_queue.pop(0))
            last_unlock_time = now

        active_positions = set()

        for x in cols:
            if x not in unlocked_cols:
                continue

            is_darter = random.random() < darter_chance
            speed = random.uniform(*darter_speed_range) if is_darter else random.uniform(*normal_speed_range)
            trail_length = random.choice(trail_length_pool)
            last_head = max((s["head"] for s in streams[x]), default=-9999)

            can_spawn = (
                len(streams[x]) < max_streams if is_darter else
                len(streams[x]) == 0 or
                (len(streams[x]) < max_streams and (last_head + trail_length) >= spacing_requirements[x])
            )

            if can_spawn:
                spacing_requirements[x] = spacing_requirements[x] if is_darter else random.randint(spawn_spacing_min, spawn_spacing_max)
                streams[x].append({
                    "head": random.randint(-trail_length, 0),
                    "speed": speed,
                    "last_update": now,
                    "trail_length": trail_length,
                    "chars": [random.choice(glyphs) for _ in range(trail_length)]
                })

            active_streams = []
            for stream in streams[x]:
                if random.random() < (linger_chance * 0.09):
                    chars = stream["chars"]
                    full_len = len(chars)

                    if full_len > 0:
                        if ghost_length_pool:
                            linger_len = min(random.choice(ghost_length_pool), full_len)
                        else:
                            linger_len = min(5, full_len)

                        for i in range(linger_len):
                            y = stream["head"] - i
                            if 0 <= y < h:
                                ghosts.append({
                                    "x": x,
                                    "y": y,
                                    "ch": chars[i % full_len],
                                    "ttl": 9999
                                })
                    continue

                if now - stream["last_update"] >= stream["speed"]:
                    delta = now - stream["last_update"]
                    steps = int(delta / stream["speed"])
                    stream["head"] += steps
                    stream["last_update"] = now

                if stream["head"] - stream["trail_length"] > view_height:
                    ghost_len = random.randint(1, 8)
                    base_y = stream["head"] - stream["trail_length"]
                    for i in range(ghost_len):
                        ghost_y = base_y + i
                        if 0 <= ghost_y < h:
                            ghosts.append({
                                "x": x,
                                "y": ghost_y,
                                "ch": random.choice(glyphs),
                                "ttl": random.uniform(0.4, 1.5)
                            })
                    continue

                active_streams.append(stream)

                for j in range(stream["trail_length"]):
                    y = stream["head"] - j
                    if not (0 <= y < h):
                        continue

                    active_positions.add((x, y))

                    is_head = (j == 0)
                    if is_head or random.random() < mutation_chance:
                        stream["chars"][j % len(stream["chars"])] = random.choice(glyphs)

                    ch = stream["chars"][j % len(stream["chars"])]
                    should_draw = head_blink_phase if is_head else random.random() > blink_chance

                    if should_draw:
                        attr = (
                            curses.color_pair(3) if is_head else
                            curses.color_pair(3) if random.random() < random_flash_chance else
                            curses.color_pair(2) if j < 4 else
                            curses.color_pair(1)
                        )
                        try:
                            stdscr.addstr(y, x, ch, attr)
                        except curses.error:
                            pass

            streams[x] = active_streams

        new_ghosts = []
        for ghost in ghosts:
            if ghost["ttl"] > 0 and (ghost["x"], ghost["y"]) not in active_positions:
                try:
                    stdscr.addstr(ghost["y"], ghost["x"], ghost["ch"], curses.color_pair(1))
                except curses.error:
                    pass
                ghost["ttl"] -= frame_time
                new_ghosts.append(ghost)
        ghosts = new_ghosts

        stdscr.refresh()
        time.sleep(frame_time)

if __name__ == "__main__":
    try:
        from shutil import get_terminal_size
        terminal_size = os.get_terminal_size()
    except:
        terminal_size = os.terminal_size((120, 40))

    term_cols = terminal_size.columns
    term_lines = terminal_size.lines
    base_width = term_cols - (term_cols % spacing)
    total_width = base_width + (EXTRA_COLUMNS * spacing)
    total_lines = term_lines + EXTRA_ROWS

    if os.name == "nt":
        os.system(f"mode con: cols={total_width} lines={total_lines}")

    curses.wrapper(run)
