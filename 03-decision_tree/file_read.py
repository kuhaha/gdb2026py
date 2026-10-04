f = open("fd.txt", "r", encoding="utf-8")
s = f.read()
print(s)
f.close()
f = open("fd.txt", "r", encoding="utf-8")
for line in f:
    print("> " + line)
f.close()
