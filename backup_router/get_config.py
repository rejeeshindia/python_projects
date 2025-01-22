import os 
import glob
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
    print(f"Current time = {timestamp}")
    backupfilename=f"backup_{timestamp}.cfg"
    print(backupfilename)
    print("Starting Backup")
    with open(backupfilename,"w") as backup_file:
        backup_file.write(running_config)

def clean_backup():

    files_to_delete=glob.glob("backup*")
    print(f"Existing backups - ")
    for file in files_to_delete:
        print(file)

    time.sleep(1)
    for files in files_to_delete:
        print ("Deleting file - ")
        os.remove(file)








def main():

    while True:
        print("\n1. Backup\n")
        print("\n2. Run a cmd \n")
        print("\n4. Delete backups \n")
        print("\n5. Exit\n")

        choice = input("Enter the selection - ")

        if choice == "1":
            backup()
        
        if choice == "2":
            cmd_and_display()
        if choice == "4":
            clean_backup()

        elif choice == "5":
            print("Exiting")
            break

    






if __name__ == "__main__":

    '''cmd_and_display()'''
    '''backup()'''
    main()