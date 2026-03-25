def collatz(number):
    if number % 2 == 0:
        result =  number // 2
    else:
        result = 3 * number + 1
    return result

number = int(input("Enter an integer: "))

results = []
while number != 1:
    number = collatz(number)
    results.append(number)

print(*results,sep=' ')
