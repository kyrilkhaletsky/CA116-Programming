s = raw_input()
ints = []

while s != "end":
   s = int(s)
   ints.append(s)
   s = raw_input()

i = 0

while i < len(ints):
   if ints[i] % 2 == 0:
      print ints[i]
   i += 1
