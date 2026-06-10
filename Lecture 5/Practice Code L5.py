# #Q1
# #print number from 1 to 100 
# a=1
# while a <=100:
#     print("hello",a)
#     a+=1
# print("loop ends here ")

# # Q2
# #Print number fromm 100 to 1 
# b=100
# while b >=1:
#     print("hello",b)
#     b-=1

#Q3
#Print the multipliction table of a number n 
# n=int(input("enter which table u want : ") )
# a=1  #start from 
# while a<=10:
#     print(n*a)
#     a+=1

#Q4
#print the eliments of the following in a loop 
#[1,4,9,16,25,36,49,64,81,100]
# a=1
# while a <=10:
#     print(a**2)
#     a+=1
# or 
# nums=[1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx < len(nums):
#     print(nums[idx])
#     idx+=1

#Q5
# search for a number x in this tuple using loop (1,4,9,16,25,36,49,64,81,100)
# nums=(1,4,9,16,25,36,49,64,81,100)

# i=0 
# x=36
# while i< len(nums):
#     if (nums [i]== x):
#         print("found index",i)
    
#     i+=1

#Q6
#print the elements of the following list, using a loop 
# [1,4,9,16,25,36,49,64,81,100]
# val=[1,4,9,16,25,36,49,64,81,100,"new"]
# for new_val in val:
#     print(new_val)
# else:
#     print("end from else command")

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