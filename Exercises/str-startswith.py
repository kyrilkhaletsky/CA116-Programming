import sys

s = sys.argv[1]
prefix = sys.argv[2]
i = len(prefix)

if s[i:] == prefix:
   print True
else:
   print False
