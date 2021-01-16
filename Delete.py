import os
import sys
import subprocess
import time

exec = "C:/Program Files/OpenVPN/bin/openvpn-gui.exe"
args = "--command connect client.ovpn"
local_ip = "127.0.0.1"
port = "25340"

def get_pid(port_id):
	os.system("netstat -ano | findstr {}:{} > out.txt".format(local_ip, port_id))
	file = open("out.txt", "r")
	processes_id = []
	for line in file:
		processes_id.append(line.split()[-1])
	file.close()
	os.system("del out.txt")
	return set(processes_id)
	


def check_processes_by_port(port_id):
	for pid in get_pid(port_id):
		os.system("taskkill /f /pid {}".format(pid))


def main():
	check_processes_by_port(port)
	#os.system("\"{}\" {}".format(exec, args))
	os.system('echo Conectado a vpn')


main()