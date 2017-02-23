import sys
lines = sys.stdin.readlines()
s = sys.argv[1:]

i = 0
while i < len(lines):
   line = lines[i]
   details = line.split()
   if " ".join(details[1: len(s) +1]) == " ".join(s):
      name = details[0:]
      print " ".join(details[0:])
   i += 1
