import sys
sentence = sys.argv[1:]
word = {
   "one" : "eins",
   "two" : "zwei",
   "three" : "drei",
   "four" : "vier",
   "five" : "funf",
   "six" : "sechs",
   "seven" : "sieben",
   "eight" : "acht",
   "nine" : "neun",
   "ten" : "zehn",
}

i = 0
while i < len(sentence):
   if sentence[i] in word:
      sentence[i] = word[sentence[i]]
   i += 1
print " ".join(sentence)
   
   
