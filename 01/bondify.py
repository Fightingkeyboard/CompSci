#This program is to take a name in first name last name format and print it out in a last name, first name last name format
#Written by: Anthony Chen
#Guarantteed no bamboozoles or your money back!
Name="James Bond"
#The name in first name last name format
NameLength=len(Name)
#The length (int) of the name in first name last name format
SpacePosition=Name.index(" ")
#The position number (int) of the space separating the first name and the last name
LastnameStart=SpacePosition+1
#Finds the length of the last name. The last name starts after the space
Lastname=(Name[LastnameStart:NameLength])
#Finds the last name (string) by starting at the beginning of the last name to the end of Name
print(Lastname,", ",Name,sep="")
#Prints out the name in last name, first name last name format, with a comma and space in between and no unnecessary spaces because of sep is set to nothing