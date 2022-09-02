#CREATING BROTHERS AND SISTERS TUPLE
brothers = ("danny","john","sam","tony")
sisters = ("Emma","ava","sophia","olivia")
print("brothers tuple:")
print(brothers)
print("sisters tuple:")
print(sisters)
#ADDING TUPLES
siblings=brothers+sisters
print("siblings tuple:")
print(siblings)
print("count of siblings :"+str(len(siblings)))
print("Modifying the tuples:")
#converting the tuple into list and list to tuple
list_sibling=list(siblings)
list_sibling[2]="samuel"
siblings=tuple(list_sibling)
print(siblings)
print("adding father and mother")
parents=("father_","mother_")
family_members=siblings+parents
print(family_members)