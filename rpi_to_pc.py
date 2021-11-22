"""
########################################################################################################################
# COMPONENT: rpi_to_pc.py
# DESCRIPTION: File to use in the HOST PC in order to plot the ECU data received from RPI
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
from reprint import output

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
with output(initial_len=12, interval=0) as output_lines:
    while True:
        output_lines[0] = "Waiting for ECU data..."

        # Each socket listen on a dedicated port
        tempSensorMOSFET, addr1 = sock1.recvfrom(BUF_PORT_TEMP_MOSFET)
        output_lines[1] = "__________________________DATA____________________________"
        tempSensorDIODE, addr2 = sock2.recvfrom(BUF_PORT_TEMP_DIODE)
        tempSensorINDUCTOR, addr3 = sock3.recvfrom(BUF_PORT_TEMP_INDUCTOR)
        tempSensorMCU, addr4 = sock4.recvfrom(BUF_PORT_TEMP_MCU)
        currSensorDCDC_IN, addr5 = sock5.recvfrom(BUF_PORT_CURR_IN)
        currSensorDCDC_OUT, addr6 = sock6.recvfrom(BUF_PORT_CURR_OUT)
        voltSensorDCDC_IN, addr7 = sock7.recvfrom(BUF_PORT_VOLT_IN)
        voltSensorDCDC_OUT, addr8 = sock8.recvfrom(BUF_PORT_VOLT_OUT)
        efficiency, addr9 = sock9.recvfrom(BUF_PORT_EFFICIENCY)

        output_lines[2] = "Temperature sensor MOSFET:                  {}°C".format(tempSensorMOSFET.decode())
        output_lines[3] = "Temperature sensor DIODE:                   {}°C".format(tempSensorDIODE.decode())
        output_lines[4] = "Temperature sensor INDUCTOR:                {}°C".format(tempSensorINDUCTOR.decode())
        output_lines[5] = "Temperature sensor MCU:                     {}°C".format(tempSensorMCU.decode())
        output_lines[6] = "Input Current:                              {}A".format(currSensorDCDC_IN.decode())
        output_lines[7] = "Output Current:                             {}A".format(currSensorDCDC_OUT.decode())
        output_lines[8] = "Input Voltage:                              {}V".format(voltSensorDCDC_IN.decode())
        output_lines[9] = "Output Voltage:                             {}V".format(voltSensorDCDC_OUT.decode())
        output_lines[10] = "Efficiency:                                 {}%".format(efficiency.decode())
        output_lines[11] = "__________________________________________________________"
