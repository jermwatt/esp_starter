import network
from indicator_leds import led_1


def check():
    station = network.WLAN(network.STA_IF)
    if station.isconnected():
        led_1.on()
        led_1.on()
        led_1.on()

        