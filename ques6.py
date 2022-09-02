sentense="I am a teacher and I love to inspire and teach people"
#finding unique words using split method
#split is used to split the string
list0fwords=set(sentense.split(" "))#set contains only unique values
print("unique words:")
print(list0fwords)
print("count:"+str(len(list0fwords)))