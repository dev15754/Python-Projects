
#this icon is used to hide text from code 

print('hello')   
print("hello abhy")
print("abhy2")
print("24")
print(25)      #
#print=2599  error becouse of =  in print then we use brackets 
print(2599) 
print("abhy,25")

#-------------------------------string= a b c d ,  integer 1 2 4 5 6 , float 4.99 25.66  , bolean True False (always T and F capital)  , None if we make a= none then it is not str integ not any type 
#while print string it should under "" ,for integer no need choice i have  if string name is on print place no need to add anything like 21 hear my name is  a string thats why in "" and name is a place of print  no need""

name="abhy"
section = "blue"
rollno = 25000


print ("my name is =" , name)
print ( "my name is =" , "name") #error becouse of "" in name


print ("my rollno is =",rollno)
print ("my rollno is =","rollno") #error becouse of "" in rollno

print("what is u section=",section)
print("what is u section=","section")#error becouse of "" in section

 

a=5
b=95
c=24
d=349
e=1527
f=246
g=2163
h=1562
i=rollno


sum=a+b+c+d+e+f+g+h+i

print("result after adding is =",sum)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #remainder to find
print(a**b) #a^b

m=200
l=200

print(m==l) #egual to we writee ==
print(m!=l)  # not egual to we write !=
print(a>=b) #greter then or equal to b >=
print(a>b)   #greater then > 
#viceversa for <






king=rollno
#rollno=king hear we face error we give him new value then = then  what already haved value-------------------hear new value is king    -------------  aleady have value is rollno
print("king age is",king)

queen=name
print(queen)


print(i ,king )

num = 10
num=num+10    #1

print("result=",num)

num = 10
num+=10        #2

print("result=",num)


print(not True)               #NOT gives opposite Value
print(not False)


value=True
value2=True
print(value and value2)                     # AND operator both value should true then print is true   
print(value or value2)                      #  OR operator if one is false other is true [rint true]


#type conversion
a= 2
b= 2.5
c="25"
sum=(a+b)     #error sum=(a+b+c) hear c is a string "25"   
                                 #float to string no ,float to int ok
print(sum)      
print (type(a))


a= 2  #here a = to 2 , 2 is a int we know but if we want 2 as any other type we do add type before value 
a=str(2.5)
b=float(35)

print (type(a))
print (type(b))

