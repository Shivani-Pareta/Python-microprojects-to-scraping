
print("-----Welcome to the even odd sorter")

numbers = [23,34,45,67,78,89,12,25,36,44,14,27,48,79,57,100,1234]

even_numbers = []
odd_numbers = []

for num in numbers:

    if num % 2 ==0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("\nOriginal Number:", numbers)
print(f"\nEven numbers found :{even_numbers}")
print(f"\nOdd numbers found : {odd_numbers}")
