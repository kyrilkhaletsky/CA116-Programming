import sys
with open("translation.txt") as f:
   for line in f.readlines():
      sys.stdout.write(line)
