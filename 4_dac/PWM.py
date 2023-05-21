import RPi.GPIO as GPIO

PWM_PORT = 27

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PWM_PORT, GPIO.OUT)

def run_pwm():
    p = GPIO.PWM(PWM_PORT, 1000)
    p.start(0)
    try:
        while True:
            inp = input()
            if inp == "q":
                break
            if any(map(str.isalpha, inp)):
                print("ERR:\tNAN")
            elif ("." in inp):
                print("ERR:\tnon-integer value")
            elif(int(inp) < 0):
                print("ERR:\tnegative value")
            else:
                inp = int(inp)
                p.ChangeDutyCycle(inp)
    finally:
        p.stop()

def cleanup_gpio():
    GPIO.output(PWM_PORT, 0)
    GPIO.cleanup()

def main():
    setup_gpio()
    try:
        run_pwm()
    finally:
        cleanup_gpio()

if __name__ == "__main__":
    main()