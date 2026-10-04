room = "12415大学院講義室"
f = open("fd.txt", "a", encoding="utf-8")
f.write("\r"+ room)
f.close()
f = open("fd.txt", "r", encoding="utf-8")
s = f.read()
print(s)
f.close()
