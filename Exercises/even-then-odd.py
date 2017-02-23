s = raw_input()

even = []
odd = []

while s != "end":
   num = int(s)
   if num % 2 == 0:
      even.append(s)
   else:
      odd.append(s)
   s = raw_input()

i = 0
while i < len(even):
   print even[i]
   i += 1
j = 0
while j < len(odd):
   print odd[j]
   j += 1
