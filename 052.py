target_string = "From: Rjkjskldjf@ac.uk.com yash@gmail.com rishab@yahoo.co.in Aarti234@modak.co.in.us.uk subject To: "
import re
email = re.findall("\S+@\S+",target_string)
print (email)