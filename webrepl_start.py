import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
import webrepl

def start():
    webrepl.start()
    gc.collect()
