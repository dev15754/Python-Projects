# Create a set with values 1,2,3,4,4,5. Print it and observe the duplicate.
# Create a dictionary with your name, age, and city. Print the whole dictionary.
# Create an empty set and a set and print its type.
# Add "city":"baramulla" to student = {"name":"abhy"} using .update(). Print it.
# Create collection = {1,2,3,"hello","hello","good"} and print its type.
# Print only the value of "name" from d = {"name":"abhy", "age":20}
# Create empty set. Add 1, 2, 3, 3(duplicate), "apna college", (13,22,99). Print.
# Create a nested dictionary with name and subjects (maths:95, eng:85). Print the full subjects dict.
# FinD union of coll1={1,2,3,4,8} and coll2={2,3,9,8,7}. Print result and both originals.
# Print all keys of student = {"name":"abhy", "cgpa":9.6}
# Create a set {1,2,3,"apna college",(13,22,99)}. Remove 2 and print.
# Print the value at integer key 12 from d = {12:99.9, "name":"abhy"}
# Create a set with 3 elements. Print its length, clear it, then priNt length again.
# Convert keys of student = {"name":"abhy", "cgpa":9.6} to a list and print.
# Create coll = {"abhy","zebra","tiger",5,7}. Pop 3 elements one by one and print each.
# Print all values of student = {"name":"abhy", "cgpa":9.6}
# Find intersection of coll1={1,2,3,4,8} and coll2={2,3,9,8,7}. Print result.
# Create a dict where "sub" stores a tuple of 3 subjects and "marks" stores a list of 3 marks. Print both.
# sub = {"python","java","c++","c","python","c++","python","c"} — how many classrooms needed? Print count.
# Convert values of student = {"name":"abhy", "cgpa":9.6} to a list and print.
# Store 9 (int) and 9.0 (float) as separate values in a set.
# Print all key-value pairs of student = {"name":"abhy", "cgpa":9.6} as tuples.
# data = {8,5,9,"9"} — how many elements does this have and why?
# Convert .items() of student = {"name":"abhy", "cgpa":9.6} to a list and print.
# Try s[0] on a set. What error comes? Write code and comment the error.
# Use .get() to access "name" from student = {"name":"abhy"}
# Add tuple (13,22,99) to an empty set and print.
# Use .get() to access "city" which doesn't exist first update the city then .get  .student = {"name":"abhy"}. then print# Create one empty set and one empty dict. Print the type of each.
# Start with d = {"age":20}. Change age to 19.5 and print.
# Prove .union() doesn't change the originals. Print coll1 before union and after.
# Print the type of d = {"a":1}
# Prove .intersection() doesn't change the originals. Print coll1 before and after.
# From student = {"name":"abhy", "subjects":{"maths":95,"eng":85}}, print only the maths score.
# s = {10,20,30} — print length, clear it, print length again.
# Store "table":"a piece of furniture" and "cat":"a small animal" in a dict. Print the meaning of "table".
# coll1={1,2,3,8} coll2={2,3,9} — find intersection and print only the common elements.
# Start with empty dict. Add phy, maths, chem marks using .update() all at once. Print.
# Create dict with is_adult:True and cgpa:9.6. Print the type of each value.
# Why can you add a tuple to a set but not a list? Show with code.
# Store "extra marks":94.8 in a dict. Print its type.
# Ask user for phy, maths, chem marks using input().Store in empty dict and print.
# Add "science":88 to the subjects dict inside student = {"name":"abhy", "subjects":{"maths":95}}. Print.
# Create dict with keys: "name"(str), 12(int), True(bool). Print all three values.
# Use .get() to access "city" from student dict. If missing, return "unknown".
# d = {"name":"abhy","city":"baramulla"} — update city to "srinagar". Print.
# What prints? d = {"x":1, "x":2} → print(d["x"])
# student = {"name":"abhy","subjects":{"maths":95}} — use .get() on subjects to access "eng". If missing return 0.
# Print each key-value pair from student = {"name":"abhy","age":20} on a separate line using .items().
# Create a full student record with name, age, is_adult(bool), marks(list), subjects(nested dict with 2 subjects). Print each value using its key.

#-----------------
# Q1
# Create a set with values 1,2,3,4,4,5. Print it and observe the duplicate.
# value={1,2,3,4,4,5}
# print(value)
# # i observe it remove duplicate number from sets 

