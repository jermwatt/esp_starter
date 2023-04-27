import ConnectWifiStaticIP
from pins_led import success_signal, failure_signal
import run_webrepl
import gc

### connect to wifi ###
wifi_connect_result = ConnectWifiStaticIP.connect()

# visual indicator of wifi connection
if wifi_connect_result == 0:
    # blink success signal
    success_signal(0, True, 500)
    success_signal(0, True, 500)
    success_signal(0, True, 500)

    ### start webrepl ###
    webrepl_startup_result = run_webrepl.start()
    if webrepl_startup_result == 0:
        success_signal(0, True, 1000)
        success_signal(0, True, 1000)

    else:
        failure_signal(0)
else:
    # blink failure signal
    failure_signal(0)

gc.collect()

from irq_switch_timer_test import start
start()
