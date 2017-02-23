import sys
lines = sys.stdin.readlines()

i = 0
while i < len(lines):
   line = lines[i]
   details = line.split()
   mark = details[4]
   sys.stdout.write(mark + "\n")
   i += 1