#-----------------
# Q2
# Create a dictionary with your name, age, and city. Print the whole dictionary.
# dict={
#     "name":"abhy",
#     "age":19,
#     "city":"baramulla",
# }
# print(dict)

#-----------------
# Q3
# Create an empty set and a set and print its type.
# take=set()
# take1={1,2,3}

# print(type(take))
# print(type(take1))

#-----------------
# Q4
# Add "city":"baramulla" to student = {"name":"abhy"} using .update(). Print it.
# student={}
# student.update({"city":"baramulla",
#                 "name":"abhy"})
# print(student)

#-----------------
# Q5
# Create collection = {1,2,3,"hello","hello","good"} and print its type.
# collection= {1,2,3,"hello","hello","good"}
# print(type(collection))

#-----------------
# Q6
# Print only the value of "name" from d = {"name":"abhy", "age":20}

# d = {"name":"abhy", "age":20}
# print(d["name"])


#-----------------
# Q7
# Create empty set. Add 1, 2, 3, 3(duplicate), "apna college", (13,22,99). Print.

# s=set()
# s.add(1)
# s.add(2)
# s.add(3)
# s.add(3)
# s.add(2)
# s.add(1)
# s.add("apna college")
# s.add((13,22,99))
# print(s)


#-----------------
# Q8
# Create a nested dictionary with name and subjects (maths:95, eng:85). Print the full subjects dict.

# dict1={
#     "name":"abhy",
#     "subjects":{
#         "maths":95,
#         "eng":85
#     }
# }
# print(dict1)
# print(dict1["subjects"]["maths"])
#-----------------
# Q9
# Find union of coll1={1,2,3,4,8} and coll2={2,3,9,8,7}. Print result and both originals.
# coll1={1,2,3,4,8}
# coll2={2,3,9,8,7}
# print(coll1.union(coll2))


#-----------------
# Q10
# Print all keys of student = {"name":"abhy", "cgpa":9.6}
# data= {"name":"abhy", "cgpa":9.6}
# print(data.keys())


#-----------------
# Q11
# Create a set {1,2,3,"apna college",(13,22,99)}. Remove 2 and print.
# demo={1,2,3,"apna college",(13,22,99)}
# demo.remove(2)
# print(demo)



#-----------------
# Q12
# Print the value at integer key 12 from d = {12:99.9, "name":"abhy"}
# d = {12:99.9, "name":"abhy"}
# print(d[12])

#-----------------
# Q13
# Create a set with 3 elements. Print its length, clear it, then print length again.
# demo={1,"apna",25.4}
# print(len(demo))
# demo.clear()
# print(len(demo))

#-----------------
# Q14
# Convert keys of student = {"name":"abhy", "cgpa":9.6} to a list and print.
# demo={"name":"abhy", "cgpa":9.6}
# convert=demo.keys()
# print(list(convert))
## or 
# demo={"name":"abhy", "cgpa":9.6}
# print(list(demo.keys()))

#-----------------      
# Q15
# Create coll = {"abhy","zebra","tiger",5,7}. Pop 3 elements one by one and print each.
# coll = {"abhy","zebra","tiger",5,7}
# print(coll.pop())
# print(coll.pop())
# print(coll.pop())

#-----------------
# Q16
# Print all values of student = {"name":"abhy", "cgpa":9.6}
# student = {"name":"abhy", "cgpa":9.6}
# print(student.values())


#-----------------
# Q17
# Find intersection of coll1={1,2,3,4,8} and coll2={2,3,9,8,7}. Print result.
# coll1={1,2,3,4,8}
# coll2={2,3,9,8,7}
# print(coll1.intersection(coll2))


#-----------------
# Q18
# Create a dict where "sub" stores a tuple of 3 subjects and "marks" stores a list of 3 marks. Print both.
# demo={
#     "sub":("maths","eng","phy"),
#     "marks":[85,98,78]
# }
# print(demo)
# print(demo["sub"])
# print(demo["marks"])


#-----------------
# Q19
# sub = {"python","java","c++","c","python","c++","python","c"} — how many classrooms needed? Print count.
# sub = {"python","java","c++","c","python","c++","python","c"}
# classroom=len(sub)
# print("total classes need is ",classroom)




