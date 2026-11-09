import subprocess as sp
import optparse
import re

def get_command_line_input():

    parser = optparse.OptionParser()    

    parser.add_option("-i", "--interface", dest="interface", help="get user input for interface.")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address.")

    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("Please specify the interface name")

    if not options.new_mac:
        parser.error("please specify the new mac address")

    return options.interface, options.new_mac

def change_mac_address(interface, new_mac):

    sp.call(["ifconfig", interface, "down"])
    sp.call(["ifconfig", interface, "hw", "ether", new_mac])
    sp.call(["ifconfig", interface, "up"])

def get_current_mac():

    result = sp.check_output(["ifconfig", interface])

    if not result:
        return

    current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(result))[0]

    return current_mac

interface, new_mac = get_command_line_input()
change_mac_address(interface, new_mac)

current_mac = get_current_mac()

if not current_mac:
    raise("MAC Address Extraction Failed!")

if current_mac == new_mac:
    print("Mac Address Changed Successfully to ", new_mac)

