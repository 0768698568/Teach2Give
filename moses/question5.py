#Question 5: Reverse Integer
#Write a program that takes an integer as input and returns an integer with reversed digit ordering.

def reverse_integer(num):
    reversed_num = 0
    is_negative = False
    
    if num < 0:
        is_negative = True
        num = abs(num)
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
num = int(input("Enter an integer: "))

print("Reversed integer:", reverse_integer(num))
