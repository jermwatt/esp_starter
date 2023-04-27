from machine import Pin, Timer
import dht
from utime import sleep_ms

temp_timer = Timer(1)
temp_sensor_1 = dht.DHT22(Pin(4))
temp_sensor_1 = dht.DHT22(Pin(5))
temp_sensor_1 = dht.DHT22(Pin(6))
temp_led_1 = Pin(20, Pin.OUT)    
temp_led_2 = Pin(21, Pin.OUT)   
temp_led_3 = Pin(22, Pin.OUT)   


def measure_temp_sensors(event):
    temp_sensor_1.measure()
    print("Temp: ", temp_sensor_1.temperature(), "°C, Humidity: ", temp_sensor_1.humidity(), "%")
    
    temp_sensor_2.measure()
    print("Temp: ", temp_sensor_2.temperature(), "°C, Humidity: ", temp_sensor_2.humidity(), "%")
    
    temp_sensor_3.measure()
    print("Temp: ", temp_sensor_3.temperature(), "°C, Humidity: ", temp_sensor_3.humidity(), "%")
    
def start_temp_sensors():
    # turn on indicator leds
    temp_led_1.on()
    temp_led_2.on()
    temp_led_3.on()
    
    # start temp sensing
    temp_timer.init(period=5000, mode=Timer.PERIODIC, callback=temp_sensor_3)
    
def stop_temp_sensors():
    temp_timer.deinit()
    sleep_ms(3000)
    temp_led_1.off()
    temp_led_2.off()
    temp_led_3.off()

