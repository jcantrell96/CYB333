# Author Jordan Cantrell
# Project Option 2
#12/21/2024

# Importing SCAPY, IP and UDP to attack target IP

from scapy.all import IP, UDP, send

# Define the destination and payload
Mission_Target = input('Enter website or IP address to scan: ')  # Replace with your target IP
destination_port = 23          # Replace with your target port
payload = "Blue Team Attack"               # Data to send

# Create the packet to send to ATTACK Target
packet = IP(dst=Mission_Target) / UDP(dport=destination_port) / payload

# Send the packet to target
send(packet)
print("Packet sent!")



# Import the socket, time, and pyflight modules for python3.
import socket
import time
import pyfiglet
Project_CYB3333_banner = pyfiglet.figlet_format("Happy Holiday Cyber Blue Team! Please inform COC of Testing")
print(Project_CYB3333_banner )
Portsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Prompting Cyber team for attack target
Mission_Target = input('Enter website or IP address to scan: ')
# Displaying attack scan has initated
Mission_Target_ip = socket.gethostbyname(Mission_Target)
print('Scanning target:', Mission_Target_ip)
# Creates the Blue_Team_Port_Scan function for scanning ports.
def Blue_Team_port_scan(port):
    try:
        Portsocket.connect((Mission_Target_ip, port))
        return True
    except:
        return False

Attack_initiation = time.time()
# This will attack ports 0-1024 that are common for cyber events.
for port in range(1024):
    if Blue_Team_port_scan(port):
        print(f'port {port} is open, This is a finding, Please Notify CTO!')
    else:
        print(f'port {port} is closed, This is not a finding!')
Stop_attack = time.time()
print(f'Time taken {Stop_attack - Attack_initiation:.2f} seconds')
# Closing the test with a goodbye.
Project_CYB3333_banner2 = pyfiglet.figlet_format("Good Work Cyber Blue Team! Please inform COC of Testing")
print(Project_CYB3333_banner)

#importing modules that are used to for the windows hosts

import subprocess
import re

def Collect_Analyze_logs():
    # This will use the  'wevtutil' command to query the Windows Event Logs that are used for vulnerbility scanner
    wincommand = 'wevtutil qe Security /q:"*[System [(EventID=4625)]]" /f:text /rd:true /c:1'
    findings = subprocess.run(wincommand, capture_output=True, text=True, shell=True)

    # coolected_logs collects the logs needed for cyber investigation that are useful
    Collected_logs = re.findall(r'Event[^\r\n]*', findings.stdout)

    # inspect the collected logs.
    for finding in Collected_logs:
        if "Failure" in finding and "Logon Type: 3" in finding:
            print("This is a finding! Let's dig deeper!")
            print(finding)

if __name__ == "__main__":
    Collect_Analyze_logs()
