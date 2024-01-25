#Programmer: X Gergye
#Program: Variables & Methods
#Date: 1.11.2024

quote = "All is fair in love and war!"
print(quote)

print(quote.upper()) #Uppercase
print(quote.lower()) #Lowercase
print(quote.title()) #Titlecase
print(len(quote)) #Length of characters in our quote

name = "X Gergye" #string
age = 16 #int
gpa = 3.7 #float

print(age)
print(int(gpa)) #Cast a float into an int
print("\nMy name is",name,"and I am",age,"with a GPA of", str(gpa) + ".") #Concating using a comma inatead of a + while casting our gpa variable into a string to account for the spacing before the period

print("\nMy name is " + name + " and I am " + str(age) + " with a GPA of " + str(gpa) + ".") #Concatenate variables while casting an Int to Str

print("")

age += 1 # adds one to the variable age
print(age)

print("")

age += 10 # adds ten to the variable age
print(age)

print("")

birthday = 1
age += birthday #We can add two variables with the values as Int together
print(age)                    
