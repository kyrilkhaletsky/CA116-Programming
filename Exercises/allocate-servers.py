s = raw_input()
servers = []
duration = 1000

while s != "end":
   start_time = int(s)
   i = 0
   while i <len(servers) and start_time < servers[i]:
      i += 1
   if i < len(servers):
      servers[i] = start_time + duration
   else:
      servers.append(start_time + duration)
   s = raw_input()
print len(servers)

