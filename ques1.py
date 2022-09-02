ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort() #sort() is a predefined method which is used to sort a iterator
print("sorted list:")
print(ages)
#FINDING AND ADDING MIN & MAX NUMBERS INTO LIST
#IN QUESTION DID'NT MENTION THE POSITION OF ADDING THE NEW ELEMENTS
#SO BY DEFAULT APPEND() ADD ELEMENTS AT END
min_age = ages[0]
max_age = ages[len(ages)-1]
print("min age: "+str(min_age))
print("max age: "+str(max_age))
ages.append(min_age)
ages.append(max_age)
print("List after adding min and max:")
print(ages)
#FINDING THE MEDIAN VARIES BASED ON LENGTH OF LIST
length=len(ages)
if(length%2==0):
  median_age = (ages[length//2-1]+ages[length//2])/2
else:
  median_age = ages[length//2]
print("Median of ages :"+str(median_age))
#FINDING THE AVERAGE AGE / SUM OF AGES DIVIDED BY LENGTH
average = sum(ages)/len(ages)
print("Average of ages :"+str(average))
range_age = max_age-min_age
#RANGE IS DIFFERENCE B/W MAX AND MIN AGES
print("Range of ages :"+str(range_age))