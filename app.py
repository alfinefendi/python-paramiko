import paramiko
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch environment variables
host = os.getenv('HOST')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

# Print out the values to verify
print(f"Loaded HOST: {host}")
print(f"Loaded PASSWORD: {password}")

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try :
    ssh_client.connect(hostname=host, username=username, password=password)
    print("Connected to the server successfully!")
    command = 'cd /var/www && ls'
    stdin,stdout,stderr = ssh_client.exec_command(command)
    print(stdout.read().decode())
    print(stderr.read().decode())

finally :
    ssh_client.close()
