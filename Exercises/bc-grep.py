import sys
n = sys.argv[1]

line = []
s = raw_input()

while s != "end":
   line.append(s)
   s = raw_input()

i = 0
while i < len(line):
   if s.find(n):
      i += 1
   else:
      print line[i]
