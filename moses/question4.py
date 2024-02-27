#Question 4: Capitalize Words
#Write a program that accepts a string as input, capitalizes the first letter of each word in the 
#string, and then returns the result string.

def capitalize_words(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize()for word in words]
    result = ''.join(capitalized_words)
    return result
input_str = input("Enter a string: ")
print(capitalize_words(input_str))