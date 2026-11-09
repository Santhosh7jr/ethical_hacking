import subprocess as sp
import optparse

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

    print("Successfully changed the mac address to ", new_mac)

interface, new_mac = get_command_line_input()
change_mac_address(interface, new_mac)