import urllib.request
import re

url = "https://www.summet.com/dmsi/html/codesamples/addresses.html"

response = urllib.request.urlopen(url)

html = response.read()

htmlstr = html.decode()

phone = re.findall(r'\(\d{3}\) \d{3}-\d{4}',htmlstr)
#print (phone)

#sample = "()[]828394jaiosjdfilfioujweASDFJAISDFISDD

#m = re.findall(r'\[\]',sample)
#print (m)
names = re.findall(r'<li>([A-Z][a-z]*\s[A-Z][a-z]*)',htmlstr)
print (len(names))


addresses = re.findall(r'',htmlstr)
#print (addresses)