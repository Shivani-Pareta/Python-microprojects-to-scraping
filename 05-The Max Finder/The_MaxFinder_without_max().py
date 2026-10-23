#Look through a list of numbers and manually find the largest number without using Python's built-in max() function.
print("-----The MaxFinder-----")

numbers = [11,24,35,46,57,68,79,80,34,4554,53,42,64,75,86,97,8,26,3742,51]
highest_number = numbers[0] #Assuming the first number is the highest initially

for num in numbers:
    if num > highest_number:
        highest_number = num 
#we asked the code to check if the new number that the for loop is picking is greater than the number 0
#this will be the case for the first number then later it starts comparing with the previous number that it picked 
#then we asked the code to check if the number it saw next is bigger that the last one if yes assign it to the highest_number variable and keep the loop going 
print(f"\n Highest number out of the numbers presented is :{highest_number}")