#-----------------
# Q20
# Convert values of student = {"name":"abhy", "cgpa":9.6} to a list and print.
# student = {"name":"abhy", "cgpa":9.6}
# print(list(student.values()))



#-----------------
# Q21
# Store 9 (int) and 9.0 (float) as print separate values in a set.
# demo={9,"9.00"}
# print(demo)

#-----------------
# Q22
# Print all key-value pairs of student = {"name":"abhy", "cgpa":9.6} as tuples.
# student = {"name":"abhy", "cgpa":9.6}
# print(student.items())



#-----------------
# Q23
# data = {8,5,9,"9"} — how many elements does this have and why?
# data = {8,5,9,"9"}
# print(data)

# #it has 4 elemets becouse it has no common one inside the set but if we see there are two 9 but one 
# is int and other is str 

#-----------------
# Q24
# Convert .items() of student = {"name":"abhy", "cgpa":9.6} to a list and print.

# student = {"name":"abhy", "cgpa":9.6}
# print(list(student.items()))


#-----------------
# Q25
# Try s[0] on a set. What error comes? Write code and comment the error.
# s = {1, 2, 3}
# print(s[0])
# #error as there is no index defined in sets so the error come if we want the result convert to list then 


#-----------------
# Q26
# Use .get() to access "name" from student = {"name":"abhy"}
# student = {"name":"abhy"}
# print(student.get("name"))



#-----------------
# Q27
# Add tuple (13,22,99) to an empty set and print.
# value=set()
# value.add((13,22,99))
# print(value)


#-----------------
# Q28
# Use .get() to access "city" which doesn't exist first update the city then .get  .student = {"name":"abhy"}. then print

# student = {"name":"abhy"}
# student.update({"city":"baramulla",})
# print(student.get("city"))


#-----------------
# Q29
# Create one empty set and one empty dict. Print the type of each.

# value=set()
# value2={}
# print(type(value))
# print(type(value2))

#-----------------
# Q30
# Start with d = {"age":20}. Change age to 19.5 and print.
# d = {"age":20}
# (d.update({"age":19.5,}))
# print(d)



#-----------------
# Q31
# Prove .union() doesn't change the originals. Print coll1 before union and after.




#-----------------
# Q32
# Print the type of d = {"a":1}




#-----------------
# Q33
# Prove .intersection() doesn't change the originals. Print coll1 before and after.




#-----------------
# Q34
# From student = {"name":"abhy", "subjects":{"maths":95,"eng":85}}, print only the maths score.




#-----------------
# Q35
# s = {10,20,30} — print length, clear it, print length again.




#-----------------
# Q36
# Store "table":"a piece of furniture" and "cat":"a small animal" in a dict. Print the meaning of "table".




#-----------------
# Q37
# coll1={1,2,3,8} coll2={2,3,9} — find intersection and print only the common elements.




#-----------------
# Q38
# Start with empty dict. Add phy, maths, chem marks using .update() all at once. Print.




#-----------------
# Q39
# Create dict with is_adult:True and cgpa:9.6. Print the type of each value.




#-----------------
# Q40
# Why can you add a tuple to a set but not a list? Show with code.




#-----------------
# Q41
# Store "extra marks":94.8 in a dict. Print its type.




#-----------------
# Q42
# Ask user for phy, maths, chem marks using input(). Store in empty dict and print.




#-----------------
# Q43
# Add "science":88 to the subjects dict inside student = {"name":"abhy", "subjects":{"maths":95}}. Print.




#-----------------
# Q44
# Create dict with keys: "name"(str), 12(int), True(bool). Print all three values.




#-----------------
# Q45
# Use .get() to access "city" from student dict. If missing, return "unknown".




#-----------------
# Q46
# d = {"name":"abhy","city":"baramulla"} — update city to "srinagar". Print.




#-----------------
# Q47
# What prints? d = {"x":1, "x":2} → print(d["x"])




#-----------------
# Q48
# student = {"name":"abhy","subjects":{"maths":95}} — use .get() on subjects to access "eng". If missing return 0.




#-----------------
# Q49
# Print each key-value pair from student = {"name":"abhy","age":20} on a separate line using .items().




#-----------------
# Q50
# Create a full student record with name, age, is_adult(bool), marks(list), subjects(nested dict with 2 subjects). Print each value using its key.