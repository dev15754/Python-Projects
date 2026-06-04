#----------------------------Tuples in Python
#built in data type that is immutable sequence of value means the value canot change one crete the tuples

# marks=(94.1,75.2,98.16,55.26,82.12)
# print(type(marks))

# print(marks[0])
# # marks[0]=9          #error ~~~~~^^^ TypeError: 'tuple' object does not support item assignment
# #-------------------------------------------------------------------
# tup1=(9) #this is a string to make a tuples u need to add ,
# tup2=(9,)
# tup3=("abhy")
# tup4=("abhy",)
# print(type(tup1))
# print(type(tup2))
# print(type(tup3))
# print(type(tup4))

# index   count
#name index find index position
#name count and count the elements


# tup=(1,2,3,4,5,2)
# print(tup.index(3))

#===========================================================ex 1
# ask1=(input("enter movie name 1"))
# ask2=(input("enter movie 2 fav"))
# ask3=(input("fav movie 3"))
# store=[ask1,ask2,ask3]
# print(store)

#====================== 2way 
# movies = []

# movies.append(input("Enter movie name 1: "))
# movies.append(input("Enter movie name 2: "))
# movies.append(input("Enter movie name 3: "))

# print(movies)

#===========================================================ex2
# list1=[1,2,3,2,1]
# copylist1=(list1.copy())
# copylist1.reverse()

# if(copylist1 == list1):
#     print("palindrome")
# else:
#     print("not")