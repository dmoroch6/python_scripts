import argparse
import re
import signal
from termcolor import colored
import subprocess
from concurrent.futures import ThreadPoolExecutor
import sys


def def_handler(sig,frame):
    print(colored(f"\n EXITING PROGRAM!!...", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def get_arguments():
    parser = argparse.ArgumentParser(description="Discover host checking ICMP packages.")
    parser.add_argument("-t", required=True, dest="target", help="Host or network range to scan")

    args = parser.parse_args()

    return args.target

def parse_target(target_str):

    target_str_splitted = target_str.split(".") #192.168.1.1-100
    first_three_octets = '.'.join(target_str_splitted[:3]) # we are validating the first 3 octets 

    if len(target_str_splitted)==4:
        if "-" in target_str_splitted[3]:
            start, end = target_str_splitted[3].split('-')
            return [f"{first_three_octets}.{i}"for i in range(int(start),int(end)+1)]

        else:
            return [target_str]
    else:
        print(colored(f'IP format/range is not valid',"red"))

def host_discovery(target):

        try:
            ping = subprocess.run(["ping", "-c","1", target], timeout=1, stdout=subprocess.DEVNULL)

            if ping.returncode == 0:
                    print(colored(f"\nThe following ip: {target} is active" , "green"))
        except subprocess.TimeoutExpired:
            pass
            
def main():
    target_str = get_arguments()
    targets = parse_target(target_str)

    print(colored(f'\n Host in the network','green'))
    max_threads=250
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
       executor.map(host_discovery,targets)

if __name__=="__main__":
    main()
