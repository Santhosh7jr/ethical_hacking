import subprocess as sp

sp.call("ifconfig wlan0 down", shell=True)
sp.call("ifconfig wlan0 hw ether 00:11:22:33:44:55", shell=True)
sp.call("ifconfig wlan0 up", shell=True)