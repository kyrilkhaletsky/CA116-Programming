import sys
lines = sys.stdin.readlines()
longest_line = ""

i = 0
while i < len(lines):      
   line = lines[i]
   if len(longest_line) < len(lines[i]):
      longest_line = line[i]
   i = i + 1

print longest_line
