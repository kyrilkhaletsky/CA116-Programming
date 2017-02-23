# Example: "3 NZ, New Zealand" < "21 IE, Ireland".
# For equal counts, use string comparison on the country; otherwise,
# use integer comparison on the counts.
def less_than_counts(a,b):
   [ ca, na ] = a.split(None,1) # E.g.: "3 NZ, New Zealand" -> [ "3", "NZ, New Zealand" ]
   [ cb, nb ] = b.split(None,1)
   if ca == cb:
      return na < nb
   else:
      return int(ca) < int(cb)

# This version of selection sort assumes that the list is a list of strings,
# and that the first token in each string is an integer, and that the sort order
# is increasing numeric order.
def selection_sort(a):
   i = 0
   while i < len(a):
      p = i
      j = i + 1
      while j < len(a):
         # Example: "3 NZ, New Zealand" < "21 IE, Ireland".
         if less_than_counts(a[j],a[p]):
            p = j
         j = j + 1

      tmp = a[p]
      a[p] = a[i]
      a[i] = tmp

      i = i + 1

# Read in ip-to-country mapping.
with open("geo-ip-mapping.txt") as f:
   lines = f.readlines()

geo = {}

i = 0
while i < len(lines):
   line = lines[i]
   details = line.split()
   ip = details[0]
   country = " ".join(details[1:])
   geo[ip] = country
   i += 1
	
# Prepare in ip-to-country mapping (a dictionary).


# Read in Apache log.
with open("apache.log") as f:
   lines = f.readlines()

count = {}
i = 0
while i < len(lines):
   line = lines[i]
   details = line.split()
   ip = details[5]
   status = details[1]
   page = details[7]
   country = geo[ip]
   if status == "200" and page == "/":
      if country not in count:
         count[country] = 0
      count[country] = count[country] + 1
   i += 1
   
lines = []

for country  in count:
   lines.append(str(count[country]) + " "+country)

selection_sort(lines)

i = 0
while i < len(lines):
   print lines[i]
   i += 1
# Process Apache log.

# Prepare, sort and output the output lines.
