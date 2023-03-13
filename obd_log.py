import obd



ports = obd.scan_serial()       # return list of valid USB or RF ports
print("ports: ", ports)                    # ['/dev/ttyUSB0', '/dev/ttyUSB1']

connection = obd.OBD() # auto-connects to USB or RF port

#https://python-obd.readthedocs.io/en/latest/Command%20Tables/

cmd = obd.commands.RPM

response = connection.query(cmd) # send the command, and parse the response

print(response.value) # returns unit-bearing values thanks to Pint
cmd_dtc = obd.commands.DTC_RPM
response_dtc = connection.query(cmd_dtc)
print("  dtc ", response_dtc)
