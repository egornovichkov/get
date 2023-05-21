import RPi.GPIO as GPIO

DAC_MAX_U = 3.3
DAC_BIT_DEPTH = 8
DAC_PORTS = [10, 9, 11, 5, 6, 13, 19, 26]
DAC_PORTS.reverse()

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DAC_PORTS, GPIO.OUT)

def convert_input(inp):
    if any(map(str.isalpha, inp)):
        return "ERR:\tNAN"
    elif ("." in inp):
        return "ERR:\tnon-integer value"
    elif(int(inp) < 0):
        return "ERR:\tnegative value"
    elif(int(inp) > (2 ** DAC_BIT_DEPTH - 1)):
        return "ERR:\tvalue > 255"
    else:
        inp = int(inp)
        GPIO.output(DAC_PORTS, tuple(map(lambda x: 1 & int(x), "{0:0>8}".format(bin(inp)[2:]))))
        return "OUT_VOLTAGE:\t{:.4f}".format(inp / (2 ** DAC_BIT_DEPTH - 1) * DAC_MAX_U)

def cleanup_gpio():
    GPIO.output(DAC_PORTS, 0)
    GPIO.cleanup()

def main():
    setup_gpio()
    try:
        inp = input()
        while inp != "q":
            result = convert_input(inp)
            print(result)
            inp = input()
    finally:
        cleanup_gpio()

if __name__ == "__main__":
    main()