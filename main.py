from machine import Pin
from network import LoRa

import pycom
import time
import socket
import binascii
import struct

# Create a socket to communicate with TheThingsNetwork
def create_ttn_socket():
    join_ttn()
    
    ttn_sock = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    ttn_sock.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
    ttn_sock.setblocking(False)
    
    return ttn_sock

# Join TheThingsNetwork
def join_ttn():
    # Initialize LoRa in LORAWAN mode.
    lora = LoRa(mode=LoRa.LORAWAN, sf=7, tx_power=14)
    lora.BW_125KHZ
    lora.CODING_4_5

    # Create an ABP authentication params using parameter from TheThingsNetwork:
    # https://console.thethingsnetwork.org/applications/<your-app>/devices/<your-device>
    device_address = '26011D09'
    network_session_key = 'E782B283027DD5EF0CC8C217B91549CD'
    app_session_key = '52F44DCA45CC0E05CD4286F8056DEAAB'
    
    # Join TTN using ABP (Activation By Personalization)
    da = struct.unpack(">l", binascii.unhexlify(device_address.replace(' ','')))[0]
    nsk = binascii.unhexlify(network_session_key.replace(' ',''))
    ask = binascii.unhexlify(app_session_key.replace(' ',''))
    lora.join(activation=LoRa.ABP, auth=(da, nsk, ask))
    
    # Wait for join OK
    while not lora.has_joined():
        print('Joining The Things Network ...' )
        time.sleep(1)

    print('Sussessfully joined The Things Network')

# Create the button object (representing the LoPy user button)
def create_button():
    button = Pin("G17", Pin.IN, pull=Pin.PULL_UP)
    button.callback(Pin.IRQ_RISING, button_handler) # Interrupt on raising signal
    
    return button
    
# Interrupt handler for button
def button_handler(arg):
    button.callback(Pin.IRQ_RISING, None) # Deactivate interrupt
    active = 0
    for i in range(20):
        active += button()
        time.sleep_ms(10)

    if active > 15:
        button_action()
    
    button.callback(Pin.IRQ_RISING, button_handler) # reactivate interrupt

# Pressing the button will send the current counter value to TheThingsNetwork
# Received uplink data is used to set the color LED accordingly
def button_action():
    global sock
    global counter
    
    data_down = str(counter)
    print('Sending data:',  data_down)
    sock.send(data_down)
    
    data_up = sock.recv(4)
    print('Recieved data:',  data_up,  'len(data):',  len(data_up))
    
    if(len(data_up) == 3):
        color = (data_up[0]<<16)|(data_up[1]<<8)|data_up[2]
        print('Update LED')
        pycom.rgbled(color)
    else:
        print('Swich LED off')
        pycom.rgbled(0)
    
    counter += 1

# Switch off the LED
pycom.heartbeat(False)
pycom.rgbled(0)

# Create LoRa socket and button
sock = create_ttn_socket()
button = create_button()
counter = 0;
