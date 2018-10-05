import re
def parse_address(input_file):
	file = open(input_file, 'r')
	lines = file.readlines()
	file.close()

	for each in lines:
		for match in re.findall(r'\d{1,3}[A-Za-z\\/-][\w\\/-]*',each):
			print ("House/Flat Number: ", match)

#parse_address()