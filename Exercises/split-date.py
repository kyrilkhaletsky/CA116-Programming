import sys
line = sys.stdin.readline()
line = line.strip()
date = line.split("/")


i = 0

while i < len(date):
   sys.stdout.write(date[i] + "\n")
   i += 1

