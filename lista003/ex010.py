num = int(input())
for c in range(1, num + 1):
    if c % 3 == 0 and c % 5 == 0:
        print("Fizz Buzz")
    elif c % 3 == 0:
        print("Fizz")
    elif c % 5 == 0:
        print("Buzz")
    else:
        print(c)