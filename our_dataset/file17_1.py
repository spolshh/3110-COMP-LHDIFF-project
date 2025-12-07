# list processing
numbers = [1, 2, 3, 4, 5, 6]
squared = []
for n in numbers:
    squared.append(n * n)
    if n == 2:
        print("this is 2")
print("Squared:", squared)
#squared nums
evens = [x for x in numbers if x % 2 == 0]
print("Evens:", evens)
#even numbers
total = sum(numbers)
print("Total:", total)
print(total*2)
avg = total / len(numbers)
print("Avg:", avg)
newest_avg = 29+avg
#this is atest
# end