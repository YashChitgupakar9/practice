worldcup ={"europe":{"belgium":"kevin debryne","germany":"kroos","spain":"isco","france":"grezman"},"southamerica":{"brazil":"neymar","argentina":"messi","columbia":"james","uruguay":"suazez"},"africa":{"senegal":"mane","egypt":"salah","ivorycoast":"zaha","nigeria":"iwobi"}}

print(worldcup["europe"]["belgium"])
print(worldcup["africa"]["nigeria"])
countrylist = worldcup["southamerica"].values()
print(countrylist)
for key,val in worldcup["southamerica"].items():
    print(key, "=>", val)
print(worldcup["europe"]["france"])
