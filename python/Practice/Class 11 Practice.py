# file=open("myfile.txt",'r') open file as read mode
# print(file.read()) for read total file

# print(file.readline())
# print(file.readline())
# print(file.readline())

# print(file.read(5)) print 1st 5 char

# file_lines=file.read()
# print(file_lines)

# file_lines=file.readline()
# print(file_lines)



# file=open("myfile.txt",'w') open as write mode 
# file.write("Hello I am 1st Sazzat from UGV")


# file=open("myfile.txt",'a') open as append mode 
# file.write("\nHello I am 4th Sazzat from UGV")


# file=open("myfile1.txt",'x') create a new file .if already exist than it gives error


# file=open("myfile.txt",'r')
# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.seek(0)
# print(file.readline())


# file=open("myfile.txt",'r+') open as open as read and write mode
# print(file.read())
# file.write("\nHello I am 7th Sazzat from UGV")
# print(file.read())


# student_list=["Asik","Sazzat","Al-Amin","Rakib"]
# file=open("student_list.txt",'a')
# for student in student_list:
#     file.write(f"{student}\n")


# with open("student_list.txt",'r') as file:
#     print(file.read())
#     print(file.readline(2))
#     file.close()
#     print(file.closed) it check whether a file is close or not
