# # -----------------------------------------Class_1(Introduction to Python)--------------------------------------

# # print("Hello This is my First Programe")





# # -----------------------------------Class_3(Working With String And Booleans)------------------------------------

# # name="Asikul Islam Sazzat -EVE"
# # print(name[0:6])
# # print(name[:12])
# # print(name[13:])
# # print(name[-3:])
# # print(name[:])


# # name="Asikul islam sazzat"
# # name1="MUSA KALIMULLA"
# # number="123456789"
# # print(name)
# # print("Upper: ",name.upper())
# # print("Capitalize: ",name.capitalize())
# # print("Title: ",name.title())
# # print("EndsWith: ",name.endswith("sazzat"))
# # print("StartWith: ",name.startswith("asikul"))
# # print("Find: ",name.find("sazzat"))
# # print("Split: ",name.split(" "))
# # print("Len: ",len(name))
# # print("Swapcase: ",name1.swapcase())
# # print("Lower: ",name.lower())
# # print("Check Upper: ",name1.isupper())
# # print("Check Lower: ",name.islower())
# # print("Check AlphaNumaric: ",number.isalnum())


# # name="     asikul islam sazzat "
# # print("Strip:",name.strip())
# # print("Rstrip:",name.rstrip())
# # print("Lstrip:",name.lstrip())


# # name="Asikul Sazzat"
# # name1="Avijit Samaddar"
# # print("Replace: ",name.replace("Asikul"," Ismail" ))
# # print("Join: ",",".join(name1))


# # name=input(str("Input Your Name: "))
# # location=input(str("Enter Your Location: "))
# # location1="AIUB"
# # print("Hey Me {} From {}".format(name, location))
# # print(f"Hey Me {name} From {location1}")


# # -------------------------------------------Class_5(Loops in Python)---------------------------------------------

# # a=1
# # while a<=20:
# #     print(a)
# #     a+=1


# # for i in range(10):
# #     print(i)


# # for i in range(0,20):
# #     print(i)


# # for i in range(0,20,2):
# #     print(i)


# # student=["Sazzat","Abir","Forhad","Akash"]
# # print("ALL Stiudent: ",student)
# # print("Single Student: ",student[1])
# # for index,value in enumerate(student):
# #     print(f"{index}->{value}")


# # parent_students = [{"name": "Rahim", "childs": ["Abdul", "Morshed"]}, {"name": "Karim", "childs": ["Sajib", "Saikat"]}, {"name": "Raihan", "childs": ["Ruhul", "Rusho"]}]
# # for student in parent_students:
# #     for child in student["childs"]:
# #         print(f"{child} is {student['name']}\'s child")


# # a=0
# # entry_restricted_for=5
# # program_close=17
# # while a<20:
# #     a+=1
# #     if a==entry_restricted_for:
# #         continue
# #     if a== program_close:
# #         break
# #     print("Now Value: ",a)


# # students = ["Rahim", "Karim", "Rafiq", "Jobbar", "Sushanto"]
# # # for student in students:
# # #     print(student)
# # a=0
# # while a<len(students):
# #     print(students[a])
# #     a+=1


# # -------------------------------------Class_6(Working with List and Tuple)---------------------------------------

# # student=["Rahim", "Karim", "Rafiq", "Sazzat", "Jobbar", "Sushanto"]
# # student1=("Sakil","Nahid","Arnob","Nazrul","Zihad") it is immutable it cannot be change
# # print("Check student type: ",type(student))
# # print("Check student1 type: ",type(student1))
# # print(student[4])
# # print(student1[3])


# # student=["Rahim", "Karim", "Rafiq", "Sazzat", "Jobbar", "Sushanto"]
# # student1=["Rahim", "Jakaria", "Siam", "Jakaria"]
# # student.append("Zakir")
# # print("After Append: ",student)


# # student.pop()
# # print("After Pop: ",student)


# # student.pop(3)
# # print("After pop using index: ",student)


# # student.remove("Sazzat")
# # print("After Remove a Specific Value: ",student)


# # student.extend(student1)
# # print("After Extend: ",student)


# # student.sort()
# # print("After Sort: ",student)


# # student.sort(reverse=True)
# # print("After Sort in Reverse: ",student)


# # student.reverse()
# # print("After Reverse: ",student)


# # student.clear()
# # print("After Clear: ",student)


# # copy=student1.copy()
# # student.append(copy)
# # print(student)


# # print("Index Number: ",student.index("Sazzat"))
# # print("Count Total Value: ",student1.count("Jakaria")) It return how many time "Jakaria" Available


# # student.insert(0, "Maria")
# # print("After Insert: ",student)


# # -----------------------------------Class_7(Working with Set and Dictionary)-------------------------------------
# # -------------------------------------------------------Set------------------------------------------------------
# # student = {"rafiq", "sofiq", "sohan", "jobbar", "sohan", "rafiq"}
# # nums1 = {1, 2, 4, 6, 9, 8}
# # nums2 = {4, 2, 7, 10}


# # print("Check Data Type: ",type(student))
# # print("Check Len: ",len(student))


