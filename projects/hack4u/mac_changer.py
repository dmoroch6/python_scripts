 #!/bin/bash/env python3
import argparse
import subprocess
import re
from termcolor import colored

def get_arguments():
    parser = argparse.ArgumentParser(description="Change a interfaz mac address")
    parser.add_argument("-i","--insert", required=True, dest="interface", help="Network interface name")
    parser.add_argument("-m","--mac", required=True, dest="mac_address", help="Device current mac address")

    return parser.parse_args()

def is_valid_input(interface,mac_address):
    is_valid_interface =     re.fullmatch(r'wlp\d+s\d+f\d+', interface) ### This line will not take other interfaces than mine :p. is it risky? :,(
    is_valid_mac_address = re.match(r'([A-Fa-f0-9]{2}[:]){5}[A-Fa-f0-9]{2}$',mac_address) ## This line will take all valid mac addresses.

    return is_valid_interface and is_valid_mac_address

def change_mac_address(interface, mac_address):

    if is_valid_input(interface, mac_address): # Validate if input is in a correct syntax 
        subprocess.run(["ifconfig", interface,"down"])
        subprocess.run(["ifconfig", interface, "hw","ether", mac_address])
        subprocess.run(["ifconfig", interface, "up"])
        print(colored("Mac changed succcesfully", "green"))
    else:
        print(colored("Data not correct","red"))
        
def main():
    args=get_arguments()
    change_mac_address(args.interface, args.mac_address)


if __name__=='__main__':
    main()
