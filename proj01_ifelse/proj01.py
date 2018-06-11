# Name:
# Date:

# proj01: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.
#Then, it prints out a sentence that says the number of years until they graduate.

print "HELLO WORLD!!!"
Ur_Name = raw_input("What is your name?")
print "Your name is " + Ur_Name[0].upper() + Ur_Name[1:].lower()
print "I like that name."
Fav_color = raw_input("What is your fav color?")
print "Your favorite color is " + Fav_color + "."
Grade = raw_input("What grade are you in?")
print "Oh, your in " + Grade + " grade."
Left =12-int(Grade)
print "You will graduate highschool in "+ str(Left) + " years!!"
x= raw_input("Can I come to your graduation?")
if x=="yes":
    print "Okay, i'll come"
else:
    print "Alright I won't go"

# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday
Ur_Name = raw_input("What is your name?")
print "Your name is " + Ur_Name[0].upper() + Ur_Name[1:].lower()
print "I like that name."
y= int(raw_input("What is the current day?[number]"))
u= int(raw_input("What is the current month?[number]"))
i= int(raw_input("What is your birth month[number]"))
o= int(raw_input("What is your birth day[number]"))
if i>u:
    print "The number of months until your birthday is" + u-i
else


# If you complete extensions, describe your extensions here!