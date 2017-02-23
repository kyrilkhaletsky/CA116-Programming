s = raw_input()
ints = []

while s != "end":
   s = int(s)
   ints.append(s)
   s = raw_input()

i = 0

while i < len(ints):
   if ints[len(ints) -1-i] % 2 == 0:
      print ints[len(ints) -1 -i]
   i += 1
