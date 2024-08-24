import telnetlib
import time

host = "10.10.10.10"
user = "admin"
password = "admin"

# Increase the timeout value to allow more time for responses
timeout = 10

try:
    tel = telnetlib.Telnet(host, 23, timeout)

    tel.read_until(b"Username:", timeout)
    tel.write(user.encode('ascii') + b"\n")
    tel.read_until(b"Password:", timeout)
    tel.write(password.encode('ascii') + b"\n")
    time.sleep(1) 
    tel.write(b"show gpon \n")
    # time.sleep(1) 
    # tel.write(b"interface gpon-olt_1/2/2\n")
    # time.sleep(1) 
    # tel.write(b"no shutdown\n")
    time.sleep(1)
    output = tel.read_very_eager().decode('ascii')
    print(output)

finally:
    # Ensure the connection is closed even if an error occurs
    try:
        tel.close()
    except Exception as close_error:
        print(f"Failed to close the connection: {close_error}")
