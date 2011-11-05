import subprocess, sys, urllib2
print "parsing: ", sys.argv[1]
print subprocess.check_output(["java", "-jar", "tika-app-0.10.jar", "-j", "-d", "-T",
    sys.argv[1]])
#tika = subprocess.Popen(["java", "-jar", "tika-app-0.10.jar", "-j", "-d", "-T"])
#print tika.communicate(urllib2.urlopen(sys.argv[1]).read())[0]
