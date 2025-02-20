import RPi.GPIO as RT
import time

leds = [2, 3, 4, 17, 27, 22, 10, 9]
aux = [21, 20, 26, 16, 19, 25, 23, 24]

RT.setmode(RT.BCM)

RT.setup(leds, RT.OUT)
RT.setup(aux, RT.IN)

while True:
    for i in range(8):
        RT.output(leds[i], RT.input(aux[i]))

RT.output(leds, 0)
RT.cleanup()