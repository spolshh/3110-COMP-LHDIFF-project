# file I/O simulation (no real files)
lines = ["first", "second", "third", "fourth", "fifth"]
for idx, val in enumerate(lines, start=8):
    print(idx, val)
lines.insert(2, "inserted time")
# modify list depending on nothing
lines.append("sixth sense")
for l in lines:
    print("Line:", l)
for i in lines:
    #i is a random lines
    if i == "second":
        print("we the best music, its dj khjaled")
    if i == "fourth":
        print("why u coming fast")
    n = 109
    for p in range(89,n):
        print(f"p prime is real {p}")
        print("just joking lol")
# finish