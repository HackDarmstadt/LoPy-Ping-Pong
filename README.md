# LoPy Ping Pong

**Please Note**: Work in progress

## Summary

This repo contains a [The Things Network](https://www.thethingsnetwork.org/)  demo setup for a [LoPy](https://www.pycom.io/product/lopy/) microcontroller communicating over [LoRa](https://www.lora-alliance.org/What-Is-LoRa/Technology).
The demo does the following things:

1. Connect to The Things Network backend
2. Set a counter to 0
3. Sends the current counter value over LoRa to the The Things Network when the user presses the onboard button
4. Receives a (optional) data package from The Things Network
5. If the data parses to RGB value, sets the onboard color LED accordingly (otherwise, LED is switched off)

The text below provides pointers to LoRa WAN, The Things Network, LoPy and setting the demo up.

## LoRa WAN

LoRa is a radio modulation technology for low power wide area networks ([LPWAN](https://en.wikipedia.org/wiki/LPWAN)). 
LoRa WAN is an open LPWAN data link standard maintained by the LoRa Alliance.

### Benefits
* Low power (battery powerd devices that last for months/years)
* Long range (kilometers, under line-of-sight conditions > 40km has been observed)
* Low budget ($12 for a modem, $200 for a gateway, OSS stack)
* Unlicenced spectrum (Europe/Africa 868MHz, Americas 915MHz, Asia 433MHz)

### Drawbacks
* Small bandwith: Transmitting anything close to pictures, videos is meaningless with LoRa
* Limited air time/Fair use policy 

### Recommended Reading
* [LoRa (Wikipedia article)](https://en.wikipedia.org/wiki/LPWAN)
* [LoRa Technology (official page)](https://www.lora-alliance.org/What-Is-LoRa/Technology)
* [LoRa vs LTE vs Sigfox (blog post by Nick Hunn)](http://www.nickhunn.com/lora-vs-lte-m-vs-sigfox/)
* [Decoding the LoRa PHY (33c3 session by Matt Knight)](https://media.ccc.de/v/33c3-7945-decoding_the_lora_phy#video&t=129)
* [Limitation (The Things Network Forum)](https://www.thethingsnetwork.org/forum/t/limitations-data-rate-packet-size-30-seconds-uplink-and-10-messages-downlink-per-day-fair-access-policy/1300)
* [Understanding the Limits of LoRaWAN (article in IEEE Communications)](https://arxiv.org/pdf/1607.08011.pdf)

## The Things Network

TODO

## LoPy

LoPy is a MicroPython enabled microcontroller that supports three different wireless protocols: LoRa, Wifi, Bluetooth. Not a low price option to use with The Things Network but many usability benefits, as all necessary pieces (microprocessor, radio module, python are nicely packaged into a single component).

### Alternatives
* TheThingsUno: Built for The Things Network but not yet available (June 2017).
* Teensy LC (microcontroller) + RFM95 (radio module): Low cost but requires soldering and fiddling
* Many more

### Links
* [LoPy (official page)](https://www.pycom.io/product/lopy/)
* [LoPy getting started](https://docs.pycom.io/pycom_esp32/pycom_esp32/getstarted.html)
* [Pymakr Plugin (IDE)](https://docs.pycom.io/pycom_esp32/pycom_esp32/toolsandfeatures.html#pymakr-ide)
* [LoPy LoRaWAN example (ABP)](https://docs.pycom.io/pycom_esp32/pycom_esp32/tutorial/includes/lora-abp.html)
* [LoPy and The Things Network (forum posts)](https://www.thethingsnetwork.org/forum/search?q=lopy)
* [Micropython (official page)](https://micropython.org/)
* [Dive into Python 3](http://www.diveintopython3.net/)


## Demo Setup

The demo setup consists of the following components:
* Your laptop, a micro USB cable, and the Pymakr IDE installed
* LoPy node with extension board and antenna 
* The python code in this repository
* "The Things Network" (TTN) backend running in the cloud
* Your TTN account and your own TTN application
* The TTN console

### Step by Step Description

1. Follow the 'LoPy to Single Channel ...' online tutorial
2. Open the TTN console and navigate to your registered device
2. Connect to your LoPy via micro-USB
3. Load the boot.py and main.py files to your LoPy
4. Update the connect parameters in main.py to your application's parameters
5. Run the main.py
6. Click on the micro button on the LoPy extension board
7. You should see the message in the TTN console

### Links
* [LoPy to Single Channel Gateway to The Things Network (by Chris Samuelson)](https://www.hackster.io/ChrisSamuelson/lopy-to-single-channel-gateway-to-the-things-network-08f642)
* [TTN Console (need to login for this)](https://console.thethingsnetwork.org/)
