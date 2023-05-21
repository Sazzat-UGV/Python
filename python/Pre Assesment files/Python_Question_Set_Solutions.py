# # 1) Write a Python function to sum all the numbers in a list
# # Sample list: [8, 2, 3, 0, 7]

# # def sum_all(list):
# #     sum=0
# #     for num in list:
# #         sum=sum+num
# #     print("Total Sum of the List: ",sum)

# # sum_all([8, 2, 3, 0, 7])





# # 2) Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters
# # Sample list: “The quick Brown Fox”
# # Expected Output :
# # No. of Upper case characters : 3
# # No. of Lower case Characters : 12

# # def check_string(string):
# #     count_upper=0
# #     count_lower=0
# #     for i in string:
# #         if i.isupper():
# #             count_upper+=1
# #         if i.islower():
# #             count_lower+=1
# #     print("No. of Upper case characters: ",count_upper)
# #     print("No. of Lower case Characters ",count_lower)

# # check_string("The quick Brown Fox")





# # 3) Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys
# # Expected output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# a={}
# for i in range(1,16):
#     a[i]=i*i
# print(a)

# # 4) Write a Python program to sum all the items in a dictionary
# # Sample dictionary: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
# dic={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
# sum=0
# dic_key=dic.values()
# for i in dic_key:
#     sum=sum+i
# print(sum)







# # 5) Write a Python program to create a symmetric difference set of set a and b
# # a = {1, 3, 5, 9, 6}
# # b = {2, 5, 7, 4, 1}
# # Expected output: {3, 2, 7, 9, 6, 4}

# # a = {1, 3, 5, 9, 6}
# # b = {2, 5, 7, 4, 1}
# # print("Output:",b.symmetric_difference(a))





# # 6) Write a Python program to remove all elements from a given set.
# # Sample input: {3, 2, 7, 9, 6, 4}
# # Expected output: {}

# # given_set={3, 2, 7, 9, 6, 4}
# # given_set.clear()
# # print("Output: ",given_set)





# # 7) If a word remains the same after reversing it then it's a palindrome. Now define a function to detect if a word is palindrome or not

# # def check_palindrom(string):
# #     reverse=""
# #     for char in string:
# #          reverse=char + reverse
# #     return string == reverse
    
# # print(check_palindrom("MOM"))





# # 8) 1 kilometer is equal to 0.621371 mile. Now create function that can convert kilometers to mile

# # def convert_miles(kilometer):
# #     if type(kilometer) not in [int,float]:
# #         raise KeyError("Please enter kilometers as a number")
# #     return 0.621371 *kilometer

# # print(convert_miles(5))





# # 9) Write a function that can remove punctuation marks from a string
# #     # punctuations: "!()-[]{};:'"\,<>./?@#$%^&*_~"

# # def punctuations_remover(string):
# #     punctuations = "!()-[]{};:\,<>./?@#$%^&*_~"
# #     fresh=""
# #     for i in string:
# #         if i not in punctuations:
# #             fresh=fresh+i
# #     return fresh
# # print(punctuations_remover("A.s;i:k"))





# # 10) The Fibonacci sequence is a sequence where the next term is the sum of the previous two terms. The first two terms of the Fibonacci sequence are 0 followed by 1. Now write a program to print fibonacci series up to a certain number

# # def fibonacci(end_number):
# #     a,b=0,1
# #     count=0
# #     while count < end_number:
# #         a,b=b,a+b
# #         print(b)
# #         count+=1
# # fibonacci(10)





# # 11) Write a function that can take a sentence and print each word of that sentence in alphabetic order
# # def sort_words_alphabetically(sentence):
# #     word=sentence.split(" ")
# #     word.sort()
# #     for i in word:
# #         print(i)

# # sort_words_alphabetically("hi we are learning python and it's awesome")





# # 12) Write a function to find even or odd
# # def check_even(num):
# #     if num%2==0:
# #         print(f"{num } in a Even Number")
# #     else:
# #         print(f"{num } in a Odd Number")

# # check_even(7)





# # 13) Write a program to check if a number is positive, negative or zero

# # def check_number(number):
# #     if number > 0:
# #         print(f"{number} is a Positive Number")
# #     elif number < 0:
# #         print(f"{number} is a Negative Number")
# #     else:
# #         print(f"{number} is a zero")

# # check_number(10)





# # 14) If any natural number is greater than 1 and having no positive divisors other than 1 and the number itself then it's called a prime number. For example: 3, 7, 11 etc are prime numbers. Now write a function that can check if a number is prime number or not

# # def prime_checker(number):
# #     if number > 1:
# #         for i in range(2, number):
# #             if (number % i) == 0:
# #                 print(f"{number} is not a prime number")
# #                 break
# #         else:
# #             print(f"{number} is a prime number")
# #     else:
# #         print(f"{number} is not a prime number")

# # prime_checker(10)





# # 15) Write a function to find the largest number among three given input numbers

# # def find_largest_number(num1, num2, num3):

# #     largest = num1

# #     if (num1 > num2) and (num1 > num3):
# #         largest = num1
# #     elif (num2 > num1) and (num2 > num3):
# #         largest = num2
# #     else:
# #         largest = num3

# #     print(f"The largest number is {largest}")

# # find_largest_number(15, 23, 8)





# # # A leap year is exactly divisible by 4 except for century years (years ending with 00). The century year is a leap year only if it is perfectly divisible by 400. For example,
# #     # 2017 is not a leap year
# #     # 1900 is a not leap year
# #     # 2012 is a leap year
# #     # 2000 is a leap year

# # 16) Now write a function to check if a year is leap year or not

# def check_leap_year(year):
#     if year % 400 == 0:
#         print(f"{year} is a leap year")
#     elif (year % 4 == 0) and (year % 100 != 0):
#         print(f"{year} is a leap year")
#     else:
#         print(f"{year} is not a leap year")

# check_leap_year(2009)


