#!/usr/local/bin/python3.5
# This cli is to search SNfind from shell
# Completed from Jan 28, 32017
# By Shahruddin for Test Engineering
# DO NOT MODIFY THIS SCRIPT WITHOUT BUYOFF WITH searchfastDOMdb.py SCRIPT !!!
# USED BY searchfastDOMdb.py
# Update: Apr 19, 2018: use jpecppus account to avoid passwd change issue
# SNFindv2 : Include RecordDate improvement.
###############################################################

import paramiko
import sys
jabp2dom1 = {"username": "jpecppus",
       "hostname": "10.79.29.84"}
jabp2dom2 = {"username": "jpecppus",
       "hostname": "10.79.29.241"}

def SNfind(sernum):
	remote = paramiko.SSHClient()
	remote.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	remote.load_system_host_keys()
	#command = "snfind %s 0 | grep PASTE | awk '{print $1,$2,$6,$7,$8,$13,$15,$17}'" % (sys.argv[1])
	command = "snfind %s 0 | grep PASTE | awk '{print $1,$2,$6,$7,$8,$13,$15,$17}'" % (sernum)
	remote.connect(**jabp2dom1)
	stdin, stdout, stderr = remote.exec_command(command, timeout=5)
	result = stdout.read().decode()
	remote.close()

	if result:
	 pass
	 #print(result)
	else:
	 remote = paramiko.SSHClient()
	 remote.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	 remote.load_system_host_keys()
	 #sys.argv[1] = 'JAE22040CVV'
	 #print("Searching in JABP2DOM2: ", sys.argv[1])
	 command = "snfind %s 0 | grep PASTE | awk '{print $1,$2,$6,$7,$8,$13,$15,$17}'" % (sernum)
	 remote.connect(**jabp2dom2)
	 stdin, stdout, stderr = remote.exec_command(command, timeout=5)
	 result = stdout.read().decode()
	 remote.close()
	 if result:
	  pass
	 else:
	  result = "NRF"
	 #print(result)
	return(result)

def eDOM(sernum,uuttype,rev,wip,shiftpattern,cell):
	remote = paramiko.SSHClient()
	remote.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	remote.load_system_host_keys()
	command = "agen.exe edom %s %s %s %s %s %s" % (sernum,uuttype,rev,wip,shiftpattern,cell)
	remote.connect(**jabp2dom2)
	stdin, stdout, stderr = remote.exec_command(command, timeout=5)
	result = stdout.read().decode()
	remote.close()

def eDOMv2(sernum,uuttype,rev,wip,shiftpattern,cell,DOMrectime):
        remote = paramiko.SSHClient()
        remote.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        remote.load_system_host_keys()
        command = "agen.exe edom %s %s %s %s %s %s %s" % (sernum,uuttype,rev,wip,shiftpattern,cell,DOMrectime)
        remote.connect(**jabp2dom2)
        stdin, stdout, stderr = remote.exec_command(command, timeout=5)
        result = stdout.read().decode()
        remote.close()
