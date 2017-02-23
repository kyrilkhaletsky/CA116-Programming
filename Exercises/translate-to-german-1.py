import sys
word = sys.argv[1]

words = {
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

print "The German for", word, "is", words[word] + "."
   
   
