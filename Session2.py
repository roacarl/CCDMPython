

# Question 1
x = "Hello"
print(x)

#or
x = "Hello"
print( x + " Carl")

# index
#Question 2
print(x[0])
print(x[1])


#Question 3
x = "Hello World"
# Slicing
s = x[0:3]
print(s)

s = x[:3]
print(s)

# Question 4
#Create a String (give an appropriate name) that takes in User's First name and stores it. 
# Create another String that takes in the User's Surname on a new line.
#Finally, the final output should output a welcome message to the user on the screen

#Concatenation

myname = "Mark"
print("Welcome " + myname + " to CCDM Course")






# List
#Create a list called courses CCMD, CCIT, CCLSA,


courses = "CCMD, CCIT, CCLSA"
print(courses)

courses = ["CCMD","CCIT","CCLSA" ,"CCNS"]
print(courses)

# access item at index 0
print(courses[-2])


#Slicing 

my_list = ['p','r','o','g','r','a','m','i','z']
# items from index 2 to index 4
print(my_list[2:5])

# items from index 5 to end
print(my_list[5:])

# items beginning to end
print(my_list[:])


#using the Append method to insert values into a list
courses.append("CCAIT")
print(courses)


# deleting from the list
del courses[0]
print(courses)


# deleting from the last list
del courses[-1]
print(courses)




#Exercise
#Question1


list = [ "New York", "Los Angles", "Boston", "Denver" ]
print(list)        # prints all elements
print(list[0])     # print first element


list2 = [1,3,4,6,4,7,8,2,3]
print(sum(list2))

print(min(list2))

print(max(list2))

print(list2[0])

print(list2[-1])'''
