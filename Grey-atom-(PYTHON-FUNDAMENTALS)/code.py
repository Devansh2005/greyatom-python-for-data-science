# --------------
# Code starts here

# Create the lists 
class_1=["Geoffrey Hinton","Andrew Ng ", "Sebastian Raschka","Yoshua Bengio"]
class_2= ["Hilary Mason","Carla Gentry","Corinna Cortes"]

# Concatenate both the strings
new_class=class_1+class_2
print(new_class)

# Append the list
new_class.append("Peter Warden")
# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove("Carla Gentry")
# Print the list
print(new_class)


# Create the Dictionary
courses={"Math":65,"Englsh":70,"History":80,"French":70,"Science":60}
print(courses)



# Slice the dict and stores  the all subjects marks in variable
# print(courses.values())

# Store the all the subject in one variable `Total`
total=sum(courses.values())
# Print the total
print(total)
# Insert percentage formula
percentage=total/5
# Print the percentage
print(percentage)



# Create the Dictionary
mathematics={"Geoffrey Hinton":78,
'Andrew Ng':95,
'Sebastian Raschka':65,
'Yoshua Benjio':50,
'Hilary Mason':70,
'Corinna Cortes':66,
'Peter Warden':75}

# Given string

topper=max(mathematics,key=mathematics.get)
print(topper)

# Create variable first_name 
split_name=topper.split(' ')
first_name=split_name[0]
Last_name=split_name[1]


# Create variable Last_name and store last two element in the list

full_name=Last_name+" "+first_name
# Concatenate the string
certificate_name=full_name.upper()
# print the full_name
print(certificate_name)
# print the name in upper case



