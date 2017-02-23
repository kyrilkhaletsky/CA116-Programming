import sys

s = sys.argv[1]

i = len(s) - 1

while i > 0 and s[i].isspace():

   i -= 1

print s[0:i + 1]

