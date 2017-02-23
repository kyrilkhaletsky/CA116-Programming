import sys
lines = sys.stdin.readlines()
total = 0.0
i = 0
while i < len(lines):
   line = lines[i]
   details = line.split()
   mark = int(details[4])
   total = total + mark
   i += 1

if 0 < len(lines):
   print total / len(lines)
