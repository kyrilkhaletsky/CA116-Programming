s = raw_input()
ints = []

while s != "end":
   s = int(s)
   ints.append(s)
   s = raw_input()

i = 0

while i < len(ints) and ints[i] % 2 == 0:
   i += 1
if i < len(ints):
   print i
