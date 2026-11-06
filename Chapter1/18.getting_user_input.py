import subprocess as sp

interface = " " + input("Interface: ") + " "
new_mac = " " + input("new_mac: ")

sp.call("ifconfig" + interface + "down", shell=True)
sp.call("ifconfig" + interface + "hw ether" + new_mac, shell=True)
sp.call("ifconfig" + interface + "up", shell=True)