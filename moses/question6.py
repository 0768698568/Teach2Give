#Question 6: Count Vowels
#Write a program that counts the number of vowels in a sentence.

def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in sentence:
        if char in vowels:
            vowel_count += 1
    return vowel_count

sentence = input("Enter a sentence: ")
print("Number of vowels:", count_vowels(sentence))

        