seen = []

line = raw_input()
while line != "end":
   i = 0
   while i < len(seen) and seen [i] != line:
      i += 1
   have_seen_line = i < len(seen)

   if not have_seen_line:
      seen.append(line)

   line = raw_input()
print seen