# # student.add("Sazzat")
# # print("After Add: ",student)


# # student.update({"Sazzat","Sarah","Maria","Nusrat"}) it help to added multiple data
# # print("After Update: ",student)


# # student.remove("sohan")
# # print("After Romove: ",student)


# # print(student)
# # print("After Pop: ",student.pop())


# # print("After Union: ",nums1.union(nums2))


# # print("After Intersection: ",nums1.intersection(nums2))


# # nums1.intersection_update(nums2)
# # print("After Intersection Update: ",nums1)


# # print("After Symmeetric Difference: ",nums1.symmetric_difference(nums2))


# # nums1.symmetric_difference_update(nums2)
# # print("After Symmeetric Difference Update: ",nums1)


# # nums1.clear()
# # print("After Clear: ",nums1)


# # print("Check Subset",nums2.issubset(nums2))


# # print("Check Superset",nums1.issuperset(nums2))


# # copy=nums1.copy()
# # print("After Copy:",copy)


# # nums1.discard(8)
# # print("After Discard",nums1) it safly remove any item


# # print("After Difference:",nums1.difference(nums2))


# # nums1.difference_update(nums2)
# # print("After Difference Update:",nums1)

# # ---------------------------------------------------Dictionary---------------------------------------------------

# student = {"name": "Rahim", "age": 34, "gender": "Male", "asset": 5000}

# # print(student["age"])


# # student["age"]=45
# # print("After Change Age: ",student["age"])


# # student["age"]+=6
# # print("After Increment Age: ",student["age"])


# # student["cgpa"]=3.5
# # print("After Added New Value: ",student)


# # student.update({"CGPA":3.8,"Roll":"12011016"})
# # print("After Update: ",student)


# # student.pop("name")
# # print("After Pop: ",student)


# # student.popitem()
# # print("After Popitem: ",student)


# # print("After Get: ",student.get("age"))


# # student.clear()
# # print("After Clear: ",student)


# # student.setdefault("ID",12011016)
# # print("After SetDefault: ",student)


# # for key in student.keys():
# #     print(key)


# # for value in student.values():
# #     print(value)


# # print("Getting Item: ",student.items())


# # for key,value in student.items():
# #     print(f"{key}=>{value}")


# # -----------------------------------------Class_8(Getting Start with Function)--------------------------------------

# # def addition(a,b):
# #     return a+b
# # print(addition(10, 90))



# # age=18
# # def ageCalculation(age):
# #     age+=10
# #     return age
# # print(ageCalculation(10))



# # age=18
# # def ageCalculation(age1):
# #     global age
# #     age+=age1
# #     return age
# # print(ageCalculation(10))



# # def print_numbers(list_of_numbers, age):
# #     for number in list_of_numbers:
# #         print(number)
# # print_numbers([1, 2, 3, 4, 5],42)



# # def print_names(*names):
# #     for name in names:
# #         print(name)
# # print_names("monirul", "jannat", "safa", "mizan")



# # def print_winners(first_winner, second_winner, third_winner):
# #     print("Winner is: ", first_winner)
# #     print("Runners up is: ", second_winner)
# #     print("Third winner is: ", third_winner)
# # # print_winners("Rafiq", "Jannat", "Rafi")
# # print_winners(second_winner="sazzat",first_winner="Rafik" , third_winner="badsa")



# # def print_winners(**winners):
# #     for key, value in winners.items():
# #         print(key + " => " + value)
# # print_winners(first_winner="Rafiq", second_winner="Jannat", third_winner="Rafi")



# # def print_hello(greetings, name):
# #     print(f"{greetings} {name}")
# # print_hello("Hi", "Rasel")
# # print_hello(name="Raihan", greetings="Hello")



# # class_five_student=[]
# # class_ten_student=[]
# # def add_student(class_name,*students):
# #     if class_name=="five":
# #         active_class=class_five_student
# #     if class_name=="ten":
# #         active_class=class_ten_student
# #     for student in students:
# #         active_class.append(student)
# # add_student("five", "raihan", "sohan", "rafiq")
# # print("Class Five: ",class_five_student)
# # print("Class Ten: ",class_ten_student)


# # -----------------------------------------Class_9(Working with modules)--------------------------------------

# # import  module
# # import datetime as date
# # print(module.PI)
# # module.name("Sazzat")
# # module.name1("Sazzat",24)
# # print(date.datetime.now())


# # ------------------------------------Class_10(Debugging and error handling)---------------------------------

# # a=input("Enter a number: ")
# # b=10
# # try:
# #     sum= a+b
# # except TypeError as error:
# #     sum= int(a)+b
# # else:
# #     print("This is from Else Block")
# # finally:
# #     print("This is from Finally Block")
# # print(sum)



# # import pdb; pdb.set_trace()
# # a=input("Enter a number: ")
# # b=10
# # try:
# #     sum= a+b
# # except TypeError as error:
# #     sum= int(a)+b
# # else:
# #     print("This is from Else Block")
# # finally:
# #     print("This is from Finally Block")
# # print(sum)




















