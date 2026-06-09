                                                          #dictionary 
                            #type={} this is empty dictionary
                   # #they store data  values in key:value pairs
# to store in dictionary we should write total data in {}
#key cannot change value can change
#dictionary has no order means no index
#dictionary can change like lists
#in dictionary key caanot use for 2 different meanings
#to access the data in key store we use[]  not ()

# dict={
#     "name":"abhy",
#     "sub":("English","Maths","Sst",),
#     "cgpa": 9.6,
#     "marks": [98,97,95],
#     "age":20,
#     "is_adult":True,
#     "extra marks":94.8,
#     12:99.9
# }
# print(dict)
# print(dict["name"])
# print(dict["sub"])
# print(dict["age"])
# print(dict["is_adult"])
# print(dict[12])
# print(type(dict))

# dict["age"] = 19.5
# print(dict)

                                               #Nested Dictionaries
# student={
#     "name":"abhy",
#     "subjects":{
#         "maths":95,
#         "eng":85,
#     }
# }
# print(student["name"])
# print(student["subjects"])
# print(student["subjects"],["maths"])
# print(student["subjects"]["maths"])


#                              keys,values,items,get,update,
#keys=return all keys
#values=return all values
#items =return all keys values but as tuples
# get=return keys according to values
# update = insert the specified item in dictionary

#----------------------------------------------------------------
# student={
#     "name":"abhy",
#     "subjects":{
#         "maths":95,
#         "eng":85,
#     }
# }
# print(student.keys())
# print(list(student.keys()))

#----------------------------------------------------------------
# student={
#     "name":"abhy",
#     "subjects":{
#         "maths":95,
#         "eng":85,
#     }
# }
# print(student.values())
# print(list(student.values()))

#-----------------------------------------
# student={
#     "name":"abhy",
#     "subjects":{
#         "maths":95,
#         "eng":85,
#     }
# }
# print(student.items())
# print(list(student.items()))
#----------------------------------------
# student={
#     "name":"abhy",
#     "subjects":{
#         "maths":95,
#         "eng":85,
#     }
# }
# print(student.get("name")) #use
# print(student["name"]) #not to use

#----------------------------------------
# student={
#     "name":"abhy",
#     "subjects":{
#         "maths":95,
#         "eng":85,
#     }
# }
# student.update({"city":"baramulla"})
# print(student)



isinstance()#is used to check if a value is of a given type return true or false
