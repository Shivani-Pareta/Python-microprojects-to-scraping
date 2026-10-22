
print("-----Vowel Counter-----")

text = input("please enter your text:").lower()
vowels = "aeiou"
count = 0
consonant_count = 0


for char in text:
    if char in vowels:
        count +=1
    else:
        consonant_count +=1
print(f"Total number of vowels in the text are:{count}")
print(f"total number consonants in the text are:{consonant_count}")