ints = []

s = raw_input()
while s != "end":
   n = int(s)
   ints.append(n)
   s = raw_input()

i = 1

while i < len(ints) and ints[i-1] <= ints[i]:
   i += 1

if i < len(ints):
   print "Not Sorted"
else:
   print "Sorted"
