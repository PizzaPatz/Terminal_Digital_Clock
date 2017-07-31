from time import sleep
from os import system
from datetime import datetime
import time
import threading



def clear():
	system("cls")

r1 = {
	"1":
	"    \u2588\u2588",
	"2":
	"\u2588\u2588\u2588\u2588\u2588\u2588",
	"3":
	"\u2588\u2588\u2588\u2588\u2588\u2588",
	"4":
	"\u2588\u2588  \u2588\u2588",
	"5":
	"\u2588\u2588\u2588\u2588\u2588\u2588",
	"6":
	"\u2588\u2588\u2588\u2588\u2588\u2588",
	"7":
	"\u2588\u2588\u2588\u2588\u2588\u2588",
	"8":
	"\u2588\u2588\u2588\u2588\u2588\u2588",
	"9":
	"\u2588\u2588\u2588\u2588\u2588\u2588",
	"0":
	"\u2588\u2588\u2588\u2588\u2588\u2588",
	":":
	"      "
}
r2 = {
	"1":
	"    \u2588\u2588",
	"2":
	"    \u2588\u2588",
	"3":
	"    \u2588\u2588",
	"4":
	"\u2588\u2588  \u2588\u2588",
	"5":
	"\u2588\u2588    ",
	"6":
	"\u2588\u2588    ",
	"7":
	"    \u2588\u2588",
	"8":
	"\u2588\u2588  \u2588\u2588",
	"9":
	"\u2588\u2588  \u2588\u2588",
	"0":
	"\u2588\u2588  \u2588\u2588",
	":":
	"  \u2588\u2588  "
}

r3 = {
	"1":
	"    \u2588\u2588",
	"2":
	"\u2588\u2588\u2588\u2588\u2588\u2588",
	"3":
	"\u2588\u2588\u2588\u2588\u2588\u2588",
	"4":
	"\u2588\u2588\u2588\u2588\u2588\u2588",
	"5":
	"\u2588\u2588\u2588\u2588\u2588\u2588",
	"6":
	"\u2588\u2588\u2588\u2588\u2588\u2588",
	"7":
	"    \u2588\u2588",
	"8":
	"\u2588\u2588\u2588\u2588\u2588\u2588",
	"9":
	"\u2588\u2588\u2588\u2588\u2588\u2588",
	"0":
	"\u2588\u2588  \u2588\u2588",
	":":
	"      "
}

r4 = {
	"1":
	"    \u2588\u2588",
	"2":
	"\u2588\u2588    ",
	"3":
	"    \u2588\u2588",
	"4":
	"    \u2588\u2588",
	"5":
	"    \u2588\u2588",
	"6":
	"\u2588\u2588  \u2588\u2588",
	"7":
	"    \u2588\u2588",
	"8":
	"\u2588\u2588  \u2588\u2588",
	"9":
	"    \u2588\u2588",
	"0":
	"\u2588\u2588  \u2588\u2588",
	":":
	"  \u2588\u2588  "
}

r5 = {
	"1":
	"    \u2588\u2588",
	"2":
	"\u2588\u2588\u2588\u2588\u2588\u2588",
	"3":
	"\u2588\u2588\u2588\u2588\u2588\u2588",
	"4":
	"    \u2588\u2588",
	"5":
	"\u2588\u2588\u2588\u2588\u2588\u2588",
	"6":
	"\u2588\u2588\u2588\u2588\u2588\u2588",
	"7":
	"    \u2588\u2588",
	"8":
	"\u2588\u2588\u2588\u2588\u2588\u2588",
	"9":
	"\u2588\u2588\u2588\u2588\u2588\u2588",
	"0":
	"\u2588\u2588\u2588\u2588\u2588\u2588",
	":":
	"      "
}


print(r1['1'],r1['2'],r1[':'])
print(r2['1'],r2['2'],r2[':'])
print(r3['1'],r3['2'],r3[':'])
print(r4['1'],r4['2'],r4[':'])
print(r5['1'],r5['2'],r5[':'])


print(r1['7'],r1['2'])
print(r2['7'],r2['2'])
print(r3['7'],r3['2'])
print(r4['7'],r4['2'])
print(r5['7'],r5['2'])

def terminator():
	for e in event.get():
		if e.type == KEYDOWN:
			if (e.key == K_a):
				print("A was pressed")


def clock():
	while 1:
		try:
			clear()
			print("------------------------------------------------------------------")
			print()
			ctime = datetime.now()
			hour = str(ctime.hour)
			minute = str(ctime.minute)
			second = str(ctime.second)	
			if(len(hour)<2):
				hour = "0"+hour
			if(len(minute)<2):
				minute = "0"+minute
			if(len(second)<2):
				second = "0"+second
			print("  ",r1[hour[0]],r1[hour[1]],r1[':'],r1[minute[0]],r1[minute[1]],r1[':'],r1[second[0]],r1[second[1]])
			print("  ",r2[hour[0]],r2[hour[1]],r2[':'],r2[minute[0]],r2[minute[1]],r2[':'],r2[second[0]],r2[second[1]])
			print("  ",r3[hour[0]],r3[hour[1]],r3[':'],r3[minute[0]],r3[minute[1]],r3[':'],r3[second[0]],r3[second[1]])
			print("  ",r4[hour[0]],r4[hour[1]],r4[':'],r4[minute[0]],r4[minute[1]],r4[':'],r4[second[0]],r4[second[1]])
			print("  ",r5[hour[0]],r5[hour[1]],r5[':'],r5[minute[0]],r5[minute[1]],r5[':'],r5[second[0]],r5[second[1]])
			print()
			print("                          ",ctime.month,"/",ctime.day,"/",ctime.year)
			print("------------------------------------------------------------------")
			print("CTRL + C to exit")
			sleep(0.5)
		except KeyboardInterrupt:
			sleep(0.1)
			break;	



clock()