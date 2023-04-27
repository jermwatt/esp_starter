from machine import Pin
from utime import sleep_ms
import dht
from pins_led import leds, failure_signal
temp_1 = dht.DHT22(Pin(2))
temp_2 = dht.DHT22(Pin(0))
temp_3 = dht.DHT22(Pin(4))
temps = [temp_1, temp_2, temp_3]


def return_single_temp(num):
    try:
        temps[num].measure()
        leds[num + 1].on()
        sleep_ms(1000)
        leds[num + 1].off()
        data = {"temperature:": float(
            temps[num].temperature()), "humidity": float(temps[num].humidity())}
        return data
    except:
        failure_signal(num)
        return {}


def return_all_temp():
    for num in range(len(temps)):
        try:
            temps[num].measure()
            leds[num + 1].on()
        except:
            failure_signal(num)
            leds[num + 1].on()
    sleep_ms(1000)
    for num in range(len(temps)):
        leds[num + 1].off()

    data = {}
    for num in range(len(temps)):
        temp = temps[num].temperature()
        hum = temps[num].humidity()
        data['temp_' + str(num + 1)] = float(temp)
        data['hum_' + str(num + 1)] = float(hum)        
    return data
