# Ask user 5 favorite movies, display only the first 3 movies
# Ask user 5 city names, display only the last 2 cities
# Ask user 5 fruit names, arrange them alphabetically and print
# Ask user 5 fruit names, arrange them in reverse alphabetical order and print
# Ask user 4 favorite games, add one more game at the end and print updated list
# Ask user 5 subject names, remove the subject at index 2 and print remaining subjects
# Ask user 5 numbers, print them in reverse order
#  Ask user 5 movie names, insert "KGF" at index 1 and delete whats on that index exist before new one and print the updated collection
# Ask user 5 city names, print cities from index 1 to index 3
# Ask user 5 names, print names from index 2 till the end
# Ask user 5 colors, display only the first 4 colors
# Store ("Delhi","Mumbai","Delhi","Jammu"), count how many times "Delhi" appears
# Store ("Python","Java","Python","C++"), count occurrences of "Python"
# Store ("Apple","Banana","Orange","Banana"), find the position of "Orange"
# Store (10,20,30,40,50), find the index of 40
# Ask user 5 favorite movies, sort them alphabetically and print
# Ask user 5 favorite movies, sort them in reverse alphabetical order and print
# Ask user 5 fruits, remove "Apple" if it exists and print final collection
# Ask user 5 city names, add "Jammu" at the end and print
# Ask user 5 numbers, insert 100 at index 2 and print-------------------------------------------both methods manual and loop
# Ask user 5 movie names, remove the movie at index 1 and print
# Ask user 5 names, reverse the collection and print
# Ask user 5 colors, sort them and then reverse them
# Ask user 5 subjects, print the subject stored at index 3
# Ask user 5 marks, print marks from index 1 to index 4
# Ask user 5 marks, print all marks except the first one
# Ask user 5 numbers, check whether the first and last numbers are equal
# Ask user 5 movie names, check whether the first movie and last movie are the same
# Ask user 5 numbers, create a copy, reverse the copy and print both collections
# Ask user 5 numbers, create a copy, reverse it and check if it is a palindrome
# Ask user 5 names, insert your own name at index 0 and print
# Ask user 5 fruits, remove the first occurrence of "Mango"
# Store ("Red","Blue","Green","Blue"), count occurrences of "Blue"
# Store ("Jammu","Delhi","Punjab","Haryana"), print the city at index 2
# Ask user 5 movie names, print only the middle 3 movies
# Ask user 5 cities, display them in reverse order
# Ask user 5 favorite foods,sort them alphabetically then add one more food item at index 0 and in last
# Ask user 5 numbers, remove the number at index 3 and print remaining numbers
# Ask user 5 movie names, display only movies from index 2 onwards
# Ask user 5 numbers, reverse them and check if the reversed version is equal to the original
# Store your name in a tuple using ("Abhy"), print its type
# Store your name in a tuple incorrectly using ("Abhy",), print its type
# Store marks in a tuple, try changing the first mark and observe what happens
# Store student details (name, age, city) in one collection and print the city
# Store student details and change the city name, then print updated details
# Store 5 marks and print the mark at index 0
# Store 5 marks and print the mark at index 1
# Store your name using ("Abhy") and ("Abhy",), print both types and compare
# Store a tuple of marks and print the first and last marks
# Store mixed data (name, age, city) and print only the age

# ____________
# Q1
# Ask user 5 favorite movies, display only the first 3 movies
movies = []
for i in range(5):
    # movie = input("Enter favorite movie"+str(i+1))
    movie = input(f"enter fav movie {i+1}")
    movies.append(movie)

print("First 3 movies:",movies[:3] )

# ____________
# Q2
# Ask user 5 city names, display only the last 2 cities
city=[]
for a in range(5):
    ask_city=(input(f"enter city name {a+1}"))
    city.append(ask_city)

print(city [3:])
  
