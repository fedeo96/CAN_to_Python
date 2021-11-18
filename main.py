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
# LAST MODIFIED: 18/11/2021
########################################################################################################################
"""


# --------------------------------------------------- IMPORTS ----------------------------------------------------------

import os
import can

# --------------------------------------------------- VARIABLES --------------------------------------------------------

bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
tempSensorDCDC_1 = ""
tempSensorDCDC_2 = ""
tempSensorDCDC_3 = ""
tempSensorMCU = ""
currSensorDCDC = ""
voltSensorDCDC = ""

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

        if message.arbitration_id == 0x501:
            currSensorDCDC = int((str(format(int('{0:x}'.format(message.data[0]), 16), '08b'))), 2)
            print("DCDC Output Current: ", currSensorDCDC)

        if message.arbitration_id == 0x502:
            voltSensorDCDC = int((str(format(int('{0:x}'.format(message.data[0]), 16), '08b'))), 2)
            print("DCDC Output Voltage: ", voltSensorDCDC)

except KeyboardInterrupt:
    # Catch keyboard interrupt
    os.system("sudo /sbin/ip link set can0 down")
    os.system("sudo /sbin/ip link set can0 up type can bitrate 500000")
    print('\n\rKeyboard interrtupt')