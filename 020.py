f = open("Sample.txt",'r+')

#print(f.readlines())
f.read()
f.write("gymnastics a game of flexibility \n wresling is all about showmanship\n")
f.flush()
f.close()

f1 = open("Sample.txt", 'r')
print (f1.read())