# ____________
# Q3
# Ask user 5 fruit names, arrange them alphabetically and print 
fruits=[]
for a in range(5):
    ask_fruit=(input(f"Tell fruit name {a+1}"))
    fruits.append(ask_fruit)
fruits.sort()
print(fruits)


# ____________
# Q4
# Ask user 5 fruit names, arrange them in reverse alphabetical order and print

fruits=[]
for a in range (5):
    ask_fruit=(input(f"tell fruit name {a+1}"))
    fruits.append(ask_fruit)
fruits.sort(reverse=True)
print(fruits)

# ____________
# Q5
# Ask user 4 favorite games, add one more game at the end and print updated list
games=[]
for g in range(4):
    ask_games=input(f"tell games name {g+1}")
    games.append(ask_games)
games.append("abhy")
print(games)

# ____________
# Q6
# Ask user 5 subject names, remove the subject at index 2 and print remaining subjects
subject=[]
for a in range(5):
    ask=(input(f"favourite subject{a+1}"))
    subject.append(ask)
subject.pop(2)
print(subject)

# #____________
#Q7
# Ask user 5 numbers, print them in reverse order
number=[]
for a in range(5):
    ask_num=(input(f"tell number {a+1}"))
    number.append(ask_num)
number.reverse()
print(number)
   

#____________
#Q8
# Ask user 5 movie names, insert "KGF" at index 1 and delete whats on that index exist before new one and print the updated collection
movies=[]
for a in range(5):
    movie=(input(f"tell movie {a+1}"))
    movies.append(movie)
movies.insert(1,"kgf")
movies.pop(2)
print(movies)



#____________
#Q9
#Ask user 5 city names, print cities from index 1 to index 3
city=[]
for a in range(5):
    ask_city=(input(f"tell city {a+1}"))
    city.append(ask_city)
print(city[1:4])

#____________
#Q10
# Ask user 5 names, print names from index 2 till the end
names=[]
for a in range(5):
    ask_name=input(f"tell names {a+1}")
    names.append(ask_name)
print(names[2:])

#____________
#Q11
# Ask user 5 colors, display only the first 4 colors
colours=[]
for a in range(5):
    ask_colour=input(f"tell colour {a+1}")
    colours.append(ask_colour)
print(colours[0:4])

#____________
#Q12
# Store ("Delhi","Mumbai","Delhi","Jammu"), count how many times "Delhi" appears
store=["Delhi","Mumbai","Delhi","Jammu"]
print(store.count("Delhi"))



#____________
#Q13
# Store ("Python","Java","Python","C++"), count occurrences of "Python"

store=["Python","Java","Python","C++"]
print(store.count("Python"))

#____________
#Q14
# Store ("Apple","Banana","Orange","Banana"), find the position of "Orange"
store=["apple","Banana","Orange","Banana"]
print(store.index("Orange"))


#____________
#Q15
# Store (10,20,30,40,50), find the index of 40
store=[10,20,30,40,50]
print(store.index(40))

#____________
#Q16
# Ask user 5 favorite movies, sort them alphabetically and print
movies=[]
for a in range(5):
    ask_movies=(input(f"tell movie {a+1}"))
    movies.append(ask_movies)
movies.sort()
print(movies)


#____________
#Q17
# Ask user 5 favorite movies, sort them in reverse alphabetical order and print
movies=[]
for a in range(5):
    ask_movies=(input(f"tell movie {a+1}"))
    movies.append(ask_movies)
movies.sort(reverse=True)
print(movies)


#____________
#Q18
# Ask user 5 fruits, remove "Apple" if it exists and print final collection
fruits=[]
for a in range (5):
    ask_fruits=(input(f"tell fruit {a+1}"))
    fruits.append(ask_fruits)

if "Apple" in fruits:
    fruits.remove("Apple")
print(fruits)

#____________
#Q19
# Ask user 5 city names, add "Jammu" at the end and print
city=[]
for a in range(5):
    ask_city=(input(f"tell city {a+1}"))
    city.append(ask_city)
