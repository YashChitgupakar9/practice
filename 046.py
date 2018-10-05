import re, urllib
import urllib.request 
sites = "google cnn bcc yahoo cricbuzz ".split()		
for each in sites:
	print("finding: " + each)
	
	d = urllib.request.urlopen("http://" + each + ".com")
	file = d.read()
	#print(file)
	title = re.findall("<title>.*</title>",str(file),re.I|re.M)
	print(title[0])
	

  