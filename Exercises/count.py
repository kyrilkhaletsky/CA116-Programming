import sys

haystack = sys.argv[1]
needle = sys.argv[2]

count = 0
i = 0

while i < len(haystack) - len(needle):
   if haystack[i +len(needle)] == needle:
      count += 1
      i = i + len(needle)
   else:
      i += 1

print count
