import re

print(re.match("\d\d\d", "323") != None)

print(re.match("^\d\d\d\d-\d\d-\d\d$", "3233-22-11") != None)


print(float("2121.332"))
print(float(""))
