import RPi.GPIO as RT
import time
import matplotlib.pyplot as plt

def adc(dac, razr):
    data = [0]*razr

    for i in range(razr):
        data[i] = 1
        RT.output(dac, data)
        time.sleep(0.002)
        if RT.input(comp):
            data[i] = 0
            RT.output(dac, data)
    return bin_list_2_dec(data)

def dec_2_bin_list(num):
    
    ans = [int(i) for i in bin(num)[2:]]
    while len(ans) < 8:
        ans.insert(0, 0)

    return ans

def bin_list_2_dec(data):
    s = ""
    for i in data:
        s += str(i)
    return int(s, 2)


dac = [8, 11, 7, 1, 0, 5, 12, 6]
led = [2, 3, 4, 17, 27, 22, 10, 9]
troyka = 13
comp = 14
maxV = 3.3
razr = 8

RT.setmode(RT.BCM)

RT.setup(troyka, RT.OUT)
RT.setup(comp, RT.IN)
RT.setup(led, RT.OUT)
RT.setup(dac, RT.OUT)

timeData = []
voltData = []

try:
    start = time.time()
    print("charge...")
    RT.output(troyka, 1)
    val = 0

    while val < 0.7 * (2 ** razr):
        val = adc(dac, razr)
        RT.output(led, dec_2_bin_list(val))
        valV = val * maxV / (2**razr)

        print(val)
        print(dec_2_bin_list(val))
        print()

        voltData.append(val)
        timeData.append(time.time() - start)

    RT.output(troyka, 0)
    print("dicharge...")

    while val > 0.02 * (2 ** razr):
        val = adc(dac, razr)
        RT.output(led, dec_2_bin_list(val))
        valV = val * maxV / (2**razr)

        print(val)
        print(dec_2_bin_list(val))
        print()

        voltData.append(val)
        timeData.append(time.time() - start)
    
    end = time.time()


    print("Продолжительность:", end - start)
    print("Период одного измерения:", (end - start) / len(voltData))
    print("Частота дискретизации:", len(voltData) / (end - start))
    print("Шаг квантования АЦП:", maxV / (2**razr-1))

    with open("experiment_data.txt", "w") as file:
        for i in range(len(voltData)):
            file.write(str(voltData[i]) + ' ')
            file.write(str(timeData[i]) + '\n')


    plt.scatter(timeData, voltData, s=1)
    plt.show()

finally:
    RT.output(dac, 0)
    RT.output(led, 0)
    RT.cleanup()
