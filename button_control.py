import RPi.GPIO as GPIO
import time

led_pin = 17

button_pin = 18

led_status = True


def print_message():
	print ("========================================")
	print ("|          Button control LED          |")
	print ("|    ------------------------------    |")
	print ("|         LED connect to GPIO0         |")
	print ("|        Button connect to GPIO1       |")
	print ("|                                      |")
	print ("|   Press button to turn on/off LED.   |")
	print ("|                                      |")
	print ("|                            SunFounder|")
	print ("========================================\n")
	print 'Program is running...'
	print 'Please press Ctrl+C to end the program...'
	raw_input ("Press Enter to begin\n")

def setup_gpio():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.HIGH)

    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


    GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=switch_led)


def switch_led(env=None):
    global led_status

    led_status = not led_status

    GPIO.output(led_pin, led_status)

    if led_status:
        print ("Led off")

    else:
        print("Led ON")

def main():
    print_message()

    
    while True:
        time.sleep(1)

def destroy():

    GPIO.output(led_pin, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == "__main__":
    setup_gpio()

    try:
        main()

    except KeyboardInterrupt:
        destroy()    