import sys
line = sys.stdin.readline()
words = line.split()

i = 0
while i < len(words):
   sys.stdout.write(words[i] + "\n")
   i += 1
