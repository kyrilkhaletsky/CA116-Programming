def get_minutes(k):
   s = k.split(":")
   h = s[0]
   h = int(h)
   m = s[1]
   m = int(m)
   h = h * 60
   return h + m

def main():
   print get_minutes("0:05")
   print get_minutes("00:05")
   print get_minutes("1:05")
   print get_minutes("06:05")

if __name__ == "__main__":
   main()
