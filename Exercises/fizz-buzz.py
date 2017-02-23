n = input("Enter positive n: ")

i = 0

while i < n:
   
   if i % 15 == 0:
      print "fizz-buzz"
   elif i % 3 == 0:
      print "fizz"
   elif i % 5 == 0:
      print "buzz"
   else:
   i += 1
   
