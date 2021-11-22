"""
########################################################################################################################
# COMPONENT: rpi_to_pc.py
# DESCRIPTION: File to use in the HOST PC in order to plot the ECU data
# PROJECT: CAN_to_Python.py
#
# AUTHOR: Federico Deidda
#
# REVISION:
# REVISION AUTHOR:
# LAST MODIFIED: 22/11/2021
########################################################################################################################
"""

# --------------------------------------------------- IMPORTS ----------------------------------------------------------

import socket

# --------------------------------------------------- VARIABLES --------------------------------------------------------

UDP_IP_RPI = "127.0.0.1"  # put RPI's IP

# BUFFER DATI DA RASPBERRY
BUF_PORT_TEMP_MOSFET = 8192
BUF_PORT_TEMP_DIODE = 8192
BUF_PORT_TEMP_INDUCTOR = 8192
BUF_PORT_TEMP_MCU = 8192
BUF_PORT_CURR_IN = 8192
BUF_PORT_CURR_OUT = 8192
BUF_PORT_VOLT_IN = 8192
BUF_PORT_VOLT_OUT = 8192
BUF_PORT_EFFICIENCY = 8192

# PORTE DATI DA RPI
UDP_PORT_TEMP_MOSFET = 18001
UDP_PORT_TEMP_DIODE = 18002
UDP_PORT_TEMP_INDUCTOR = 18003
UDP_PORT_TEMP_MCU = 18004
UDP_PORT_CURR_IN = 18005
UDP_PORT_CURR_OUT = 18006
UDP_PORT_VOLT_IN = 18007
UDP_PORT_VOLT_OUT = 18008
UDP_PORT_EFFICIENCY = 18009

# CREAZIONE SOCKET
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock6 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock7 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock8 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock9 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

# BINDING SOCKET
sock1.bind((UDP_IP_RPI, UDP_PORT_TEMP_MOSFET))
sock2.bind((UDP_IP_RPI, UDP_PORT_TEMP_DIODE))
sock3.bind((UDP_IP_RPI, UDP_PORT_TEMP_INDUCTOR))
sock4.bind((UDP_IP_RPI, UDP_PORT_TEMP_MCU))
sock5.bind((UDP_IP_RPI, UDP_PORT_CURR_IN))
sock6.bind((UDP_IP_RPI, UDP_PORT_CURR_OUT))
sock7.bind((UDP_IP_RPI, UDP_PORT_VOLT_IN))
sock8.bind((UDP_IP_RPI, UDP_PORT_VOLT_OUT))
sock9.bind((UDP_IP_RPI, UDP_PORT_EFFICIENCY))

# ---------------------------------------------------- MAIN ------------------------------------------------------------

# Start listening loop
while True:
    print("Waiting for ECU data...\n")
    # Each socket listen on a dedicated port (8 data - 8 ports)

    tempSensorMOSFET, addr1 = sock1.recvfrom(BUF_PORT_TEMP_MOSFET)
    print("__________________________DATA____________________________")
    tempSensorDIODE, addr2 = sock2.recvfrom(BUF_PORT_TEMP_DIODE)
    tempSensorINDUCTOR, addr3 = sock3.recvfrom(BUF_PORT_TEMP_INDUCTOR)
    tempSensorMCU, addr4 = sock4.recvfrom(BUF_PORT_TEMP_MCU)
    currSensorDCDC_IN, addr5 = sock5.recvfrom(BUF_PORT_CURR_IN)
    currSensorDCDC_OUT, addr6 = sock6.recvfrom(BUF_PORT_CURR_OUT)
    voltSensorDCDC_IN, addr7 = sock7.recvfrom(BUF_PORT_VOLT_IN)
    voltSensorDCDC_OUT, addr8 = sock8.recvfrom(BUF_PORT_VOLT_OUT)
    efficiency, addr9 = sock9.recvfrom(BUF_PORT_EFFICIENCY)

    print("Temperature sensor MOSFET:                  ", tempSensorMOSFET.decode())
    print("Temperature sensor DIODE:                   ", tempSensorDIODE.decode())
    print("Temperature sensor INDUCTOR:                ", tempSensorINDUCTOR.decode())
    print("Temperature sensor MCU:                     ", tempSensorMCU.decode())
    print("DCDC Input Current:                         ", currSensorDCDC_IN.decode())
    print("DCDC Output Current:                        ", currSensorDCDC_OUT.decode())
    print("DCDC Input Voltage:                         ", voltSensorDCDC_IN.decode())
    print("DCDC Output Voltage:                        ", voltSensorDCDC_OUT.decode())
    print("Efficiency:                                 ", efficiency.decode())
    print("__________________________________________________________\n")
