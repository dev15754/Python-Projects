                                #Recursion
#when a function call itsself repeatdly
#recursion and loops are similar 100%

# def show(n):
#     for n in range(5,0,-1):
#         print(n)

# show(5)

#or
def show(n):
    if (n==0):
        return
    print(n)
    show(n-1)


show(5)