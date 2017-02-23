import sys

s = sys.argv[1]
y = ""

i = 0

while i < len(s):
   if s[i].islower():
      y = y + "x"
   elif s[i].isupper():
      y = y + "X"
   i += 1
print y
