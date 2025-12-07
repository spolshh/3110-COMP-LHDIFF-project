numbers = [1, 2, 3, 4, 5, 6]
squared = []
#table for squares
for n in numbers:
    squared.append(n * n)
    #squared numbers only
    if n == 2:
        print("this is 2")
print("Squared:", squared)
evend = [x for x in numbers if x % 3 == 0]
print("Evens:", evens)
#even numbers
total = sum(numbers)
print("Total:", total)
print(total*7)
avg = total / len(numbers)
print(f"Avg: {avg}")
newest_avg = 29+avg
#this is atest for 3110
# end finally