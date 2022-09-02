#CREATING AN EMPTY DICTIONARY
dog={}
#ADDING KEY VALUE PAIRS
dog['Name']='Tommy'
dog['Color']='White'
dog['Breed']='Bull Dog'
dog['Legs']= 4
dog['Age']=2
print("DOG DICTIONARY: ")
print(dog)
student={}
student['first_name']='jagedeesh'
student['last_name']='Naidu'
student['gender']='Male'
student['age']=24
student['marital_status']='single'
student['skills']=['python','java','C']
student['country']='United states'
student['city']='Warrensburg'
student['address']='Ward Edwards Building, 1400 E South St'
print("STUDENT DICTIONARY: ")
print(student)
#LENGTH OF STUDENT DICTIONARY USING LEN()
print("length of student DICTIONARY:"+str(len(student)))
#ACCESSING THE STUDENT DICTIONARY
print("skills:",end="")
print(student['skills'])
print('\n')
print("Type of Skills key:",end="")
print(type(student['skills']))# type() is to get the datatype
#MODIFY THE SKILL LIST APPENDING THE ELEMENTS
student['skills'].append('C++')
print("after adding another skill:",end="")
print(student['skills'])
print('\n')
#get the keys and values
print("Getting the Dictionary Keys as a list")
print("Dog keys:",end="")
print(list(dog.keys()))
print("Student keys:",end="")
print(list(student.keys()))
print('\n')
print("Getting the Dictionary Values as a list")
print("Dog values:",end="")
print(list(dog.values()))
print("Student values:",end="")
print(list(student.values()))