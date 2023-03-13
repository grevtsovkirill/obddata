import obd


ports = obd.scan_serial()       # return list of valid USB or RF ports
print("ports : ", ports)                    # ['/dev/ttyUSB0', '/dev/ttyUSB1']

connection = obd.OBD() # auto-connects to USB or RF port
# all commands
# https://python-obd.readthedocs.io/en/latest/Command%20Tables/

cmd = obd.commands.RPM

response = connection.query(cmd) # send the command, and parse the response

print(response.value) # returns unit-bearing values thanks to Pint
cmd_dtc = obd.commands.DTC_RPM
response_dtc = connection.query(cmd_dtc)
print("  dtc ", response_dtc)



# OBD Globals
obdRunning = True
obdAvailable = False
obdVoltage = 0
obdCoolant = 0
obdOil = 0
obdLoad = 0
obdIntake = 0

# OBD Thread
def obd_thread():
    global obdRunning, obdAvailable, obdVoltage, obdCoolant, obdOil, obdLoad, obdIntake
    obdConnection = obd.OBD()
    print("OBD connected")
    while obdRunning:
        cmd = obd.commands.COOLANT_TEMP
        response = obdConnection.query(cmd)
        obdCoolant = response.value.magnitude
        
        cmd = obd.commands.ELM_VOLTAGE
        response = obdConnection.query(cmd)
        obdVoltage = response.value.magnitude
        
        #cmd = obd.commands.OIL_TEMP
        #response = obdConnection.query(cmd)
        #obdOil = response.value
        
        cmd = obd.commands.ENGINE_LOAD
        response = obdConnection.query(cmd)
        obdLoad = response.value.magnitude
        
        cmd = obd.commands.INTAKE_TEMP
        response = obdConnection.query(cmd)
        obdIntake = response.value.magnitude
        obdAvailable = True
        time.sleep(0.5)
