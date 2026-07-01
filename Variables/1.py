
#VARIABLES
a= 100
#DECLARING AND ASSIGNING VARIABLE
age = 32
height = 6.1
name = "Pr"
is_student = True

#printing the varibale
print("age :" , age)
print("height :", height)
print("Name :", name)


#Naming Convention 

#Variable names should be descriptive
#they must always start with  a letter or an '_' and can contain letter,numbers and underscores
#variables names are case sensitive

#valid variable names

first_name = "Pri"
last_name = "Jai"



# #invalid names
# #error
# 2age = 30
# first-name= "Pri"
# @name = "Jai"



#Case sesitivity
name = "Pri"
Name = "Jai"
print(name==Name)


#Understanding Variable types
#Python is dyanimacally typed, type of a variable is determined at run time
age1 = 25 #integer
height1 = 6.1 #float
name1 = "Pri" #str
is_student1= True #boolean
print(type(age1))
print(type(height1))
print(type(name1))
print(type(is_student1))



#TYPE CHECKING AND CONVERSION
type(height)

#conversion 

age2 = 25;
print(type(age2))

#Type Conversion

age_str = str(age2)
print (age_str)
print(type(age_str))

age4= '25'
int(age4)

age5 = '25'
print(type(int(age5)))


# #ERROR
# name2 = "Pri"
# print( int(name2))
# '''


ht = 5.11
type = type(height)
print(type)

#float to int
int(ht)

#int to float
float(int(ht))



