# factorial and accumulation
nums = [2, 3, 4]
acc = 99
apart = 106
def factorial(n):
    #booom
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
print("5! =", factorial(9))
for i in range(apart-acc):
    print(i)
    print("heres i^2: ")
    print(i*i)
#that was a test for i
for x in nums:
    acc *= x * 7
print("Product:", acc)
# goodbye