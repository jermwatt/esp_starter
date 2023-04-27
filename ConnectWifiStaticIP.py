def connect():
    import network
    
    try:
        station = network.WLAN(network.STA_IF)
        if not station.isconnected():
            import ujson as json
            
            with open("/wifi_cfg.json") as wifi_cfg:
                wifi_info = json.loads(wifi_cfg.read())
                
            ip = wifi_info["ip"]
            subnet = wifi_info["subnet"]
            gateway = wifi_info["gateway"]
            dns = wifi_info["dns"]
            ssid = wifi_info["ssid"]
            password = wifi_info["password"]
            
            station.active(True)
            station.ifconfig((ip, subnet, gateway, dns))
            station.connect(ssid, password)
            while not station.isconnected():
                pass
            print('SUCCESS: board connected to local wifi')
            print('network config:', station.ifconfig())
            return 0
        else:
            print('SUCCESS: board already connected to local wifi')
            print('network config:', station.ifconfig())
            return 0
    except Exception as e:
        print('FAILURE: failed to connect to network, exception below')
        print(e)
        return 1
