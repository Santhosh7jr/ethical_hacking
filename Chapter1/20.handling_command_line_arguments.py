import subprocess as sp
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="get user input for interface.")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address.")

(options, arguments) = parser.parse_args()

print(options)

interface = options.interface
new_mac = options.new_mac

sp.call(["ifconfig", interface, "down"])
sp.call(["ifconfig", interface, "hw", "ether", new_mac])
sp.call(["ifconfig", interface, "up"])