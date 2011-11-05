import telnetlib, urllib2, sys
t = telnetlib.Telnet("127.0.0.1", 10010)
print "opening: ", sys.argv[1]
t.write(urllib2.urlopen(sys.argv[1]).read())
print t.read_all()
