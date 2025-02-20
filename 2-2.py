import RPi.GPIO as RT
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
num = [0, 1, 1, 1, 0, 0, 1, 1]
#      7  6  5  4  3  2  1  0

RT.setmode(RT.BCM)
RT.setup(dac, RT.OUT)

RT.output(dac, num)

time.sleep(20)

RT.output(dac, 0)

RT.cleanup()