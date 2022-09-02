it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print("length of the set:"+str(len(it_companies)))
print("adding Twitter it companies")
it_companies.add('Twitter')
print(it_companies)
print("updating multiple it companies")
it_companies.update(['TCS','Infosys'])
print(it_companies)
print("removing an element from it companies")
it_companies.remove("TCS")
#remove() if element present it removes else it raises error in set
#discard() if element present it removes else it'll not raises error in set
print("set after removing element")
print(it_companies)
C=A.union(B)
print("After joining A & B:")
print(C)
D=A.intersection(B)
print("After Intersection A & B:")
print(D)
print("Check A is Subset of B:",end="")
print(A.issubset(B))
print("Check A is Disjoint to B:",end="")
print(A.isdisjoint(B))
print("Join A with B:",end="")
ab=A.union(B)
print(ab)
print("Join B with A:",end="")
ba=B.union(A)
print(ab)
print("joining ab with ba")
print(ab.union(ba))
print(" symmetric difference between A and B:",end='')
print(A.symmetric_difference(B))
print("deleting the sets")
del A
del B
del it_companies
print("deleted")
print("converting the ages list to set:")
print("length of age before conversion:"+str(len(age)))
age=set(age)
print("length of age after conversion:"+str(len(age)))
print(age)