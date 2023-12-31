#!/usr/bin/env python

import subprocess
import optparse
from pyfiglet import figlet_format
print(figlet_format("MAC Shift", font = "standard" ))

parser = optparse.OptionParser()

parser.add_option("-i", "--interface ", dest="interface", help="Interface to change its MAC Address")
parser.add_option("-m", "--mac ", dest="new_mac", help="New MAC Address")
(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

print("[+] Changing MAC address for " + interface + " to " + new_mac + " [+]")

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

print("[+] MAC Address changed successfully [+]")