from machine import ADC, Pin, PWM, Timer
from time import sleep

pot_pwm = PWM(Pin(10))    # create an PWM object on pin 21
pot_adc = ADC(Pin(34))      # create ADC object on ADC pin
adc.atten(ADC.ATTN_11DB)  # Full range: 3.3v
pot_timer = Timer(2)
pot_led = Pin(20, Pin.OUT)    
led_pwm = PWM(pot_led,freq=1000)

def read_potentiometer(event):
    # set pot value
    pot_value = pot_adc.read()
    pwm_value = int(pot_value * 0.25)
    print("pot: ", pot_value, ", pwm: ", pwm_value)
    pot_pwm.duty(pwm_value)  # 0.24 derives from scaling 0..4095 to 0..1023 =>
    
    # set led value - range from 0 to 1023
    
    
    sleep(0.1)
    
def start_pot():
    pot_timer.init(period=5000, mode=Timer.PERIODIC, callback=read_potentiometer)

def stop_pot():
    pot_timer.deinit()
    


