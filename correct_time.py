import ntptime
import time
UTC_OFFSET = -7 * 60 * 60


def set_time():
    ntptime.settime()


def check_time():
    current_time = time.localtime(time.time() + UTC_OFFSET)
    print(current_time)
