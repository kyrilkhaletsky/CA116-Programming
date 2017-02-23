import sys
lines = sys.stdin.readlines()

i = 0
while i < len(lines):
   line = lines[i]
   details = line.split()
   name = details[1:]
   time = line.split("-")
   print time[0], " ".join(details[1:])
   i += 1
