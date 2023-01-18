list1=["vaidik","nirjal","jaydeep","dharmiik","divyesh","darshan","prince","abhay"]
for i in list1:
    print(i)
list2=[["vaidik", 508],["darshan",491],["nirjal",332],["prince",510],["sahil",515]]

for i,j in list2:
    print(i,"And enrolment is ",j)

dict1 = dict(list2)

for i in dict1:
    print(i) #Prints only key

for i,j in dict1.items(): #iteam() function is used to fatch the key and values
    print(i,"and enroment is ",j)
