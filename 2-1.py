import RPi.GPIO as RT
import time

RT.setmode(RT.BCM)

leds = [2, 3, 4, 17, 27, 22, 10, 9]

for i in leds: RT.setup(i, RT.OUT)

for i in leds: RT.output(i, 0)

time.sleep(0.5)

for _ in range(3):
    for i in leds:
        RT.output(i, 1)
        time.sleep(0.15)
        RT.output(i, 0)

for i in leds: RT.output(i, 0)

RT.cleanup()