city.append("Jammu")
print(city)

#____________
#Q20
# Ask user 5 numbers, insert 100 at index 2 and print it 
num1=(input("tell no 1 "))
num2=(input("tell no 2 "))
num3=(input("tell no 3 "))
num4=(input("tell no 4"))
num5=(input("tell no 5 "))
ask_num=[num1,num2,num3,num4,num5]
ask_num.insert(2,100)
print(ask_num)

#-----------------------------------------------------------

number=[]
for a in range(5):
    ask_num=(input(f"tell num {a+1}"))
    number.append(ask_num)
number.insert(2,100)
print(number)

#___________
#Q21
# Ask user 5 movie names, remove the movie at index 1 and print
movies=[]
for a in range(5):
    ask_movie=(input(f"tell movie {a+1}"))
    movies.append(ask_movie)
movies.pop(1)
print(movies)

# ____________
# Q22
# Ask user 5 names, reverse the collection and print
names=[]
for a in range(5):
    ask_names=(input(f"tell name {a+1}"))
    names.append(ask_names)
names.reverse()
print (names)


#____________
#Q23
# Ask user 5 colors, sort them and then reverse them
colours=[]
for a in range(5):
    ask_colour=(input(f"tell colour {a+1}"))
    colours.append(ask_colour)
colours.sort()
colours.reverse()
print(colours)

#____________
#Q24
# Ask user 5 subjects, print the subject stored at index 3
subject=[]
for a in range(5):
    ask_subject=(input(f"tell sub {a+1}"))
    subject.append(ask_subject)
print(subject[3])

#____________
#Q25
# Ask user 5 marks, print marks from index 1 to index 4
marks=[]
for a in range (5):
    ask_marks=int(input(f"marks of sub {a+1}"))
    marks.append(ask_marks)
print(marks[1:5])

#____________
#Q26
# Ask user 5 marks, print all marks except the first one
marks=[]
for a in range(5):
    ask_marks=int(input(f"marks of sub{a+1}"))
    marks.append(ask_marks)
marks.pop(0)
print(marks)

#____________
#Q27
# Ask user 5 numbers, check whether the first and last numbers are equal
numbers=[]
for a in range(5):
    ask_number=int(input(f"tell num {a+1}: "))
    numbers.append(ask_number)
if(numbers[0]==numbers[4]):
    print(numbers,"first and last are equal")
else:
    print("not equal")


#____________
#Q28
# Ask user 5 movie names, check whether the first movie and last movie are the same
movies=[]
for a in range(5):
    ask_movie=(input(f"tell movie {a+1}"))
    movies.append(ask_movie)
if(movies[0]==movies[4]):
    print("same",movies)
else:
    print("not same")

#___________
#Q29
# Ask user 5 numbers, create a copy, reverse the copy and print both collections
numbers=[]
for a in range(5):
    ask_number=int(input(f"tell num {a+1}"))
    numbers.append(ask_number)
copy=(numbers.copy())
(numbers.reverse())
print(copy)
print(numbers)


# ____________
# Q30
# Ask user 5 numbers, create a copy, reverse it and check if it is a palindrome
numbers=[]
for a in range(5):
    ask_numbers=int(input(f"tell no {a+1}"))
    numbers.append(ask_numbers)
copy=(numbers.copy()) 
print(copy)
numbers.reverse()
print(numbers)

if(copy == numbers):
    print("its Palindrome")
else:
    print("not a Palindrome")


#____________
#Q31
# Ask user 5 names, insert your own name at index 0 and print
names=[]
for a in range (5):
    ask_names=(input(f"tell names{a+1}"))
    names.append(ask_names)
names.insert(0,"Abhy")
print(names)

#____________
#Q32
# Ask user 5 fruits, remove the first occurrence of "Mango"
fruits=[]
for a in range (5):
    ask_fruits=(input(f"tell fruit {a+1}"))
    fruits.append(ask_fruits)
