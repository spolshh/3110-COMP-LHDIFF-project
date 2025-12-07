# factorial and accumulation
def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
#booom
print("5! =", factorial(5))
nums = [2, 3, 4]
acc = 1
apart = 9
for i in range(apart-acc):
    print(i)
    print("heres i^2: ")
    print(i*i)
#that was a test for i
for x in nums:
    acc *= x
print("Product:", acc)
# goodbye