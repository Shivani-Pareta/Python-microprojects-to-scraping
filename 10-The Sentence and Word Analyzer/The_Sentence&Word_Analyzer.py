#check the number of vowels and total letters and words in a sentence/paragraph

print("-----The Sentence & Word Analyzer-----")

content = input("Please enter your content here:")

vowels= "aeiou"
vowel_count=0
consonant_count=0

for char in content:
    if char in vowels:
        vowel_count+=1
    elif char.isalpha():
        consonant_count+=1
#else does not take conditions hence elif

word_list = content.split()
word_count = len(word_list)
#split uses spaces to covert the content into a list of words and later the len function counts the items in the list

print(f"\n Total Characters :{vowel_count+consonant_count}")
print(f"\n Total Words:{word_count}")
print(f"\n Total Vowels:{vowel_count}")