if("Mango"in fruits):
    (fruits.remove("Mango"))
    print(fruits)
else:
    print  ("no mango in list ")

 
#____________
#Q33
# Store ("Red","Blue","Green","Blue"), count occurrences of "Blue"
store=["red","blue","green","blue"]
counting=store.count("blue")
print("occurence of blue is:" ,counting)

#____________
#Q34
# Store ("Jammu","Delhi","Punjab","Haryana"), print the city at index 2

store=["Jammu","Delhi","Punjab","Haryana"]
print("city at index 2 is :", store[2])

#____________
#Q35
# Ask user 5 movie names, print only the middle 3 movies
movies=[]
for a in range(5):
    ask_movie=(input(f"movies tell{a+1}"))
    movies.append(ask_movie)
print(movies[2:5])

#____________
#Q36
# Ask user 5 cities, display them in reverse order
cities=[]
for a in range(5):
    ask_cities=(input(f"tell cities{a+1}"))
    cities.append(ask_cities)
cities.reverse()
print(cities)

#____________
#Q37
#Ask user 5 favorite foods,sort them alphabetically then add one more food item at index 0 and in last
foods=[]
for a in range(5):
    ask_foods=(input(f"tell food {a+1}"))
    foods.append(ask_foods)
foods.sort()
foods.append("abhy")
foods.insert(0,"Abhy")
print(foods)

#____________
#Q38
# Ask user 5 numbers, remove the number at index 3 and print remaining numbers
number=[]
for a in range (5):
    ask_num=(input(f"tell number {a+1}"))
    number.append(ask_num)
number.pop(3)
print(number)

#____________
#Q39
# Ask user 5 movie names, display only movies from index 2 onwards
movies=[]
for a in range (5):
    ask_movies=(input(f"tell number {a+1}"))
    movies.append(ask_movies)
print(movies[2:])


#____________
#Q40
# Ask user 5 numbers, reverse them and check if the reversed version is equal to the original
numbers=[]
for a in range (5):
    ask_num=(input(f"tell number {a+1}"))
    numbers.append(ask_num)
copy=numbers.copy()
numbers.reverse()
if(copy == numbers):
    print("yes")
else:
    print("no")


#____________
#Q41
# Store your name in a tuple using ("Abhy"), print its type
name=("abhy",)
print(type(name))

#____________
#Q42
# Store your name in a tuple incorrectly using ("Abhy",), print its type
name=("abhy")
print(type(name))

#____________
#Q43
# Store marks in a tuple, try changing the first mark and observe what happens
marks=(35,45,65,24,36)
print(type(marks))
marks.remove(35)
print(marks)# didnot remove becouse in tupler objects cannot change its fixed if still want 
            #to remove use list by making marks=[35,45,65,24,36] 

#____________
#Q44
# Store student details (name, age, city) in one collection and print the city
details=("abhy",20,"Kashmir")
print(details[2])

#____________
#Q45
# Store student details and change the city name, then print updated details
details=("abhy",25,"kashmir")
details=list(details)
details[2]="delhi"
details=tuple(details)
print(details)

#____________
#Q46
# Store 5 marks and print the mark at index 0
marks=[]
for a in range(5):
    ask_marks=int(input(f"marks for sub"))
    marks.append(ask_marks)
print(marks[0])


____________
# Q47
# Store 5 marks and print the mark at index 1
marks=[]
for a in range(5):
    ask_marks=int(input(f"marks for sub"))
    marks.append(ask_marks)
print(marks[1])


#____________
#Q48
# Store your name using ("Abhy") and ("Abhy",), print both types and compare
store1=("Abhy")
store2=("Abhy",)
print(type(store1))
print(type(store2))

#____________
#Q49
# Store a tuple of marks and print the first and last marks
marks=25,45,65,75,85
print(marks[0],"\t",marks[-1])

#____________
#Q50
# Store mixed data (name, age, city) and print only the age
data=("abhy",25,"baramulla")
print(data[1])
