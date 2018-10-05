text = "inform him with latest information"

import re

match = re.findall("[^inform]*im",text)

print(match)
yash = re.findall("\w",text)
print(yash)

phone = "6789-466-678, 7893-383-389, 2443-323-232 4234 6394895839 28209384839"

boom = re.findall("[6][0-9]{3}-\d{3}-678",phone)
print(boom)
numbers = re.findall('\d{10}',phone)	
print(numbers)