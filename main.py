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
tempSensorDCDC_1 = ""
tempSensorDCDC_2 = ""
tempSensorDCDC_3 = ""
tempSensorMCU = ""
currSensorDCDC = ""
voltSensorDCDC = ""

# UDP VARIABLES
UDP_IP_PC = "127.0.0.1"

# PORTE DATI PER SIMULINK
UDP_PORT_TEMP_1 = 18001
UDP_PORT_TEMP_2 = 18002
UDP_PORT_TEMP_3 = 18003
UDP_PORT_TEMP_MCU = 18004
UDP_PORT_CURR = 18005
UDP_PORT_VOLT = 18006

# INVIA A PC
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock6 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

# ---------------------------------------------------- MAIN ------------------------------------------------------------

try:
    while True:
        message = bus.recv()  # Wait until a message is received.

        if message.arbitration_id == 0x500:
            tempSensorDCDC_1 = int((str(format(int('{0:x}'.format(message.data[0]), 16), '08b'))), 2)
            print("Temperature sensor 1 DCDC: ", tempSensorDCDC_1)
            tempSensorDCDC_2 = int((str(format(int('{0:x}'.format(message.data[1]), 16), '08b'))), 2)
            print("Temperature sensor 2 DCDC: ", tempSensorDCDC_2)
            tempSensorDCDC_3 = int((str(format(int('{0:x}'.format(message.data[2]), 16), '08b'))), 2)
            print("Temperature sensor 3 DCDC: ", tempSensorDCDC_3)
            tempSensorMCU = int((str(format(int('{0:x}'.format(message.data[3]), 16), '08b'))), 2)
            print("MCU Temperature Sensor: ", tempSensorMCU)
            sock1.sendto(message.data[0], (UDP_IP_PC, UDP_PORT_TEMP_1))
            sock2.sendto(message.data[1], (UDP_IP_PC, UDP_PORT_TEMP_2))
            sock3.sendto(message.data[2], (UDP_IP_PC, UDP_PORT_TEMP_3))
            sock4.sendto(message.data[3], (UDP_IP_PC, UDP_PORT_TEMP_MCU))

        if message.arbitration_id == 0x501:
            currSensorDCDC = int((str(format(int('{0:x}'.format(message.data[0]), 16), '08b'))), 2)
            print("DCDC Output Current: ", currSensorDCDC)
            sock1.sendto(message.data[0], (UDP_IP_PC, UDP_PORT_CURR))

        if message.arbitration_id == 0x502:
            voltSensorDCDC = int((str(format(int('{0:x}'.format(message.data[0]), 16), '08b'))), 2)
            print("DCDC Output Voltage: ", voltSensorDCDC)
            sock1.sendto(message.data[0], (UDP_IP_PC, UDP_PORT_VOLT))

except KeyboardInterrupt:
    # Catch keyboard interrupt
    os.system("sudo /sbin/ip link set can0 down")
    os.system("sudo /sbin/ip link set can0 up type can bitrate 500000")
    print('\n\rKeyboard interrtupt')