#Loop through numbers 1 to 50. If a number is divisible by 3, print "Fizz". 
# If divisible by 5, print "Buzz". If divisible by both, print "FizzBuzz". 
# Otherwise, print the number itself.

print("-----The FizzBuzz Challenge-----")

Leaftovers = []
FizzBuzz = []
Fizz = []
Buzz = []

for num in range(1,50):
    if num % 3 == 0 and num % 5 ==0:
        FizzBuzz.append(num)
        print(f"{num}:FizzBuzz")
    elif num % 3 == 0:
        Fizz.append(num)
        print(f"{num}:Fizz")
    elif num % 5 == 0 :
        Buzz.append(num)
        print(f"{num}:Buzz")
    else:
        Leaftovers.append(num)

print(f"Numbers divisbile by 3 and 5: {FizzBuzz}")
print(f"Numbers divisbile by 3: {Fizz}")
print(f"Numbers divisbile by 5: {Buzz}")
print(f"Numbers divisbile by neither 3 nor 5: {Leaftovers}")


#Additionally appended them into a clean list for better visual understanding