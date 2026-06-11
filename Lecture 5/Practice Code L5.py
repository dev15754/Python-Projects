# #Q1
# #print number from 1 to 100 
a=1
while a <=100:
    print("hello",a)
    a+=1
# print("loop ends here ")

# # Q2
# #Print number fromm 100 to 1 
b=100
while b >=1:
    print("hello",b)
    b-=1

#Q3
#Print the multipliction table of a number n 
n=int(input("enter which table u want : ") )
a=1  #start from 
while a<=10:
    print(n*a)
    a+=1

#Q4
#print the eliments of the following in a loop 
#[1,4,9,16,25,36,49,64,81,100]
# a=1
# while a <=10:
#     print(a**2)
#     a+=1
# or 
nums=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx < len(nums):
    print(nums[idx])
    idx+=1

#Q5
# search for a number x in this tuple using loop (1,4,9,16,25,36,49,64,81,100)
nums=(1,4,9,16,25,36,49,64,81,100)

i=0 
x=36
while i< len(nums):
    if (nums [i]== x):
        print("found index",i)
    
    i+=1

#Q6
#print the elements of the following list, using a loop 
# [1,4,9,16,25,36,49,64,81,100]
val=[1,4,9,16,25,36,49,64,81,100,"new"]
for new_val in val:
    print(new_val)
else:
    print("end from else command")

#Q7
#search for a number X in this touple using loop
# (1,4,9,16,25,36,49,64,81,100)
num=(1,4,9,16,25,36,49,64,81,100)
x=81
idx=0
for el in num:
    if(el==x):
        print(x," found at index ",idx)
        break
    idx+=1

# # Q8
# #print numbers from one to hundred using for and range ()
for num in range(1,101):
    print(num)


# # Q9
# # print numbers from 100 to 1
for num in range (100,0,-1):
    print(num)

#Q10
#print a multiplication table of a number n
n=int(input("enter table of what u need"))
for i in range(1,11):
    print(n*i)

# Q11
# where to find the sum of first n numbers using for
n=2
sum=0
for i in range (1,n+1):
   sum+=i
print("total sum" ,sum)

# Q12
# write a program to find the sum of first N numbers using while
n=7
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
  
print(sum)

# Q13
# write a program to find the factorial of first n numbers using for
n=5
fact =1 #not 0

for i in range(1,n+1):
    fact*=i
   
print("factorial",fact)

