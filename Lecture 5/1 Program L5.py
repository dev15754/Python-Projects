#                               loops (loops are yoused to reapet the instruction)
#                                           while loop
# while condition:
#     same work

# d=1
# while d <=500:
#     print("hello",d)
#     d+=1
# print("loop ended")
# #-------------------------in reverce while loop 
# d=5
# while d >=1:
#     print("hello",d)
#     d-=1
# print("loop ended")


#                                   Break and Continue in loop
# break used to terminate the loop when encountered 
# Continue: terminate execution in the current iteration and continues execution of the loop with the next iteration


# -------------------
i =1
while i<=5:
    print(i)
    if (i==3):
        break
    i+=1

print("end of loop ")
# -------------
nums=(1,4,9,16,25,36,49,64,81,100)

# i=0 
# x=36
# while i< len(nums):
#     if (nums [i]== x):
#         print("found index",i)
#         break #cafter this rest of the actions  will cancel 
#     else:
#         print("finding")
#     i+=1
# print("end of loop ")

# -------------
# i =0
# while i<=5:
#     if (i==3):
#         i+=1
#         continue # use as skip
#     print(i)
#     i+=1

#                                            For Loop 
#four loops are used for sequential traversal. for traversing list, string , tuples etc.
list=(1,2,3,4,5,6)
for a in list:
    print(a)
else:
    print("end")