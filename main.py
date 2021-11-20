"""
########################################################################################################################
# COMPONENT: main.py
# DESCRIPTION: Main Function
# PROJECT: CAN_to_Python.py
#
# AUTHOR: Federico Deidda
#
# REVISION:
# REVISION AUTHOR:
# LAST MODIFIED: 20/11/2021
########################################################################################################################
"""

# --------------------------------------------------- IMPORTS ----------------------------------------------------------

import os
import socket
import can

# --------------------------------------------------- VARIABLES --------------------------------------------------------

# CAN VARIABLES
bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
tempSensorMOSFET = ""
tempSensorDIODE = ""
tempSensorINDUCTOR = ""
tempSensorMCU = ""
currSensorDCDC_IN = ""
currSensorDCDC_OUT = ""
voltSensorDCDC_IN = ""
voltSensorDCDC_OUT = ""

# UDP VARIABLES
UDP_IP_PC = "127.0.0.1"

# PORTE DATI PER PC
UDP_PORT_TEMP_MOSFET = 18001
UDP_PORT_TEMP_DIODE = 18002
UDP_PORT_TEMP_INDUCTOR = 18003
UDP_PORT_TEMP_MCU = 18004
UDP_PORT_CURR_IN = 18005
UDP_PORT_CURR_OUT = 18006
UDP_PORT_VOLT_IN = 18007
UDP_PORT_VOLT_OUT = 18008

# CREAZIONE SOCKET
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock6 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock7 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock8 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

# ---------------------------------------------------- MAIN ------------------------------------------------------------

try:
    while True:
        message = bus.recv()  # Wait until a message is received.

        if message.arbitration_id == 0x500:
            tempSensorMOSFET = int((str(format(int('{0:x}'.format(message.data[0]), 16), '08b'))), 2)
            print("Temperature sensor MOSFET:   ", tempSensorMOSFET)
            tempSensorDIODE = int((str(format(int('{0:x}'.format(message.data[1]), 16), '08b'))), 2)
            print("Temperature sensor DIODE:    ", tempSensorDIODE)
            tempSensorINDUCTOR = int((str(format(int('{0:x}'.format(message.data[2]), 16), '08b'))), 2)
            print("Temperature sensor INDUCTOR: ", tempSensorINDUCTOR)
            tempSensorMCU = int((str(format(int('{0:x}'.format(message.data[3]), 16), '08b'))), 2)
            print("Temperature Sensor MCU     : ", tempSensorMCU)
            sock1.sendto(message.data[0], (UDP_IP_PC, UDP_PORT_TEMP_MOSFET))
            sock2.sendto(message.data[1], (UDP_IP_PC, UDP_PORT_TEMP_DIODE))
            sock3.sendto(message.data[2], (UDP_IP_PC, UDP_PORT_TEMP_INDUCTOR))
            sock4.sendto(message.data[3], (UDP_IP_PC, UDP_PORT_TEMP_MCU))

        if message.arbitration_id == 0x501:
            currSensorDCDC_IN = int((str(format(int('{0:x}'.format(message.data[0]), 16), '08b'))), 2)
            print("DCDC Input Current:          ", currSensorDCDC_IN)
            sock5.sendto(message.data[0], (UDP_IP_PC, UDP_PORT_CURR_IN))
            currSensorDCDC_OUT = int((str(format(int('{0:x}'.format(message.data[1]), 16), '08b'))), 2)
            print("DCDC Output Current:         ", currSensorDCDC_OUT)
            sock6.sendto(message.data[1], (UDP_IP_PC, UDP_PORT_CURR_OUT))

        if message.arbitration_id == 0x502:
            voltSensorDCDC_IN = int((str(format(int('{0:x}'.format(message.data[0]), 16), '08b'))), 2)
            print("DCDC Input Voltage:          ", voltSensorDCDC_IN)
            sock7.sendto(message.data[0], (UDP_IP_PC, UDP_PORT_VOLT_IN))
            voltSensorDCDC_OUT = int((str(format(int('{0:x}'.format(message.data[1]), 16), '08b'))), 2)
            print("DCDC Output Voltage:         ", voltSensorDCDC_OUT)
            sock8.sendto(message.data[1], (UDP_IP_PC, UDP_PORT_VOLT_OUT))

except KeyboardInterrupt:
    # Catch keyboard interrupt
    os.system("sudo /sbin/ip link set can0 down")
    os.system("sudo /sbin/ip link set can0 up type can bitrate 500000")
    print('\n\rKeyboard interrtupt')