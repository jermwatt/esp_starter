from pins_led import failure_signal_all
from pins_temp import return_single_temp, return_all_temp
from pins_flex import return_flex
from pins_switch import switch_1
from urequests_funcs import get, post, get_url, post_url
switch_pressed = False


def sense_and_send():
    try:
        all_data = return_all_temp()
        flex_data = return_flex()
        all_data['flex_1'] = flex_data['flex_1']
        wrapped_data = {}
        wrapped_data['data'] = all_data
        response = post(post_url, wrapped_data)
    except Exception as e:
        print(e)
        failure_signal_all()


def my_callback(pin):
    global switch_pressed

    if (switch_1.value() == 0) and (switch_pressed == False):  # active-low --> measure
        #print('switch on')
        #response = get(get_url)
        # print(response)
        sense_and_send()

        # print(response)
        switch_pressed = True
    elif (switch_1.value() == 1) and (switch_pressed == True):
        #print('switch off')
        switch_pressed = False


def start():
    switch_1.irq(my_callback)
