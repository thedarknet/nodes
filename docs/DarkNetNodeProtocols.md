# DarkNetNodeProtocols

Documentation on darknet node communication

# Vision:
  Promote interoperability between device makers, by implementing one or more of the protocols below the device can participate in the DarkNet.  

# Objective:
* Document the protocol used to particpate in the DarkNet
* The DarkNet communication protocol via I2C to be a superset of SAO (DefCon Shitty Add On) communication protocol.

# Overview

# Communication Capabilities:
| Capability | Capability Type | Notes |
| --- | --- | --- |
| Daemon Remote EndPt| HTTPS Com Protocol | Can act as a remote end point for quests |
| Daemon Client | HTTPS Com Protocol \| WebSocket | Can act as a end point for the DarkNet Daemon |
| WiFi | Connection Filter | Node can communicate over wifi |
| Gateway| Connection Filter | Node can act as an internet gateway|
| BLE | Connection Filter | Node can communicate over BLE |
|Serial | Wire Protocol | Node can communicate over Serial|
| i2C   | Wire Protocol | Node can communicate over I2C |
| SPI   | Wire Protocol | Node can communicate over SPI |

# Communication Capability Bits:

| Bit | Value | Capability|
| --- | --- | --- |
|  0  |   0     | NO CAPABILITY|
|  1  |  0x1    | DAEMON REMOTE ENDPOINT|
|  2  |  0x2    | DAEMON CLIENT | 
|  3  |  0x4    | WIFI   |
|  4  |  0x8    | GATEWAY | 
|  5  |  0x10   | BLE |
|  6  |  0x20   | SERIAL |
|  7  |  0x40   | I2C |
|  8  |  0x80   | SPI |
|  9  |  0x100  | HTTPS COMM PROTOCOL |
|  10 |  0x200  | WebSocket |
|  11 |  0x400  | Wire Protocol |

# Overview

Basic I2C operations for the Darknet "Official" Shitty Add-On (SAO) board

# Protocol Setup:

| Capability | SetUp|
| --- | --- | 
| NO CAPABILITY         | None |
| DAEMON REMOTE ENDPOINT| Device must be registered, Daemon will call DNMagic to validate signature and match domain|
| DAEMON CLIENT         | Device must be registered, Daemon will call DNMagic to validate signature and match domain|
| WIFI                  | AP Must be WPA2+CCMP, SID + BSSID must be registered with DarkNet (for trusted operations), DarkNet HTTPS protocol or WebSocket needs to be on default gateway address|
| GATEWAY               | Once connected it will forward requests to assigned end point | 
| BLE                   | Once Paired connect and set up serial interface, BSSID Must be registed with DarkNet (for trusted operations)|
| SERIAL                | 115200 serial communication speed, 8, N, 1|
| I2C                   | 400000 bps, i2c address is up to developer, host should scan sending DNMagic to each|
| SPI                   | 1000000 bps |
| HTTPS COMM PROTOCOL   | Send DNMagic command to default gateway address after connection |
| WebSocket             | Send DNMagic command to default gateway address after connection |
| Wire Protocol         | Communication must be: BLE Serial, Serial, I2C or SPI |

# DarkNet Node Role

What is the device used for on the DarkNet

| Bit | Value | Capability|
| --- | --- | --- |
|  0  | 0x0     | SAO |
|  1  | 0x1     | Communication Node | 
|  2  | 0x2      | NPC |
|  3  | 0x4      | Sensor |


# Trusted Mode

To get a list of devices that are registered with the DarkNet call:
Request:
```
HTTPS: GET /DNN/Devices
```
Response:
```
{
  "devices": [
    {
      "typeid": "1",
      "public key": "xxxxxx",
      "capabilties": 1,
      "aux": [
        {
          "sid": "sid"
        },
        {
          "bssid": "bssid"
        }
      ]
    },
    {
      "typeid": "2",
      "public key": "xxxxxx",
      "capabilties": 1
    },
    {
      "typeid": "3",
      "public key": "xxxxxx",
      "capabilties": 1
    }
  ],
  "signature": "xxxx"
}
```
			

# Communication Protocol:

### DNMagic
| Protocol  | cmd  | Parameters  | Response | Notes  |
|---|---|---|---|---|
| HTTPS Com Protocol  | GET /DNN/Magic/{8 Byte Number}     | InURL | ```{"magic": 265485, typeid: "<device id>" , "signature": "<message signature" , "pversion": <version #>, "capability": <cap bits>, "roles":<role bits>}``` |   |
| WebSocket           | ```{"cmd":"dnmagic"}```  | 8:Random  |  ```{"magic": 265485, typeid: "<device id>" , "signature": "<message signature" , "pversion": <version #>, "capability": <cap bits>, "roles":<role bits>}``` |  |
| Wire Protocol      | 0x10               | 8:Random  | <4:Magic=0x00040D0D><4:typeid><16:Signature>,<1:pversion>,<3:capabilities><3:role bits>  | |
* pversion = protocol Version, current verision = 1,

### Device Type

# Read Operations:

NOUN, VERB, DATA

0x00 - System Info
0x00, 0x00								- Type					STRING		EGGPLANT
0x00, 0x01								- Version				STRING		1.0.0
0x00, 0x02								- Serial				STRING		8 Chars
0x00, 0x03								- Name					STRING		12 Chars

0x02 - LED Mode
0x02, 0x00								- LED Mode				BYTE		0 - 5 (6 is off)

0x04 - Infection Mode
0x04, 0x00								- Try to infect me		BYTE		Roll the dice
0x04, 0x01								- Infection Status		BYTE		Reports true status (i.e. doctor report)

0x08 - Memory Page 2
0x08, <ADDRESS_2_BYTES>, <LENGTH>		- Read EEPROM 			Up to 16 BYTES


Write Operations:

NOUN, VERB, DATA (up to 14 bytes)

0x01 - System Info
0x01, 0x03, DATA						- Name					STRING		12 Chars

0x03 - LED Mode
0x03, 0x00, <BYTE>						- LED Mode				BYTE		0 - 6 (6 = off)

0x05 - Infection Mode
0x05, 0x00, <BYTE>						- Infection Infect		BYTE		Set to infect.  Only acts on bits 7 & 8
0x05, 0x01, <BYTE>						- Infection Cure		BYTE		Set to cure.  Only acts on bits 7 & 8

0x09 - Memory Page 2
0x09, <ADDRESS_2_BYTES>, <BYTES>, DATA	- Write EEPROM 			BYTES 		Up to 10 bytes 

