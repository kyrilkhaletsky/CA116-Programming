import sys

s = sys.argv[1]

i = 0
n = len(s) - 1

while i < len(s) and  s[i].isspace():
   i += 1


while n > 0 and s[i].isspace():

   n -= 1

print s[i:n + 1]

