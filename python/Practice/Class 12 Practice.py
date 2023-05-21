# # class Student:
# #     name="Asikul Islam Sazzat"
# #     age=23

# #     def sum(self):
# #         return 3+2

# # student1=Student()
# # print(student1.name)
# # print(student1.age)



# # class Student:
# #     def __init__(self,name,age,cgpa):
# #         self.name=name
# #         self.age=age
# #         self.cgpa=cgpa
    
# #     def __del__(self):
# #         print("Distructor Called")

# #     def print_my_name(self):
# #         print(f"My name is {self.name}")

# # student1=Student("Asikul Islam Sazzat", 23, 3.86)
# # student1.print_my_name()

# # student2=Student("Sarah Moni", 21, 4.00)
# # student2.print_my_name()

# # print(f"My name is {student1.name} and my age is {student1.age} also my CGPA is {student1.cgpa}")



# # class Student:
# #     def __init__(self,name,age,cgpa,roll):
# #         self.name=name
# #         self.age=age
# #         self.cgpa=cgpa
# #         self.roll=roll
    
# #     def participate_exam(self):
# #         print(f"{self.name} Participated in the Exam")
    
# #     def increment_birth_year(self,age_to_be_incremented):
# #         self.age=self.age+age_to_be_incremented

# # student1=Student("Asikul Islam Sazzat", 23, 3.86, 12011016)
# # student2=Student("Maria Jahan Mishu", 22, 3.50 , 12011029)

# # print(student1.name)
# # print(student1.age)
# # print(student1.cgpa)
# # print(student1.roll)
# # student1.participate_exam()
# # student1.increment_birth_year(7)
# # print(student1.age)

# # print(student2.name)
# # student2.participate_exam()
# # student2.increment_birth_year(3)
# # print(student2.age)


# class Student:
#     def __init__(self,name):
#         self.name=name
#         self.hand_cash=5000
#     def purchase_something(self,amount):
#         self.hand_cash=self.hand_cash-amount
#         print(f"Hey {self.name}. Now you have {self.hand_cash} taka")

# student1=Student("Asikul Islam Sazzat")
# student2=Student("Sarah Moni")

# student1.purchase_something(300)
# student2.purchase_something(870)