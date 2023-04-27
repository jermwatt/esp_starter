#!/bin/bash

# params
port=/dev/tty.usbserial-0001
bin_file=espBinaries/esp8266-20220117-v1.18.bin

# quit out of current screen to usb port
screen -X quit

# step 1: erase esp2866 flash --> note - to find the proper tty address of usb diff an ls of the /dev directory with the device plugged in / not plugged in.  in the compose file we normalize-map this port to /dev/ttyUSB0
esptool.py --port "$port" erase_flash

# step 2: install micropython firmware
echo 'INSTALLING: firmware'
esptool.py --port "$port" --baud 460800 write_flash --flash_size=detect -fm dio 0 "$bin_file"

# step 3: load up
for i in `cat micro_files.txt`
do
	echo 'INSTALLING:' $i
 	ampy --port "$port" --baud 115200 put $i $i
done