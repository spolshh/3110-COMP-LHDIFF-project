# file I/O simulation (no real files)
lines = ["first", "second", "third", "fourth", "fifth"]
for idx, val in enumerate(lines, start=1):
    print(idx, val)
# modify list
lines.append("sixth")
lines.insert(2, "inserted")
for l in lines:
    print("Line:", l)
#printing a line easily
for i in lines:
    if i == "second":
        print("we the best music")
    if i == "fourth":
        print("why u coming fast")
    n = 100
    for p in range(87,n):
        print(f"p prime is real {p}")
        print("just joking lol")
# finish