
""" LoPy LoRaWAN Nano Gateway configuration options """

import machine
import ubinascii

WIFI_MAC = ubinascii.hexlify(machine.unique_id()).upper()
# Set  the Gateway ID to be the first 3 bytes of MAC address + 'FFFE' + last 3 bytes of MAC address
#GATEWAY_ID = WIFI_MAC[:6] + "FFFE" + WIFI_MAC[6:12]
GATEWAY_ID = '240ac4fffe023ae0'

#SERVER = 'asis-se.thethings.network'
SERVER = 'thethings.meshed.com.au'
#SERVER = 'router.us.thethings.network'

PORT = 1700

NTP = "pool.ntp.org"
NTP_PERIOD_S = 3600


#WIFI_SSID = 'IW_phone'
#WIFI_PASS = 'helloEevee123'

WIFI_SSID = 'helloap'
WIFI_PASS = 'C1sc0123'

# for EU868
#LORA_FREQUENCY = 868100000
#LORA_GW_DR = "SF7BW125" # DR_5
#LORA_NODE_DR = 5

# for US915
#LORA_FREQUENCY = 903900000
LORA_FREQUENCY = 915000000
LORA_GW_DR = "SF7BW125" # DR_3
LORA_NODE_DR = 3
