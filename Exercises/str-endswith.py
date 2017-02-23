import sys

s = sys.argv[1]
suffix = sys.argv[2]

i = len(suffix)

if s[len(s)-i:] == suffix:
   print True
else:
   print False
