
print("----- The custome multiplication table-----")

number = int(input("Enter the number you wish to get the table of : "))

print(f"\nTable of {number}")

for i in range(1,11):
    result = number * i
    print(f"\n{number}*{i}={result}")