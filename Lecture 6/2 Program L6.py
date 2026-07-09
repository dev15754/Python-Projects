                                #Recursion
#when a function call itsself repeatdly
#recursion and loops are similar 100%

# def show(n):
#     for n in range(5,0,-1):
#         print(n)

# show(5)

#or
# def show(n):
#     if (n==0):
#         return
#     print(n)
#     show(n-1)


# show(5)

# 1!=1
# 2!=1x2
# 3!=1x2x3
# 4!=1x2x3x4

# we can say to find 5! we can say 4!x5 


# fact (n)=fact(n-1)x n
# fact(5)=(fact(5-1)x5)

# find factorial of n

def find_fact(n):
    if n==0 or n==1:
        print(1)
    else:
        n=(n-1)*n
        print(n)

find_fact(5)
