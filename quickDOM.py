#!/usr/local/bin/python3.5
# This script is contigency plan for eDOMv2.Service replacement
# Author: Shahruddin Abu Bakar
# Created on Oct 08, 2018 for fastDOM project
# .decode() is to remove the byte b' indicator
# Original script is from sort.py
# Tested OK on 29 Oct 2018
################################################################
import sys, os, subprocess, glob
import re, pendulum
from lxml import etree
from datetime import datetime, date, time, timedelta
from SNfindv2 import eDOMv2

#srcDir = "/eDOM/XML2"
srcDir = '/eDOM/XML_check/'
#targetDir = "/eDOM/XML_backup"

import os    

name_list = os.listdir(srcDir)
full_list = [os.path.join(srcDir,i) for i in name_list]
time_sorted_list = sorted(full_list, key=os.path.getmtime)

print(time_sorted_list)

for xmlfiles in time_sorted_list:
 tree = etree.parse(os.path.join(targetDir, xmlfiles))
 root = tree.getroot()
 STRTsernum  = root.find('sernum').text

 uuttype = root.find('uuttype').text
 regex = r"(\d[1-9]+[-]+[0-9]+[-]\d*)"
 match = re.search(regex, uuttype)
 uuttype = match.group(0)

 endtime = root.find('testtime').text
 testtime = root.find('tottime').text
 if testtime =="":
  testtime = "0"
 rev = root.find('rev').text
 wip = root.find('wip').text
 cell = root.find('cell').text
 shiftpattern = root.find('test').text


 rectime = pendulum.parse(endtime, tz='Asia/Singapore')                     # 2018-03-07T21:10:23+08:00
 rectimeSG = datetime.strftime(rectime, '%Y-%m-%dT%H:%M:%S.%f')             # 2018-03-07T21:10:23.000000
 rectimePDT = rectime.in_timezone('US/Pacific')
 rectimePDTx = datetime.strftime(rectimePDT , '%Y-%m-%dT%H:%M:%S.%f')
 
 # Reformat
 DOMobject = datetime.strptime(str(rectimePDTx), '%Y-%m-%dT%H:%M:%S.%f')
 DOMrectime = DOMobject.strftime('%Y-%m-%d-%H:%M:%S')			    # 2018-10-02-13:29:02


 # Print it out
 print(STRTsernum)
 print(uuttype)
 print("Actual Time: "+rectimeSG)	#2018-10-17T13:41:28.000000
 print("DOM Time :"+rectimePDTx)	#2018-10-16T22:41:28.000000
 print("DOM Format :"+DOMrectime)	#2018-10-02-13:29:02

 #Example of eDOM.Service syntax
 # ssh jpecppus@10.79.29.84 "agen.exe edom JAE221404EY 73-12012-22 A0 50399358 2018040307151915 21 2018-10-02-13:29:02"
 print("TO DOM :"+STRTsernum+" "+uuttype+" "+rev+" "+wip+" "+shiftpattern+" "+cell+" "+DOMrectime)
 # Finally, send data to eDOM using SSH method
 eDOMv2(STRTsernum,uuttype,rev,wip,shiftpattern,cell,DOMrectime)
 print("...................")
