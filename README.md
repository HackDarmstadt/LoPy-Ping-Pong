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
* [Decoding the LoRa PHY (33c3 session by Matt Knight](https://media.ccc.de/v/33c3-7945-decoding_the_lora_phy#video&t=129)
* [Limitation (The Things Network Forum)](https://www.thethingsnetwork.org/forum/t/limitations-data-rate-packet-size-30-seconds-uplink-and-10-messages-downlink-per-day-fair-access-policy/1300)
* [Understanding the Limits of LoRaWAN (article in IEEE Communications)](https://arxiv.org/pdf/1607.08011.pdf)

## The Things Network

TODO

## LoPy

TODO

## Setup

TODO
