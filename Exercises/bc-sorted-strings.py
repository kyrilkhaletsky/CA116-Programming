lines = []

s = raw_input()
while s != "end":
   lines.append(s)
   s = raw_input()

i = 1

while i < len(s) and lines[i-1] <= lines [i]:
   i += 1

if i < len(lines):
   print "Not Sorted"
else:
   print "Sorted"
