import subprocess as sp

interface = input("Interface: ")
new_mac = input("new_mac: ")

sp.call(["ifconfig", interface, "down"])
sp.call(["ifconfig", interface, "hw", "ether", new_mac])
sp.call(["ifconfig", interface, "up"])