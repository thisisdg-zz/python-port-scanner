import sys
import re
from subprocess import check_output
import time

HOST = input("IP : ")

# Default Range
start = 1
end = 65536

# Custom Range
edit = input("Edit Range?(Y/N)")

if edit == "y" or edit == "Y":
	print("Range : ")
	s = input()
	e = input()
	start = int(s) if len(s) > 0 else 1
	end =  int(e) if len(e) > 0 else 65536
	# print("e: " + e + "  s: " + s + "  end: " + str(end) + "  start: " + str(start))

#1
#	if s > e:
#		print("start is bigger than ")

# Loop to start scanning
for i in range(start, end):
    PORT = i
    
    command = "tnc " + HOST + r" -PORT " + str(PORT)
    print(command)

    status = check_output(["powershell.exe", command]).decode("utf-8")

	# Code to display the desired output [Currently non-functional]
    splitStrings = re.compile('[\r\t\n]+').split(status)
    for eachString in splitStrings:
        if eachString == "":
            splitStrings.remove(eachString)
    
    print(splitStrings)

    time.sleep(1)