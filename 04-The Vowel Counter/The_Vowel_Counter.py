
print("-----Vowel Counter-----")

text = input("please enter your text:").lower()
vowels = "aeiou"
count = 0
consonant_count = 0


for char in text:
#if char.isalpha(): # if you think the code is counting the spaces as well then .isalpha()function can be used
# to make sure the code picks up only alphabets, not numbers not spaces not symbols.
        if char in vowels:
            count +=1
        else:
            consonant_count +=1
print(f"Total number of vowels in the text are:{count}")
print(f"total number consonants in the text are:{consonant_count}")