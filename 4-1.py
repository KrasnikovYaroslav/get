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

    while 1:
        try:
            num = int(input("Введите число "))

        except ValueError:
            RT.output(dac, [0, 0, 0, 0, 0, 0, 0, 0])
            print("ЧИСЛО должно быть ЦЕЛЫМ")
            continue
        
        if num < 0:
            RT.output(dac, [0, 0, 0, 0, 0, 0, 0, 0])
            print("Число должно быть ПОЛОЖИТЕЛЬНЫМ")

        elif num > 255:
            RT.output(dac, [0, 0, 0, 0, 0, 0, 0, 0])
            print("Число должно быть МЕНЬШЕ 256")

        else:
            num_listed = dec_to_bin_list(num)
            RT.output(dac, num_listed)

            print("Expected voltage: ", num / 256 * 3.3)

        




finally:

    RT.output(dac, [0, 0, 0, 0, 0, 0, 0, 0])
    RT.cleanup()
    

