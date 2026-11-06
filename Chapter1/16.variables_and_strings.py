import subprocess as sp

interface = " wlan0 "
new_mac = " 00:11:22:33:44:55"

sp.call("ifconfig" + interface + "down", shell=True)
sp.call("ifconfig" + interface + "hw ether" + new_mac, shell=True)
sp.call("ifconfig" + interface + "up", shell=True)