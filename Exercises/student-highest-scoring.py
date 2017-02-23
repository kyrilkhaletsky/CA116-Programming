import sys
lines = sys.stdin.readlines()
mark = []
i = 0
while i < len(lines):
   line = lines[i]
   details = line.split()
   mark.append(details[4])
   i += 1
   
print mark
   
