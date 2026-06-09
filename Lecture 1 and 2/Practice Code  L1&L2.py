
# grade student based on marks 
# above >100 marks have an error 
# MARKS==100,grade =("A+")
# marks>=90,grade="A"
# 90>marks>=80,grade="B"
# 80>marks>=70,grade="m 
# below 60 fail

marks=int(input("Enter Marks"))
if(marks>=101):
    Grade="ERROR"
elif(marks==100):
    Grade="A+"
elif(marks>=90 and marks <100):
    Grade="A"
elif(marks>=80 and marks <90):
     Grade="B"
elif(marks>=70 and marks <80):
      Grade="C"
elif(marks >=60 and marks <70):
      Grade="D"
else:
    Grade="FAIL"
print("Student Grade :",Grade)

#--------------------------

# WAP to check if a number entered by user is odd or even

num=int(input("enter a number "))
if(num % 2==0):
    print("even")
else:
    print("odd")


#---------------------------

# wap to find gretest of 3 number entered by the user  use if elif and else
a=int(input("enter a number 1: "))
b=int(input("enter a number2: "))
c=int(input("enter a number3: "))
if(a>=b and a>=c):
        print(("1-"),a)
elif(b>=a and b>=c):
        print(("2-"),b)
else:
     print(("3-"),c)


#------------------
# to check if a number is multiple of 7 or not 
num=int(input("enter a number"))
if(num%7==0):
     print("its the multiple of 7")
else:
     print("not a multiple")


# to find gretest of 3 number entered by the user 
# to check if a number is multiple of 7 or not 