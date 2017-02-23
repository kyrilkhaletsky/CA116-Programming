n = input("Enter n: ")
digits = 1
while 2 ** digits <= n:
   digits += 1

i = 0

while i < digits:
   power = 2 ** (digits -i -1)
   if power <= n:
      print 1
      n = n - power
   else:
      print 0
   i += 1
   

