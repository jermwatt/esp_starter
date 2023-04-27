import webrepl


def start():
    try:
        webrepl.start(password="test")
        return 0
    except:
        return 1
