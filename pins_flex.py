from machine import ADC
adc = ADC(0)

def return_flex():
    data = {}
    data['flex_1'] = ''
    try:
        flex_val = 1024-adc.read()
        data['flex_1'] = int(flex_val)
    except Exception as e:
        #print(e)
        pass
    return data