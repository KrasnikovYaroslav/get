import RPi.GPIO as RT


def dec_to_bin_list(num):

    ans = [int(i) for i in bin(num)[2:]]
    while len(ans) < 8:
        ans.insert(0, 0)

    return ans


try:

    dac = [26, 19, 13, 6, 5, 11, 9, 10]
    RT.setmode(RT.BCM)
    RT.setup(dac, RT.OUT)
    
    port = int(input("Enter port: "))
    frequency = 1
    RT.setup(port, RT.OUT)
    pwm = RT.PWM(port, frequency)

    duty = 0.0
    pwm.start(duty)


    while 1:
        

        frequency, duty = map(float, input("Enter frequency and duty: ").split())
        pwm.ChangeFrequency(frequency)
        pwm.ChangeDutyCycle(duty)
        print("Expected voltage: ", duty * 3.3 / 100)


finally:

#    RT.output(dac, [0, 0, 0, 0, 0, 0, 0, 0])
    RT.cleanup()
    
