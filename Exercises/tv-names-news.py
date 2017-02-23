import sys
lines = sys.stdin.readlines()

i = 0
while i < len(lines):
   line = lines[i]
   details = line.split()
   if details[1] == "BBC" and details[2] == "News" and not details[2] == "Newsline":
      name = details[0]
      print " ".join(details[0:])
   i += 1
