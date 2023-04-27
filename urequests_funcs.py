import urequests
from utime import sleep_ms
import ujson as json
import gc
from pins_led import failure_signal_all, success_signal_all

get_url = "http://192.168.1.10:90"
post_url = "http://192.168.1.10:90/temp_hum_reciever"

headers = {"Content-Type": "application/json"}


def get(url):
    try:
        response = urequests.get(url)
        text = json.loads(response.content)
        response.close()
        success_signal_all(False, 250)
        return text
    except:
        failure_signal_all()


def post(url, data):
    try:
        response = urequests.post(url, headers=headers, data=json.dumps(data))
        text = json.loads(response.content)
        response.close()
        success_signal_all(False, 250)
        return text
    except:
        failure_signal_all()
