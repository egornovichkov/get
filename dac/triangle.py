import RPi.GPIO as GPIO
import time


def triangulate(t, period, amp):
    n = t / period
    flt = n - int(n)
    if flt > 0.5:
        return (1 - flt) * amp
    else:
        return flt * amp

def to_bits(signal, amplitude, bit_depth):
    return round(signal / amplitude * (2 ** bit_depth))

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DAC_PORTS, GPIO.OUT)

def convert_input(T):
    begin = time.time()
    while True:
        cur = time.time() - begin
        f = triangulate(cur, T, DAC_MAX_U)
        val = to_bits(f, DAC_MAX_U, DAC_BIT_DEPTH)
        GPIO.output(DAC_PORTS, tuple(map(lambda x: 1 & int(x), "{0:0>8}".format(bin(val)[2:]))))

def cleanup_gpio():
    GPIO.output(DAC_PORTS, 0)
    GPIO.cleanup()

def main():
    setup_gpio()
    try:
        T = float(input())
        convert_input(T)
    finally:
        cleanup_gpio()

if __name__ == "__main__":
    main()