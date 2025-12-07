# function and string demo
def greet(name):
    msg = "Hello, " + name + "!"
    return msg
#functions
name = "Alex"
message = greet(name)
print(message)
name2 = "Sam"
print(greet(name2))
# small loop
lst = [1,9,8,7,0]
new_lst =[]
i=0
for num in lst:
    new_lst[i] = (num + 100)/2
    i = i+1
for ch in name:
    print(ch)
# finished