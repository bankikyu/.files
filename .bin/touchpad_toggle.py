#!/usr/bin/python

import commands
import re

touchpadoff_str = commands.getoutput("synclient -l | grep TouchpadOff")

if re.search('1', touchpadoff_str):
  status_tuple = commands.getstatusoutput("synclient TouchpadOff=0")
else:
  status_tuple = commands.getstatusoutput("synclient TouchpadOff=1")

if status_tuple[0] is not 0:
  print "Something went wrong... synclient exited with status ", status_tuple[0]
  print "Command output was:\n", status_tuple[1]
