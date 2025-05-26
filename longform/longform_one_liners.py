import os, time, math, cmath, numpy as np

def plasma_bloom_vortex():
    print("\n[plasma_bloom_vortex] Executing radial plasma logic core...\n")
    [print(''.join(" .:-=+*#%@"[int(((math.sin(x*x*0.01 + y*y*0.01 + time.time()) + math.cos(x*0.15 + y*0.25 + time.time()*0.7)) * 4) % 10)] for x in range(-40, 40))) for y in range(-12, 12)]

def sine_storm():
    print("\n[sine_storm] Simulating atmospheric logic pressure...\n")
    [print(''.join(["-$=~"[(int(math.sin(x/5 + time.time()*2 + y*y*0.005)*3)+3)%4] for x in range(80)])) or time.sleep(0.02) for y in range(60)]

def reactor_burst():
    print("\n[reactor_burst] Generating particle impact signature...\n")
    print('\n'.join([''.join(['*#%@$'[int((math.sin(math.hypot(x,y)+time.time()*3)+1)*2.5)%5] for x in range(-30,30)]) for y in range(-15,15)]))

def waveform_glitch():
    print("\n[waveform_glitch] Outputting logical oscillation entropy...\n")
    [print(''.join(['~-'[(int(sum(math.sin((x*y + t*10)/10.0 + c) for c in range(3)))%2)] for x in range(100)])) or time.sleep(0.01) for y in range(60) for t in [time.time()]]

def symmetry_bloom():
    print("\n[symmetry_bloom] Calculating inverted twin matrices...\n")
    [print(''.join([chr(9608) if (x*x + y*y) % 13 == 0 else ' ' for x in range(-30, 30)])) for y in range(-15,15)]

def chromatic_cascade_bleed():
    print("\n[#6 chromatic_cascade_bleed] Phase lattice ignited...\n")
    for y in range(-22, 22):
        print(''.join([' .:-=+*#%@'[int((math.sin((x**2 + y**2)**0.5*0.12 - time.time()*3) + 1) * 5) % 10] for x in range(-44, 44)]))
    time.sleep(0.6)

def binary_warp_gate():
    print("\n[#7 binary_warp_gate] Stabilizing threshold band...\n")
    for y in range(-22, 22):
        print(''.join([' .oO@#*+=:'[int((math.sin(x*0.3) + math.sin(y*0.2 + time.time()*2)) * 4.5) % 10] for x in range(-44, 44)]))
    time.sleep(0.6)

def particle_shell_echo():
    print("\n[#8 particle_shell_echo] Orbital shell rotating...\n")
    for y in range(-22, 22):
        print(''.join([' .x+=*#%@$'[int(((math.sin(x*0.1 + time.time())**2 + math.cos(y*0.1 - time.time()*1.3)**2) * 4) % 10)] for x in range(-44, 44)]))
    time.sleep(0.6)

def sinefold_collapse():
    print("\n[#9 sinefold_collapse] Gridline pulse disrupted...\n")
    for y in range(-22, 22):
        print(''.join([' .:-=+*#%@$'[int(abs(math.sin((x*0.15)**2 + (y*0.15)**2 - time.time()*2)) * 10) % 10] for x in range(-44, 44)]))
    time.sleep(0.6)

def electromagnetic_bloomwave():
    print("\n[#10 electromagnetic_bloomwave] Bloomwave resonance surge...\n")
    for y in range(-22, 22):
        print(''.join([' .:=-+*#%@'[int(((math.sin((x**2 + y**2)*0.005 - time.time()*3) + 1) * 5) % 10)] for x in range(-44, 44)]))
    time.sleep(0.6)

if __name__ == "__main__":
    plasma_bloom_vortex()
    time.sleep(0.5)
    sine_storm()
    time.sleep(0.5)
    reactor_burst()
    time.sleep(0.5)
    waveform_glitch()
    time.sleep(0.5)
    symmetry_bloom()
    chromatic_cascade_bleed()
    time.sleep(0.3)
    binary_warp_gate()
    time.sleep(0.3)
    particle_shell_echo()
    time.sleep(0.3)
    sinefold_collapse()
    time.sleep(0.3)
    electromagnetic_bloomwave()
