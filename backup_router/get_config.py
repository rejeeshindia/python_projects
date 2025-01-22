import os 
import time
import netmiko
from netmiko import ConnectHandler
from datetime import datetime






device = {"device_type":"cisco_ios",
          "host":"192.168.1.20",
          "username":"cisco",
          "password":"cisco"}


def connect_device(cmd):

    try:
            
        connection = ConnectHandler(**device)
        print(f"\nConnecting to {device['host']}....")
        time.sleep(1)
        print(f"\nConnected to {device['host']}....")
    except Exception as e:
        print(f"\nFailed to connect to  {device['host']} with Error {e}")

    output=connection.send_command(cmd)
    return output

def cmd_and_display():
    
    cmd = input("Enter the cmd\n")


    output=connect_device(cmd)
    print(f"\nOutput of {cmd} = {output}\n")

def backup():

    running_config=connect_device('show run')
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    print(f"CUrrent time = {timestamp}")
    backupfilename=f"backup_{timestamp}.cfg"
    print(backupfilename)
    with open(backupfilename,"w") as backup_file:
        backup_file.write(running_config)


def main():

    while True:
        print("\n1. Backup\n")
        print("\n2. Run a cmd \n")
        print("\n3. Exit\n")

        choice = input("Enter the selection - ")

        if choice == "1":
            print("Starting Backup")
            backup()
        
        if choice == "2":
            cmd_and_display()

        elif choice == "3":
            print("Exiting")
            break

    






if __name__ == "__main__":

    '''cmd_and_display()'''
    '''backup()'''
    main()