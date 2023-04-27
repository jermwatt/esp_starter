from machine import Pin
from utime import sleep_ms

led_0 = Pin(15, Pin.OUT)
led_1 = Pin(13, Pin.OUT)
led_2 = Pin(12, Pin.OUT)
led_3 = Pin(14, Pin.OUT)

leds = [led_0, led_1, led_2, led_3]


def success_signal(num, leave_on, speed):
    leds[num].on()
    sleep_ms(speed)
    leds[num].off()
    sleep_ms(speed)
    leds[num].on()

    if not leave_on:
        leds[num].off()


def change_all_leds_state(position):
    if position == 'on':
        for num in range(1, len(leds)):
            leds[num].on()
    else:
        for num in range(1, len(leds)):
            leds[num].off()


def success_signal_all(leave_on, speed):
    change_all_leds_state('on')
    sleep_ms(speed)

    change_all_leds_state('off')
    sleep_ms(speed)

    change_all_leds_state('on')
    if not leave_on:
        change_all_leds_state('off')


def failure_signal(num):
    for i in range(3):
        leds[num].on()
        sleep_ms(200)
        leds[num].off()
        sleep_ms(200)
        leds[num].on()
        sleep_ms(200)
        leds[num].off()
        sleep_ms(200)


def failure_signal_all():
    for i in range(3):
        change_all_leds_state('on')
        sleep_ms(200)
        change_all_leds_state('off')
        sleep_ms(200)
        change_all_leds_state('on')
        sleep_ms(200)
        change_all_leds_state('off')
        sleep_ms(200)
