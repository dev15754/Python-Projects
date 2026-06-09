                      #string function
#ENDSWITH  ,  CAPITALIZE  , replace , find   , count


str= "i am studying from apna college"
print(str)
print(str.endswith("ege"))
print(str.endswith("epp"))

#--------------------------------------
str1=("i am abhyjoit singh")
print (str1)
print(str1.capitalize())
print(str1)           #it only captialize one time see this here I is not captialize like above one 

str1=str1.capitalize()
print(str1) #see this   before this we give order to capitalize print only know we say store it also 
# by writting str1=str1.capitalize()

#---------------------------------------
str3= "who is this person"
print(str3)
print(str3.replace("i","t"))  # str.replace("what","with")
print(str3.replace("this","who"))

#--------------------------------------------
str4="abhy is a good person"
print(str4)
print(str4.find("y"))
print(str4.find("good"))

#-------------------------------------------------
str5="abhy where are u"

print(str5)
print(str5.count("a"))