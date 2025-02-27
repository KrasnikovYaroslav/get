import RPi.GPIO as RT
import time


def dec_to_bin_list(num):

    ans = [int(i) for i in bin(num)[2:]]
    while len(ans) < 8:
        ans.insert(0, 0)

    return ans


try:

    dac = [26, 19, 13, 6, 5, 11, 9, 10]
    RT.setmode(RT.BCM)
    RT.setup(dac, RT.OUT)
    t = int(input())

    delta = 1
    i = 0
    while 1:

        listed = dec_to_bin_list(i)
        RT.output(dac, listed)

        i += delta

        if i == 0:
            delta = 1
        if i == 255:
            delta = -1
        
        time.sleep(float(t)/2/256)
        

        




finally:

    RT.output(dac, [0, 0, 0, 0, 0, 0, 0, 0])
    RT.cleanup()
    
