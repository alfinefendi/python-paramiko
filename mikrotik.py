import paramiko
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch environment variables
host = os.getenv('HOST')
port = os.getenv('PORT')
username = os.getenv('USER')
password = os.getenv('PASSWORD')

# Print out the values to verify
print(f"Loaded HOST: {host}")
print(f"Loaded PASSWORD: {password}")
print(f"Loaded USERNAME: {username}")

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try :
    ssh_client.connect(hostname=host, port=port, username=username, password=password)
    print("Connected to the server successfully!")
    setStaticIp = '/ip address add address=192.168.1.10/24 interface=ether1 comment="Static IP for LAN"'

    # stdin, stdout, stderr = ssh_client.exec_command(setStaticIp)
    stdin, stdout, stderr = ssh_client.exec_command('/ip address print')
    print(stdout.read().decode())
    # print(stderr.read().decode())

finally :
    ssh_client.close()
