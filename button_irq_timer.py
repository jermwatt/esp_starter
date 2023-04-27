from machine import Pin, Timer
from time import sleep_ms

led = Pin(21, Pin.OUT)    # create output pin on GPIO21

button_pin4 = Pin(4, Pin.IN, Pin.PULL_UP)

button_pressed = False

def button_pressed_isr(event):
    global button_pressed
    global button_event

    if button_pin4.value() == False:
        button_pressed = True
        button_event = event
    else:
        button_pressed = False


button_timer = Timer(1)
button_timer.init(period=50, mode=Timer.PERIODIC, callback=button_pressed_isr)

while True:
    if button_pressed == True:
        button_pressed = False
        led.on()
        print("Button pressed event", button_event)
        sleep_ms(1000)
    else:
        led.off()